import re
import os

print("Building unified ja.html skeleton with all chapters...")

with open('part1.html', 'r', encoding='utf-8') as f:
    p1_html = f.read()

with open('part2.html', 'r', encoding='utf-8') as f:
    p2_html = f.read()

# Try loading translated pages if available
try:
    import translate_pages
    translated_dict = translate_pages.pages_ja
except Exception as e:
    translated_dict = {}

# 1. Header & Styles
head_match = re.search(r'(<head>.*?</head>)', p1_html, re.DOTALL)
head_html = head_match.group(1) if head_match else ''
head_html = re.sub(r'<title>.*?</title>', '<title>Windows Internals 第7版 — Reader (日本語統合版)</title>', head_html)

# 2. Unified TOC
aside1 = p1_html[p1_html.find('<aside'):p1_html.find('</aside>')+8]
aside2 = p2_html[p2_html.find('<aside'):p2_html.find('</aside>')+8]

chapter_trans = {
    'Cover': '表紙',
    'Title Page': 'タイトル',
    'Copyright Page': '権利表記',
    'Acknowledgments': '謝辞',
    'Contents': '目次',
    'Introduction': 'はじめに',
    'Chapter 1 Concepts and tools': '第1章 概念とツール',
    'Chapter 2 System architecture': '第2章 システムアーキテクチャ',
    'Chapter 3 Processes and jobs': '第3章 プロセスとジョブ',
    'Chapter 4 Threads': '第4章 スレッド',
    'Chapter 5 Memory management': '第5章 メモリ管理',
    'Chapter 6 I/O system': '第6章 I/O システム',
    'Chapter 7 Security': '第7章 セキュリティ',
    'Chapter 8 System mechanisms': '第8章 システムメカニズム',
    'Chapter 9 Virtualization technologies': '第9章 仮想化技術',
    'Chapter 10 Management, diagnostics, and tracing': '第10章 管理、診断、トレース',
    'Chapter 11 Caching and file systems': '第11章 キャッシュとファイルシステム',
    'Chapter 12 Startup and shutdown': '第12章 起動とシャットダウン',
}

def clean_and_translate_aside(aside_html, id_prefix=''):
    def repl(m):
        style = m.group(1)
        href = m.group(2)
        text = m.group(3).strip()
        trans = chapter_trans.get(text, text)
        new_href = href if not id_prefix else f"#{id_prefix}{href[1:]}"
        return f'<a {style} href="{new_href}">{trans}</a>'
    return re.sub(r'<a (style=\"[^\"]+\") href=\"(#[^\"]+)\">([^<]+)</a>', repl, aside_html)

new_aside1 = clean_and_translate_aside(aside1)
new_aside2 = clean_and_translate_aside(aside2, id_prefix='p2-')

unified_aside = f"""<aside aria-label="Table of contents">
<h2>目次</h2>
<div style="font-weight:bold;margin:10px 0 5px;color:var(--accent);">■ Part 1</div>
{new_aside1[new_aside1.find('</h2>')+5:new_aside1.find('</aside>')]}
<div style="font-weight:bold;margin:20px 0 5px;color:var(--accent);">■ Part 2</div>
{new_aside2[new_aside2.find('</h2>')+5:new_aside2.find('</aside>')]}
</aside>"""

# 3. Reader Header Bar
unified_header = """<header>
<button id="tocToggle" aria-label="目次を開閉">☰ 目次</button>
<a href="./" style="text-decoration:none" aria-label="本棚へ戻る">← 本棚</a>
<strong>Windows Internals 第7版 · 日本語統合版</strong>
<label id="sizeLabel">文字 <button id="smaller" aria-label="文字を小さく">−</button> <button id="larger" aria-label="文字を大きく">＋</button></label>
<label>Part 1 頁 <input id="pageInput" type="number" min="1" max="801" value="1"></label>
<button id="jump">移動</button>
</header>"""

# 4. Intro block
unified_intro = """<div class="intro">
<h1>Windows Internals 第7版<br>日本語統合版 (Part 1 &amp; Part 2)</h1>
<p>本書は『Windows Internals Seventh Edition』Part 1 および Part 2 の全1,713ページを統合したWebリーダーです。</p>
<p>「原本ページを表示」展開枠およびPDF特有のページ境界バーをすべて排除し、文章としてスムーズに通読できるようにレイアウトを整形しています。翻訳完了済みの章から順次、自然で読みやすい日本語テキストへと差し替えを行っています。</p>
<div style="margin-top:10px;padding:8px 12px;background:var(--panel);border-radius:4px;font-size:14px;">
<strong>現在の翻訳状況：</strong> 前付（はじめに・謝辞等）および「第1章 概念とツール」（全44ページ分）が日本語化完了済みです。第2章以降の英文骨格もすべて移植済みで、順次日本語へ更新されます。
</div>
</div>"""

