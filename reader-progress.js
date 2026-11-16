/* Store a text block and its reading offset, so image loading and reflow do not
   invalidate a saved position as they would a document-wide scrollY value. */
(() => {
  const key = 'inside-windows:reading-position:v1:' + location.pathname;
  const pages = [...document.querySelectorAll('section.page')];
  if (!pages.length) return;
  const readingLine = () => (document.querySelector('header')?.getBoundingClientRect().bottom || 0) + 20;
  let suspended = true;
  let timer;
  let saved;
  try { saved = JSON.parse(localStorage.getItem(key)); } catch (_) {}

  function save() {
    if (suspended) return;
    try {
      const y = readingLine();
      let lo = 0, hi = pages.length - 1, index = -1;
      while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (pages[mid].getBoundingClientRect().top <= y) { index = mid; lo = mid + 1; }
        else hi = mid - 1;
      }
      let state = { version: 1, top: true, hash: location.hash };
      if (index >= 0) {
        const page = pages[index];
        const blocks = [...page.children];
        let block = 0;
        for (let i = 0; i < blocks.length; i++) {
          if (blocks[i].getBoundingClientRect().top <= y) block = i;
          else break;
        }
        const target = blocks[block];
        const rect = target.getBoundingClientRect();
        state = { version: 1, page: page.id, block,
          fraction: Math.max(0, Math.min(1, (y - rect.top) / Math.max(1, rect.height))),
          open: target.tagName === 'DETAILS' && target.open, hash: location.hash };
      }
      localStorage.setItem(key, JSON.stringify(state));
    } catch (_) { /* Reading remains available when browser storage is blocked. */ }
  }
  addEventListener('scroll', () => {
    clearTimeout(timer);
    timer = setTimeout(save, 400);
  }, { passive: true });
  addEventListener('pagehide', save);
  document.addEventListener('visibilitychange', () => { if (document.hidden) save(); });

  const valid = saved?.version === 1 &&
    (saved.top === true || (typeof saved.page === 'string' && Number.isInteger(saved.block) &&
      saved.block >= 0 && Number.isFinite(saved.fraction) && saved.fraction >= 0 && saved.fraction <= 1));
  // A newly requested chapter link takes priority; reloading the same URL can
  // still resume past its old hash anchor after the reader scrolled further.
  const resume = valid && (!location.hash || location.hash === saved.hash);
  if (!resume) { suspended = false; return; }

  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  let cancelled = false;
  const cancel = () => { cancelled = true; suspended = false; };
  for (const name of ['wheel', 'touchstart', 'pointerdown', 'keydown']) {
    addEventListener(name, cancel, { passive: true, once: true });
  }
  function restore() {
    if (cancelled) return;
    const page = saved.top ? null : document.getElementById(saved.page);
    const target = page?.children[saved.block];
    if (!saved.top && !target) { suspended = false; return; }
    if (saved.open && target.tagName === 'DETAILS') target.open = true;
    // Materialize this page before computing its text block's geometry.
    if (page) page.style.contentVisibility = 'visible';
    const start = performance.now();
    let stable = 0;
    const settle = () => {
      if (cancelled) return;
      const delta = saved.top ? -scrollY : target.getBoundingClientRect().top +
        saved.fraction * target.getBoundingClientRect().height - readingLine();
      if (Math.abs(delta) > 1) { scrollBy(0, delta); stable = 0; }
      else stable++;
      // Let surrounding pages, lazy images and the original-page expander
      // finish changing layout before releasing the saved anchor.
      if (performance.now() - start < 2200 && (stable < 5 || performance.now() - start < 650)) {
        setTimeout(settle, 80);
      } else {
        suspended = false;
        if (page) page.style.contentVisibility = '';
      }
    };
    requestAnimationFrame(settle);
  }
  if (document.readyState === 'complete') restore();
  else addEventListener('load', restore, { once: true });
  addEventListener('pageshow', e => { if (e.persisted) { cancelled = true; suspended = false; } });
})();
