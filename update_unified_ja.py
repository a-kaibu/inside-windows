import re
import os

print("Building unified ja.html (removing cover photo, copyright/imprint, and raw contents)...")

with open('part1.html', 'r', encoding='utf-8') as f:
    p1_html = f.read()

with open('part2.html', 'r', encoding='utf-8') as f:
    p2_html = f.read()

# Load translated pages
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
    'Introduction': 'はじめに',
    'Acknowledgments': '謝辞',
    'Chapter 1 Concepts and tools': '第1章 概念とツール',
    'Windows operating system versions': 'Windows OS のバージョン',
    'Windows 10 and future Windows versions': 'Windows 10 と将来のバージョン',
    'Windows 10 and OneCore': 'Windows 10 と OneCore',
    'Foundation concepts and terms': '基本概念と用語',
    'Windows API': 'Windows API',
    'Services, functions, and routines': 'サービス、関数、ルーチン',
    'Processes': 'プロセス',
    'Threads': 'スレッド',
    'Jobs': 'ジョブ',
    'Virtual memory': '仮想メモリ',
    'Kernel mode vs. user mode': 'カーネルモードとユーザーモード',
    'Hypervisor': 'ハイパーバイザー',
    'Firmware': 'ファームウェア',
    'Terminal Services and multiple sessions': 'ターミナルサービスとマルチセッション',
    'Objects and handles': 'オブジェクトとハンドル',
    'Security': 'セキュリティ',
    'Registry': 'レジストリ',
    'Unicode': 'Unicode',
    'Digging into Windows internals': 'Windows 内部の深掘り',
    'Performance Monitor and Resource Monitor': 'パフォーマンスモニターとリソースモニター',
    'Kernel debugging': 'カーネルデバッグ',
    'Windows Software Development Kit': 'Windows SDK',
    'Windows Driver Kit': 'Windows Driver Kit (WDK)',
    'Sysinternals tools': 'Sysinternals ツール',
    'Conclusion': 'まとめ',
    'Chapter 2 System architecture': '第2章 システムアーキテクチャ',
    'Requirements and design goals': '要件と設計目標',
    'Operating system model': 'オペレーティングシステムモデル',
    'Architecture overview': 'アーキテクチャの全体像',
    'Portability': '移植性',
    'Symmetric multiprocessing': '対称型マルチプロセッシング (SMP)',
    'Scalability': 'スケーラビリティ',
    'Differences between client and server versions': 'クライアント版とサーバー版の違い',
    'Checked build': 'チェックドビルド',
    'Virtualization-based security architecture overview': '仮想化ベースのセキュリティ (VBS) アーキテクチャ概要',
    'Key system components': '主要システムコンポーネント',
    'Environment subsystems and subsystem DLLs': '環境サブシステムとサブシステム DLL',
    'Other subsystems': 'その他のサブシステム (WSL 等)',
    'Executive': 'エグゼクティブ',
    'Kernel': 'カーネル',
    'Hardware abstraction layer': 'ハードウェア抽象化レイヤー (HAL)',
    'Device drivers': 'デバイスドライバ',
    'System processes': 'システムプロセス',

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

# Remove unwanted links from TOC: Cover, Title Page, Copyright Page, Contents
unwanted_toc = {'Cover', 'Title Page', 'Copyright Page', 'Contents', 'Contents at a Glance'}

def clean_and_translate_aside(aside_html, id_prefix=''):
    def repl(m):
        style = m.group(1)
        href = m.group(2)
        text = m.group(3).strip()
        if text in unwanted_toc:
            return ''  # Delete from TOC
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
<label id="sizeLabel" style="margin-left:auto">文字 <button id="smaller" aria-label="文字を小さく">−</button> <button id="larger" aria-label="文字を大きく">＋</button></label>
</header>"""

# 4. Intro block
unified_intro = """<div class="intro">
<div style="margin-top:10px;padding:8px 12px;background:var(--panel);border-radius:4px;font-size:14px;">
<strong>現在の翻訳状況：</strong> 「はじめに」および「第1章 概念とツール」（全44ページ分）が日本語化完了済みです。第2章以降の英文骨格もすべて移植済みで、順次日本語へ更新されます。
</div>
</div>"""

# Pages to omit:
# Part 1: page-1 (Cover), page-2 (Title Page), page-3 (Copyright), page-4..page-11 (Contents)
p1_omit = {f"page-{i}" for i in range(1, 12)}

# Part 2: p2-page-1 (Cover), p2-page-2 (Title), p2-page-3 (Copyright), p2-page-4..p2-page-18 (Contents at a Glance / Contents)
p2_omit = {f"p2-page-{i}" for i in range(1, 19)}

# 5. Extract and clean Part 1 pages
p1_pages = re.findall(r'<section class=\"page\" id=\"(page-\d+)\"[^>]*>(.*?)</section>', p1_html, re.DOTALL)
body_sections = []

for pid, content in p1_pages:
    if pid in p1_omit:
        continue
    if pid in translated_dict:
        clean_content = translated_dict[pid]
        body_sections.append(f'<section class="page" id="{pid}" aria-label="{pid}">{clean_content}</section>')
    else:
        cleaned = re.sub(r'<details>.*?</details>', '', content, flags=re.DOTALL)
        cleaned = re.sub(r'<div class="pagebar">.*?</div>', '', cleaned, flags=re.DOTALL)
        body_sections.append(f'<section class="page" id="{pid}" aria-label="{pid}">{cleaned}</section>')

# 6. Extract and clean Part 2 pages
p2_pages = re.findall(r'<section class=\"page\" id=\"(page-\d+)\"[^>]*>(.*?)</section>', p2_html, re.DOTALL)
for pid, content in p2_pages:
    p2_pid = f"p2-{pid}"
    if p2_pid in p2_omit:
        continue
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
function navigate(id){const target=document.getElementById(id);if(!target)return;location.hash=id;target.scrollIntoView();setTimeout(()=>target.scrollIntoView(),150);setTimeout(()=>target.scrollIntoView(),450)};document.querySelectorAll('aside a').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();navigate(a.hash.slice(1))}));
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
print(f"Updated ja.html: {size_mb:.2f} MB ({len(body_sections)} pages)")