# 5. Extract and clean Part 1 pages
p1_pages = re.findall(r'<section class=\"page\" id=\"(page-\d+)\"[^>]*>(.*?)</section>', p1_html, re.DOTALL)
body_sections = []

for pid, content in p1_pages:
    if pid in translated_dict:
        clean_content = translated_dict[pid]
        body_sections.append(f'<section class="page" id="{pid}" aria-label="{pid}">{clean_content}</section>')
    else:
        # Strip details (原本ページを表示) and pagebar
        cleaned = re.sub(r'<details>.*?</details>', '', content, flags=re.DOTALL)
        cleaned = re.sub(r'<div class="pagebar">.*?</div>', '', cleaned, flags=re.DOTALL)
        body_sections.append(f'<section class="page" id="{pid}" aria-label="{pid}">{cleaned}</section>')

# 6. Extract and clean Part 2 pages
p2_pages = re.findall(r'<section class=\"page\" id=\"(page-\d+)\"[^>]*>(.*?)</section>', p2_html, re.DOTALL)
for pid, content in p2_pages:
    p2_pid = f"p2-{pid}"
    if p2_pid in translated_dict:
        clean_content = translated_dict[p2_pid]
        body_sections.append(f'<section class="page" id="{p2_pid}" aria-label="{p2_pid}">{clean_content}</section>')
    else:
        cleaned = re.sub(r'<details>.*?</details>', '', content, flags=re.DOTALL)
        cleaned = re.sub(r'<div class="pagebar">.*?</div>', '', cleaned, flags=re.DOTALL)
        body_sections.append(f'<section class="page" id="{p2_pid}" aria-label="{p2_pid}">{cleaned}</section>')

# 7. Footer & Script
script_and_footer = """<footer>
Windows Internals 第7版 Web Reader (日本語統合版)<br>
書籍の著作権は各権利者（Pavel Yosifovich, Alex Ionescu, Mark E. Russinovich, David A. Solomon, Microsoft Press）に帰属します。
</footer>
</main>
<script>
document.querySelectorAll('details').forEach(d=>d.addEventListener('toggle',()=>{if(d.open){const i=d.querySelector('img');if(i.dataset.src){i.src=i.dataset.src;delete i.dataset.src}}}));
document.getElementById('tocToggle').onclick=()=>{if(innerWidth<=900)document.body.classList.toggle('mobile-toc');else document.body.classList.toggle('toc-hidden')};
document.querySelectorAll('aside a').forEach(a=>a.onclick=()=>document.body.classList.remove('mobile-toc'));
function navigate(id){const target=document.getElementById(id);if(!target)return;location.hash=id;target.scrollIntoView();setTimeout(()=>target.scrollIntoView(),150);setTimeout(()=>target.scrollIntoView(),450)};document.querySelectorAll('aside a').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();navigate(a.hash.slice(1))}));function jump(){const n=Math.max(1,Math.min(801,Number(document.getElementById('pageInput').value)||1));navigate('page-'+n)}document.getElementById('jump').onclick=jump;document.getElementById('pageInput').onkeydown=e=>{if(e.key==='Enter')jump()};
let size=18;document.getElementById('larger').onclick=()=>{size=Math.min(28,size+1);document.documentElement.style.fontSize=size+'px'};document.getElementById('smaller').onclick=()=>{size=Math.max(14,size-1);document.documentElement.style.fontSize=size+'px'};
</script>
<script src="reader-progress.js"></script>
</body>
</html>"""

full_html = f"""<!doctype html>
<html lang="ja">
{head_html}
<body>
{unified_header}
{unified_aside}
<main>
{unified_intro}
{''.join(body_sections)}
{script_and_footer}
"""

with open('ja.html', 'w', encoding='utf-8') as out:
    out.write(full_html)

size_mb = os.path.getsize('ja.html') / (1024 * 1024)
print(f"Generated unified ja.html: {size_mb:.2f} MB ({len(body_sections)} pages)")
