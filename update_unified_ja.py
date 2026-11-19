import re
import html as html_module
import os

from translate_pages import pages_ja
from translate_new_pages import new_pages_ja

print("Building unified ja.html (removing cover photo, copyright/imprint, and raw contents)...")

with open('part1.html', 'r', encoding='utf-8') as f:
    p1_html = f.read()

with open('part2.html', 'r', encoding='utf-8') as f:
    p2_html = f.read()

translated_dict = {**pages_ja, **new_pages_ja}

# 1. Header & Styles
head_match = re.search(r'(<head>.*?</head>)', p1_html, re.DOTALL)
head_html = head_match.group(1) if head_match else ''
head_html = re.sub(r'<title>.*?</title>', '<title>Windows Internals 第7版 — Reader (日本語統合版)</title>', head_html)
favicon = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🪟</text></svg>">'
if not re.search(r'<link[^>]+rel=["\'](?:shortcut )?icon', head_html, re.I):
    head_html = head_html.replace('</title>', f'</title>{favicon}', 1)

# 2. The table of contents is built from the headings that are actually rendered.

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
    'Creating a process': 'プロセスの作成',
    'CreateProcess* functions arguments': 'CreateProcess* 関数の引数',
    'Creating Windows modern processes': 'Windows Modern プロセスの作成',
    'Creating other kinds of processes': 'その他のプロセス作成',
    'Process internals': 'プロセスの内部構造',
    'Protected processes': '保護プロセス (Protected Processes)',
    'Protected Process Light (PPL)': '保護プロセスライト（PPL）',
    'Third-party PPL support': 'サードパーティ製 PPL のサポート',
    'Minimal and Pico processes': 'Minimal プロセスと Pico プロセス',
    'Minimal processes': 'Minimal プロセス',
    'Pico processes': 'Pico プロセス',
    'Trustlets (secure processes)': 'トラストレット (セキュアプロセス)',
    'Trustlet structure': 'トラストレットの構造',
    'Trustlet policy metadata': 'トラストレットのポリシーメタデータ',
    'Trustlet attributes': 'トラストレットの属性',
    'System built-in Trustlets': 'システム組み込みのトラストレット',
    'Trustlet identity': 'トラストレットの識別情報',
    'Isolated user-mode services': '分離ユーザーモード (IUM) サービス',
    'Trustlet-accessible system calls': 'トラストレットが利用可能なシステムコール',
    'Flow of CreateProcess': 'CreateProcess の実行フロー',
    'Stage 1: Converting and validating parameters and flags': '第1段階: パラメータとフラグの変換と検証',
    'Stage 2: Opening the image to be executed': '第2段階: 実行対象イメージのオープン',
    'Stage 3: Creating the Windows executive process object': '第3段階: Windows エグゼクティブプロセスオブジェクトの作成',
    'Stage 4: Creating the initial thread and its stack and context': '第4段階: 初期スレッドとそのスタックおよびコンテキストの作成',
    'Stage 5: Performing Windows subsystem–specific initialization': '第5段階: Windows サブシステム固有の初期化の実行',
    'Stage 6: Starting execution of the initial thread': '第6段階: 初期スレッドの実行開始',
    'Stage 7: Performing process initialization in the context of the new process': '第7段階: 新プロセスのコンテキストでの初期化実行',
    'Terminating a process': 'プロセスの終了',
    'Image loader': 'イメージローダー (Ldr)',
    'Early process initialization': 'プロセスの初期化シーケンス',
    'DLL name resolution and redirection': 'DLL 名の解決とリダイレクション',
    'Loaded module database': 'ロード済みモジュールデータベース',
    'Import parsing': 'インポートテーブルの解析',
    'Post-import process initialization': 'インポート完了後のプロセス初期化',
    'SwitchBack': 'SwitchBack (後方互換性エンジン)',
    'API Sets': 'API セット (API Sets)',
    'Jobs': 'ジョブ',
    'Job limits': 'ジョブの制限設定',
    'Working with a job': 'ジョブの操作と活用',
    'Nested jobs': 'ネストされたジョブ',
    'Windows containers (server silos)': 'Windows コンテナ (Server Silos)',

    'Chapter 4 Threads': '第4章 スレッド',
    'Creating threads': 'スレッドの作成',
    'Thread internals': 'スレッドの内部構造',
    'Data structures': 'スレッドのデータ構造',
    'Birth of a thread': 'スレッドの誕生フロー',
    'Examining thread activity': 'スレッド活動の調査',
    'Limitations on protected process threads': '保護プロセススレッドに対する制約',
    'Thread scheduling': 'スレッドスケジューリング',
    'Overview of Windows scheduling': 'Windows スケジューリングの概要',
    'Priority levels': '優先度レベル (Priority Levels)',
    'Thread states': 'スレッドの状態遷移',
    'Dispatcher database': 'ディスパッチャデータベース',
    'Quantum': 'クォンタム (タイムスライス)',
    'Priority boosts': '優先度ブースト (Priority Boosts)',
    'Context switching': 'コンテキストスイッチ',
    'Scheduling scenarios': 'スケジューリングシナリオ',
    'Idle threads': 'アイドルスレッド',
    'Thread suspension': 'スレッドの一時停止 (サスペンド)',
    '(Deep) freeze': 'ディープフリーズ (省電力サスペンド)',
    'Thread selection': 'スレッドの選定アルゴリズム',
    'Multiprocessor systems': 'マルチプロセッサシステム',
    'Thread selection on multiprocessor systems': 'マルチプロセッサでのスレッド選定',
    'Processor selection': 'プロセッサの選定ロジック',
    'Heterogeneous scheduling (big.LITTLE)': 'ヘテロジニアススケジューリング (big.LITTLE)',
    'Group-based scheduling': 'グループベースのスケジューリング',
    'Dynamic fair share scheduling': '動的フェアシェアスケジューリング (DFSS)',
    'CPU rate limits': 'CPU レート制限',
    'Dynamic processor addition and replacement': '動的なプロセッサ追加と交換',
    'Worker factories (thread pools)': 'ワーカファクトリ (スレッドプール基盤)',
    'Worker factory creation': 'ワーカファクトリの生成',

    'Chapter 5 Memory management': '第5章 メモリ管理',
    'Chapter 6 I/O system': '第6章 I/O システム',
    'Chapter 7 Security': '第7章 セキュリティ',
    'Chapter 8 System mechanisms': '第8章 システムメカニズム',
    'Chapter 9 Virtualization technologies': '第9章 仮想化技術',
    'About the Authors': '著者について',
    'Foreword': '序文',
    'Processor execution model': 'プロセッサの実行モデル',
    'Segmentation': 'セグメンテーション',
    'Task state segments': 'タスク状態セグメント',
    'Hardware side-channel vulnerabilities': 'ハードウェアのサイドチャネル脆弱性',
    'Out-of-order execution': 'アウト・オブ・オーダー実行',
    'The CPU branch predictor': 'CPU の分岐予測器',
    'The CPU cache(s)': 'CPU キャッシュ',
    'Side-channel attacks': 'サイドチャネル攻撃',
    'Side-channel mitigations in Windows': 'Windows のサイドチャネル緩和策',
    'KVA Shadow': 'KVA Shadow',
    'Hardware indirect branch controls (IBRS, IBPB, STIBP, SSBD)': 'ハードウェアによる間接分岐制御（IBRS、IBPB、STIBP、SSBD）',
    'Retpoline and import optimization': 'Retpoline とインポート最適化',
    'STIBP pairing': 'STIBP のペアリング',
    'Trap dispatching': 'トラップのディスパッチ',
    'Interrupt dispatching': '割り込みのディスパッチ',
    'Line-based versus message signaled–based interrupts': 'ライン割り込みとメッセージシグナル割り込み',
    'Timer processing': 'タイマー処理',
    'System worker threads': 'システムワーカースレッド',
    'Exception dispatching': '例外のディスパッチ',
    'System service handling': 'システムサービスの処理',
    'WoW64 (Windows-on-Windows)': 'WoW64（Windows-on-Windows）',
    'The WoW64 core': 'WoW64 の中核',
    'File system redirection': 'ファイルシステムのリダイレクト',
    'Registry redirection': 'レジストリのリダイレクト',
    'X86 simulation on AMD64 platforms': 'AMD64 プラットフォームでの x86 シミュレーション',
    'ARM': 'ARM',
    'Memory models': 'メモリモデル',
    'ARM32 simulation on ARM64 platforms': 'ARM64 プラットフォームでの ARM32 シミュレーション',
    'X86 simulation on ARM64 platforms': 'ARM64 プラットフォームでの x86 シミュレーション',
    'Object Manager': 'オブジェクトマネージャー',
    'Executive objects': 'エグゼクティブオブジェクト',
    'Object structure': 'オブジェクトの構造',
    'Synchronization': '同期',
    'High-IRQL synchronization': '高 IRQL での同期',
    'Low-IRQL synchronization': '低 IRQL での同期',
    'Advanced local procedure call': '高度なローカルプロシージャコール（ALPC）',
    'Connection model': '接続モデル',
    'Message model': 'メッセージモデル',
    'Asynchronous operation': '非同期操作',
    'Views, regions, and sections': 'ビュー、リージョン、セクション',
    'Attributes': '属性',
    'Blobs, handles, and resources': 'ブロブ、ハンドル、リソース',
    'Handle passing': 'ハンドルの受け渡し',
    'Performance': 'パフォーマンス',
    'Power management': '電源管理',
    'ALPC direct event attribute': 'ALPC のダイレクトイベント属性',
    'Debugging and tracing': 'デバッグとトレース',
    'Windows Notification Facility': 'Windows 通知機能（WNF）',
    'WNF features': 'WNF の機能',
    'WNF users': 'WNF の利用者',
    'WNF state names and storage': 'WNF の状態名と保存先',
    'WNF event aggregation': 'WNF イベントの集約',
    'User-mode debugging': 'ユーザーモードデバッグ',
    'Kernel support': 'カーネルのサポート',
    'Native support': 'ネイティブのサポート',
    'Windows subsystem support': 'Windows サブシステムのサポート',
    'Packaged applications': 'パッケージ化アプリケーション',
    'UWP applications': 'UWP アプリケーション',
    'Centennial applications': 'Centennial アプリケーション',
    'The Host Activity Manager': 'ホストアクティビティマネージャー（HAM）',
    'The State Repository': '状態リポジトリ',
    'The Dependency Mini Repository': '依存関係ミニリポジトリ',
    'Background tasks and the Broker Infrastructure': 'バックグラウンドタスクと Broker Infrastructure',
    'Packaged applications setup and startup': 'パッケージ化アプリケーションの設定と起動',
    'Package activation': 'パッケージのアクティブ化',
    'Package registration': 'パッケージの登録',
    'The Windows hypervisor': 'Windows ハイパーバイザー',
    'Partitions, processes, and threads': 'パーティション、プロセス、スレッド',
    'The hypervisor startup': 'ハイパーバイザーの起動',
    'The hypervisor memory manager': 'ハイパーバイザーのメモリ管理',
    'Hyper-V schedulers': 'Hyper-V スケジューラー',
    'Hypercalls and the hypervisor TLFS': 'ハイパーコールとハイパーバイザー TLFS',
    'Intercepts': 'インターセプト',
    'The synthetic interrupt controller (SynIC)': '合成割り込みコントローラー（SynIC）',
    'The Windows hypervisor platform API and EXO partitions': 'Windows ハイパーバイザープラットフォーム API と EXO パーティション',
    'Nested virtualization': '入れ子の仮想化',
    'The Windows hypervisor on ARM64': 'ARM64 上の Windows ハイパーバイザー',
    'The virtualization stack': '仮想化スタック',
    'Virtual machine manager service and worker processes': '仮想マシン管理サービスとワーカープロセス',
    'The VID driver and the virtualization stack memory manager': 'VID ドライバーと仮想化スタックのメモリ管理',
    'The birth of a Virtual Machine (VM)': '仮想マシン（VM）の生成',
    'VMBus': 'VMBus',
    'Virtual hardware support': '仮想ハードウェアのサポート',
    'VA-backed virtual machines': '仮想アドレスで支援される仮想マシン',
    'Virtualization-based security (VBS)': '仮想化ベースのセキュリティ（VBS）',
    'Virtual trust levels (VTLs) and Virtual Secure Mode (VSM)': '仮想トラストレベル（VTL）と Virtual Secure Mode（VSM）',
    'Services provided by the VSM and requirements': 'VSM が提供するサービスと要件',
    'The Secure Kernel': 'セキュアカーネル',
    'Virtual interrupts': '仮想割り込み',
    'Secure intercepts': 'セキュアインターセプト',
    'VSM system calls': 'VSM のシステムコール',
    'Secure threads and scheduling': 'セキュアスレッドとスケジューリング',
    'The Hypervisor Enforced Code Integrity': 'ハイパーバイザー強制コード整合性',
    'UEFI runtime virtualization': 'UEFI ランタイムの仮想化',
    'VSM startup': 'VSM の起動',
    'The Secure Kernel memory manager': 'Secure Kernel のメモリ管理',
    'Hot patching': 'ホットパッチ',
    'Isolated User Mode': '分離ユーザーモード',
    'Trustlets creation': 'トラストレットの作成',
    'Secure devices': 'セキュアデバイス',
    'VBS-based enclaves': 'VBS ベースのエンクレーブ',
    'System Guard runtime attestation': 'System Guard のランタイム証明',
    'Chapter 10 Management, diagnostics, and tracing': '第10章 管理、診断、トレース',
    'The registry': 'レジストリ',
    'Viewing and changing the registry': 'レジストリの表示と変更',
    'Registry usage': 'レジストリの用途',
    'Registry data types': 'レジストリのデータ型',
    'Registry logical structure': 'レジストリの論理構造',
    'Application hives': 'アプリケーションハイブ',
    'Transactional Registry (TxR)': 'トランザクションレジストリ（TxR）',
    'Monitoring registry activity': 'レジストリ操作の監視',
    'Process Monitor internals': 'Process Monitor の内部構造',
    'Registry internals': 'レジストリの内部構造',
    'Hive reorganization': 'ハイブの再編成',
    'The registry namespace and operation': 'レジストリの名前空間と操作',
    'Stable storage': '安定記憶域',
    'Registry filtering': 'レジストリのフィルタリング',
    'Registry virtualization': 'レジストリの仮想化',
    'Registry optimizations': 'レジストリの最適化',
    'Windows services': 'Windows サービス',
    'Service applications': 'サービスアプリケーション',
    'Service accounts': 'サービスアカウント',
    'The Service Control Manager (SCM)': 'サービスコントロールマネージャー（SCM）',
    'Service control programs': 'サービス制御プログラム',
    'Autostart services startup': '自動起動サービスの起動',
    'Delayed autostart services': '遅延自動起動サービス',
    'Triggered-start services': 'トリガー起動サービス',
    'Startup errors': '起動エラー',
    'Accepting the boot and last known good': '起動の受け入れと「前回正常起動時の構成」',
    'Service failures': 'サービス障害',
    'Service shutdown': 'サービスのシャットダウン',
    'Shared service processes': '共有サービスプロセス',
    'Service tags': 'サービスタグ',
    'User services': 'ユーザーサービス',
    'Packaged services': 'パッケージ化サービス',
    'Protected services': '保護サービス',
    'Task scheduling and UBPM': 'タスクスケジューリングと UBPM',
    'The Task Scheduler': 'タスクスケジューラ',
    'Unified Background Process Manager (UBPM)': '統合バックグラウンドプロセスマネージャー（UBPM）',
    'Task Scheduler COM interfaces': 'タスクスケジューラの COM インターフェイス',
    'Windows Management Instrumentation': 'Windows 管理基盤（WMI）',
    'WMI architecture': 'WMI アーキテクチャ',
    'WMI providers': 'WMI プロバイダー',
    'The Common Information Model and the Managed Object Format Language': 'Common Information Model と Managed Object Format Language',
    'Class association': 'クラスの関連付け',
    'WMI implementation': 'WMI の実装',
    'WMI security': 'WMI のセキュリティ',
    'Event Tracing for Windows (ETW)': 'Windows イベントトレース（ETW）',
    'ETW initialization': 'ETW の初期化',
    'ETW sessions': 'ETW セッション',
    'ETW providers': 'ETW プロバイダー',
    'Providing events': 'イベントの提供',
    'ETW Logger thread': 'ETW ロガースレッド',
    'Consuming events': 'イベントの受信',
    'System loggers': 'システムロガー',
    'ETW security': 'ETW のセキュリティ',
    'Dynamic tracing (DTrace)': '動的トレース（DTrace）',
    'Internal architecture': '内部アーキテクチャ',
    'DTrace type library': 'DTrace 型ライブラリ',
    'Windows Error Reporting (WER)': 'Windows エラー報告（WER）',
    'User applications crashes': 'ユーザーアプリケーションのクラッシュ',
    'Kernel-mode (system) crashes': 'カーネルモード（システム）のクラッシュ',
    'Process hang detection': 'プロセスのハング検出',
    'Global flags': 'グローバルフラグ',
    'Kernel shims': 'カーネルシム',
    'Shim engine initialization': 'シムエンジンの初期化',
    'The shim database': 'シムデータベース',
    'Driver shims': 'ドライバーシム',
    'Device shims': 'デバイスシム',
    'Chapter 11 Caching and file systems': '第11章 キャッシュとファイルシステム',
    'Terminology': '用語',
    'Key features of the cache manager': 'キャッシュマネージャーの主な機能',
    'Single, centralized system cache': '単一の集中型システムキャッシュ',
    'The memory manager': 'メモリマネージャー',
    'Cache coherency': 'キャッシュの一貫性',
    'Virtual block caching': '仮想ブロックキャッシュ',
    'Stream-based caching': 'ストリームベースのキャッシュ',
    'Recoverable file system support': '回復可能なファイルシステムのサポート',
    'NTFS MFT working set enhancements': 'NTFS MFT ワーキングセットの拡張',
    'Memory partitions support': 'メモリパーティションのサポート',
    'Cache virtual memory management': 'キャッシュの仮想メモリ管理',
    'Cache size': 'キャッシュサイズ',
    'Cache virtual size': 'キャッシュの仮想サイズ',
    'Cache working set size': 'キャッシュのワーキングセットサイズ',
    'Cache physical size': 'キャッシュの物理サイズ',
    'Cache data structures': 'キャッシュのデータ構造',
    'Systemwide cache data structures': 'システム全体のキャッシュデータ構造',
    'Per-file cache data structures': 'ファイルごとのキャッシュデータ構造',
    'File system interfaces': 'ファイルシステムのインターフェイス',
    'Copying to and from the cache': 'キャッシュとの間のコピー',
    'Caching with the mapping and pinning interfaces': 'マッピング／ピン留めインターフェイスによるキャッシュ',
    'Caching with the direct memory access interfaces': 'ダイレクトメモリアクセスインターフェイスによるキャッシュ',
    'Fast I/O': '高速 I/O',
    'Read-ahead and write-behind': '先読みと遅延書き込み',
    'Intelligent read-ahead': 'インテリジェントな先読み',
    'Read-ahead enhancements': '先読みの拡張',
    'Write-back caching and lazy writing': 'ライトバックキャッシュと遅延書き込み',
    'Disabling lazy writing for a file': 'ファイルの遅延書き込みを無効化する',
    'Forcing the cache to write through to disk': 'キャッシュをディスクへライトスルーさせる',
    'Flushing mapped files': 'マップトファイルのフラッシュ',
    'Write throttling': '書き込みスロットリング',
    'System threads': 'システムスレッド',
    'Aggressive write behind and low-priority lazy writes': '積極的な遅延書き込みと低優先度の遅延書き込み',
    'Dynamic memory': '動的メモリ',
    'Cache manager disk I/O accounting': 'キャッシュマネージャーのディスク I/O 計測',
    'File systems': 'ファイルシステム',
    'Windows file system formats': 'Windows のファイルシステム形式',
    'CDFS': 'CDFS',
    'UDF': 'UDF',
    'FAT12, FAT16, and FAT32': 'FAT12、FAT16、FAT32',
    'exFAT': 'exFAT',
    'NTFS': 'NTFS',
    'ReFS': 'ReFS',
    'File system driver architecture': 'ファイルシステムドライバーのアーキテクチャ',
    'Local FSDs': 'ローカル FSD',
    'Remote FSDs': 'リモート FSD',
    'File system operations': 'ファイルシステム操作',
    'Explicit file I/O': '明示的なファイル I/O',
    'Memory manager’s modified and mapped page writer': 'メモリマネージャーの変更済み／マップトページライター',
    'Cache manager’s lazy writer': 'キャッシュマネージャーの遅延書き込みスレッド',
    'Cache manager’s read-ahead thread': 'キャッシュマネージャーの先読みスレッド',
    'Memory manager’s page fault handler': 'メモリマネージャーのページフォルトハンドラー',
    'File system filter drivers and minifilters': 'ファイルシステムフィルタードライバーとミニフィルター',
    'Filtering named pipes and mailslots': '名前付きパイプとメールスロットのフィルタリング',
    'Controlling reparse point behavior': '再解析ポイントの動作制御',
    'Process Monitor': 'Process Monitor',
    'The NT File System (NTFS)': 'NT ファイルシステム（NTFS）',
    'High-end file system requirements': '高性能ファイルシステムの要件',
    'Recoverability': '回復性',
    'Data redundancy and fault tolerance': 'データ冗長性とフォールトトレランス',
    'Advanced features of NTFS': 'NTFS の高度な機能',
    'Multiple data streams': '複数データストリーム',
    'Unicode-based names': 'Unicode ベースの名前',
    'General indexing facility': '汎用インデックス機能',
    'Dynamic bad-cluster remapping': '不良クラスターの動的再マッピング',
    'Hard links': 'ハードリンク',
    'Symbolic (soft) links and junctions': 'シンボリックリンク（ソフトリンク）とジャンクション',
    'Compression and sparse files': '圧縮とスパースファイル',
    'Change logging': '変更ログ',
    'Per-user volume quotas': 'ユーザーごとのボリュームクォータ',
    'Link tracking': 'リンク追跡',
    'Encryption': '暗号化',
    'POSIX-style delete semantics': 'POSIX 形式の削除セマンティクス',
    'Defragmentation': 'デフラグメンテーション',
    'Dynamic partitioning': '動的パーティショニング',
    'NTFS support for tiered volumes': '階層化ボリュームに対する NTFS のサポート',
    'NTFS file system driver': 'NTFS ファイルシステムドライバー',
    'NTFS on-disk structure': 'NTFS のディスク上構造',
    'Volumes': 'ボリューム',
    'Clusters': 'クラスター',
    'Master file table': 'マスターファイルテーブル（MFT）',
    'File record numbers': 'ファイルレコード番号',
    'File records': 'ファイルレコード',
    'File names': 'ファイル名',
    'Tunneling': 'トンネリング',
    'Resident and nonresident attributes': '常駐属性と非常駐属性',
    'Data compression and sparse files': 'データ圧縮とスパースファイル',
    'Compressing sparse data': 'スパースデータの圧縮',
    'Compressing nonsparse data': '非スパースデータの圧縮',
    'Sparse files': 'スパースファイル',
    'The change journal file': '変更ジャーナルファイル',
    'Indexing': 'インデックス作成',
    'Object IDs': 'オブジェクトID',
    'Quota tracking': 'クォータ追跡',
    'Consolidated security': '統合セキュリティ',
    'Reparse points': '再解析ポイント',
    'Storage reserves and NTFS reservations': 'ストレージ予約領域と NTFS 予約',
    'Transaction support': 'トランザクションのサポート',
    'Isolation': '分離',
    'Transactional APIs': 'トランザクション API',
    'On-disk implementation': 'ディスク上の実装',
    'Logging implementation': 'ログ記録の実装',
    'NTFS recovery support': 'NTFS の回復機能',
    'Design': '設計',
    'Metadata logging': 'メタデータのログ記録',
    'Log file service': 'ログファイルサービス',
    'Log record types': 'ログレコードの種類',
    'Recovery': '回復',
    'Analysis pass': '解析パス',
    'Redo pass': '再実行パス',
    'Undo pass': '取り消しパス',
    'NTFS bad-cluster recovery': 'NTFS の不良クラスター回復',
    'Self-healing': '自己修復',
    'Online check-disk and fast repair': 'オンラインディスクチェックと高速修復',
    'Encrypted file system': '暗号化ファイルシステム',
    'Encrypting a file for the first time': 'ファイルの初回暗号化',
    'The decryption process': '復号処理',
    'Backing up encrypted files': '暗号化ファイルのバックアップ',
    'Copying encrypted files': '暗号化ファイルのコピー',
    'BitLocker encryption offload': 'BitLocker 暗号化のオフロード',
    'Online encryption support': 'オンライン暗号化のサポート',
    'Direct Access (DAX) disks': 'ダイレクトアクセス（DAX）ディスク',
    'DAX driver model': 'DAX ドライバーモデル',
    'DAX volumes': 'DAX ボリューム',
    'Cached and noncached I/O in DAX volumes': 'DAX ボリュームでのキャッシュ I/O と非キャッシュ I/O',
    'Mapping of executable images': '実行イメージのマッピング',
    'Block volumes': 'ブロックボリューム',
    'File system filter drivers and DAX': 'ファイルシステムフィルタードライバーと DAX',
    'Flushing DAX mode I/Os': 'DAX モード I/O のフラッシュ',
    'Large and huge pages support': 'ラージページとヒュージページのサポート',
    'Virtual PM disks and storages spaces support': '仮想PMディスクと記憶域スペースのサポート',
    'Resilient File System (ReFS)': '回復性ファイルシステム（ReFS）',
    'Minstore architecture': 'Minstore アーキテクチャ',
    'B+ tree physical layout': 'B+ ツリーの物理レイアウト',
    'Allocators': 'アロケーター',
    'Page table': 'ページテーブル',
    'Minstore I/O': 'Minstore の I/O',
    'ReFS architecture': 'ReFS アーキテクチャ',
    'ReFS on-disk structure': 'ReFS のディスク上構造',
    'Security and change journal': 'セキュリティと変更ジャーナル',
    'ReFS advanced features': 'ReFS の高度な機能',
    'File’s block cloning (snapshot support) and sparse VDL': 'ファイルのブロッククローン（スナップショット対応）とスパース VDL',
    'ReFS write-through': 'ReFS のライトスルー',
    'ReFS recovery support': 'ReFS の回復機能',
    'Leak detection': 'リーク検出',
    'Shingled magnetic recording (SMR) volumes': '瓦磁気記録（SMR）ボリューム',
    'ReFS support for tiered volumes and SMR': '階層化ボリュームと SMR に対する ReFS のサポート',
    'Container compaction': 'コンテナーの圧縮',
    'Compression and ghosting': '圧縮とゴースト化',
    'Storage Spaces': '記憶域スペース',
    'Spaces internal architecture': '記憶域スペースの内部アーキテクチャ',
    'Services provided by Spaces': '記憶域スペースが提供するサービス',
    'Chapter 12 Startup and shutdown': '第12章 起動とシャットダウン',
    'Boot process': '起動プロセス',
    'The UEFI boot': 'UEFI 起動',
    'The BIOS boot process': 'BIOS 起動プロセス',
    'Secure Boot': 'セキュアブート',
    'The Windows Boot Manager': 'Windows ブートマネージャー',
    'The Boot menu': 'ブートメニュー',
    'Launching a boot application': 'ブートアプリケーションの起動',
    'Measured Boot': 'Measured Boot（起動計測）',
    'Trusted execution': '信頼された実行環境',
    'The Windows OS Loader': 'Windows OS ローダー',
    'Booting from iSCSI': 'iSCSI からの起動',
    'The hypervisor loader': 'ハイパーバイザーローダー',
    'VSM startup policy': 'VSM 起動ポリシー',
    'The Secure Launch': 'セキュア起動',
    'Initializing the kernel and executive subsystems': 'カーネルとエグゼクティブサブシステムの初期化',
    'Kernel initialization phase 1': 'カーネル初期化フェーズ1',
    'Smss, Csrss, and Wininit': 'Smss、Csrss、Wininit',
    'ReadyBoot': 'ReadyBoot',
    'Images that start automatically': '自動起動するイメージ',
    'Shutdown': 'シャットダウン',
    'Hibernation and Fast Startup': '休止状態と高速スタートアップ',
    'Windows Recovery Environment (WinRE)': 'Windows 回復環境（WinRE）',
    'Safe mode': 'セーフモード',
    'Driver loading in safe mode': 'セーフモードでのドライバー読み込み',
    'Safe-mode-aware user programs': 'セーフモード対応ユーザープログラム',
    'Boot status file': '起動状態ファイル',
    'Contents of Windows Internals, Seventh Edition, Part 1': 'Windows Internals 第7版 第1部の内容',
    'Index': '索引',
    'X-Z': 'X〜Z',
    'Introduction to the memory manager': 'メモリマネージャーの概要',
    'Memory manager components': 'メモリマネージャーの構成要素',
    'Large and small pages': 'ラージページとスモールページ',
    'Examining memory usage': 'メモリ使用状況の調査',
    'Internal synchronization': '内部同期',
    'Services provided by the memory manager': 'メモリマネージャーが提供するサービス',
    'Page states and memory allocations': 'ページ状態とメモリ割り当て',
    'Commit charge and commit limit': 'コミット量とコミット上限',
    'Locking memory': 'メモリのロック',
    'Allocation granularity': '割り当て粒度',
    'Shared memory and mapped files': '共有メモリとマップトファイル',
    'Protecting memory': 'メモリ保護',
    'Data Execution Prevention': 'データ実行防止（DEP）',
    'Copy-on-write': 'コピーオンライト',
    'Address Windowing Extensions': 'アドレスウィンドウ拡張（AWE）',
    'Kernel-mode heaps (system memory pools)': 'カーネルモードヒープ（システムメモリプール）',
    'Pool sizes': 'プールサイズ',
    'Monitoring pool usage': 'プール使用状況の監視',
    'Look-aside lists': 'ルックアサイドリスト',
    'Heap manager': 'ヒープマネージャー',
    'Process heaps': 'プロセスヒープ',
    'Heap types': 'ヒープの種類',
    'The NT heap': 'NT ヒープ',
    'Heap synchronization': 'ヒープの同期',
    'The low-fragmentation heap': '低断片化ヒープ（LFH）',
    'The segment heap': 'セグメントヒープ',
    'Heap security features': 'ヒープのセキュリティ機能',
    'Heap debugging features': 'ヒープのデバッグ機能',
    'Pageheap': 'ページヒープ',
    'Fault-tolerant heap': 'フォールトトレラントヒープ',
    'Virtual address space layouts': '仮想アドレス空間のレイアウト',
    'x86 address space layouts': 'x86 のアドレス空間レイアウト',
    'x86 system address space layout': 'x86 システムアドレス空間のレイアウト',
    'x86 session space': 'x86 セッション空間',
    'System page table entries': 'システムページテーブルエントリ',
    'ARM address space layout': 'ARM のアドレス空間レイアウト',
    '64-bit address space layout': '64ビットのアドレス空間レイアウト',
    'x64 virtual addressing limitations': 'x64 仮想アドレスの制限',
    'Dynamic system virtual address space management': 'システム仮想アドレス空間の動的管理',
    'System virtual address space quotas': 'システム仮想アドレス空間のクォータ',
    'User address space layout': 'ユーザーアドレス空間のレイアウト',
    'Address translation': 'アドレス変換',
    'x86 virtual address translation': 'x86 仮想アドレス変換',
    'Translation look-aside buffer': 'トランスレーション・ルックアサイド・バッファー（TLB）',
    'x64 virtual address translation': 'x64 仮想アドレス変換',
    'ARM virtual address translation': 'ARM 仮想アドレス変換',
    'Page fault handling': 'ページフォルト処理',
    'Invalid PTEs': '無効な PTE',
    'Prototype PTEs': 'プロトタイプ PTE',
    'In-paging I/O': 'ページイン I/O',
    'Collided page faults': '競合するページフォルト',
    'Clustered page faults': 'クラスタ化ページフォルト',
    'Page files': 'ページファイル',
    'Commit charge and the system commit limit': 'コミット量とシステムのコミット上限',
    'Commit charge and page file size': 'コミット量とページファイルサイズ',
    'Stacks': 'スタック',
    'User stacks': 'ユーザースタック',
    'Kernel stacks': 'カーネルスタック',
    'DPC stack': 'DPC スタック',
    'Virtual address descriptors': '仮想アドレス記述子（VAD）',
    'Process VADs': 'プロセス VAD',
    'Rotate VADs': 'ローテート VAD',
    'NUMA': 'NUMA',
    'Section objects': 'セクションオブジェクト',
    'Working sets': 'ワーキングセット',
    'Demand paging': 'デマンドページング',
    'Logical prefetcher and ReadyBoot': '論理プリフェッチャーと ReadyBoot',
    'Placement policy': '配置ポリシー',
    'Working set management': 'ワーキングセット管理',
    'Balance set manager and swapper': 'バランスセットマネージャーとスワッパー',
    'System working sets': 'システムワーキングセット',
    'Memory notification events': 'メモリ通知イベント',
    'Page frame number database': 'ページフレーム番号（PFN）データベース',
    'Page list dynamics': 'ページリストの動作',
    'Page priority': 'ページ優先度',
    'Modified page writer and mapped page writer': '変更済みページライターとマップトページライター',
    'PFN data structures': 'PFN データ構造',
    'Page file reservation': 'ページファイルの予約',
    'Physical memory limits': '物理メモリの上限',
    'Windows client memory limits': 'Windows クライアントのメモリ上限',
    'Memory compression': 'メモリ圧縮',
    'Compression illustration': '圧縮の図解',
    'Compression architecture': '圧縮アーキテクチャ',
    'Memory partitions': 'メモリパーティション',
    'Memory combining': 'メモリ結合',
    'The search phase': '検索フェーズ',
    'The classification phase': '分類フェーズ',
    'The page combining phase': 'ページ結合フェーズ',
    'From private to shared PTE': 'プライベート PTE から共有 PTE へ',
    'Combined pages release': '結合ページの解放',
    'Memory enclaves': 'メモリエンクレーブ',
    'Programmatic interface': 'プログラム用インターフェイス',
    'Memory enclave initializations': 'メモリエンクレーブの初期化',
    'Enclave construction': 'エンクレーブの構築',
    'Loading data into an enclave': 'エンクレーブへのデータ読み込み',
    'Initializing an enclave': 'エンクレーブの初期化',
    'Proactive memory management (SuperFetch)': 'プロアクティブなメモリ管理（SuperFetch）',
    'Components': '構成要素',
    'Tracing and logging': 'トレースとログ記録',
    'Scenarios': 'シナリオ',
    'Page priority and rebalancing': 'ページ優先度と再バランス',
    'Robust performance': '安定したパフォーマンス',
    'ReadyBoost': 'ReadyBoost',
    'ReadyDrive': 'ReadyDrive',
    'Process reflection': 'プロセスリフレクション',
    'I/O system components': 'I/O システムの構成要素',
    'The I/O manager': 'I/O マネージャー',
    'Typical I/O processing': '一般的な I/O 処理',
    'Interrupt Request Levels and Deferred Procedure Calls': '割り込み要求レベルと遅延プロシージャコール',
    'Interrupt Request Levels': '割り込み要求レベル（IRQL）',
    'Deferred Procedure Calls': '遅延プロシージャコール（DPC）',
    'Types of device drivers': 'デバイスドライバーの種類',
    'Structure of a driver': 'ドライバーの構造',
    'Driver objects and device objects': 'ドライバーオブジェクトとデバイスオブジェクト',
    'Opening devices': 'デバイスを開く',
    'I/O processing': 'I/O 処理',
    'Types of I/O': 'I/O の種類',
    'I/O request packets': 'I/O 要求パケット（IRP）',
    'I/O request to a single-layered hardware-based driver': '単層ハードウェアドライバーへの I/O 要求',
    'I/O requests to layered drivers': '階層型ドライバーへの I/O 要求',
    'Thread-agnostic I/O': 'スレッドに依存しない I/O',
    'I/O cancellation': 'I/O のキャンセル',
    'I/O completion ports': 'I/O 完了ポート',
    'I/O prioritization': 'I/O の優先順位付け',
    'Container notifications': 'コンテナー通知',
    'Driver Verifier': 'Driver Verifier',
    'I/O-related verification options': 'I/O 関連の検証オプション',
    'Memory-related verification options': 'メモリ関連の検証オプション',
    'The Plug and Play manager': 'プラグアンドプレイマネージャー',
    'Level of Plug and Play support': 'プラグアンドプレイのサポートレベル',
    'Device enumeration': 'デバイス列挙',
    'Device stacks': 'デバイススタック',
    'Driver support for Plug and Play': 'プラグアンドプレイに対するドライバーのサポート',
    'Plug-and-play driver installation': 'プラグアンドプレイ対応ドライバーのインストール',
    'General driver loading and installation': 'ドライバーの一般的な読み込みとインストール',
    'Driver loading': 'ドライバーの読み込み',
    'Driver installation': 'ドライバーのインストール',
    'The Windows Driver Foundation': 'Windows ドライバーフレームワーク（WDF）',
    'Kernel-Mode Driver Framework': 'カーネルモードドライバーフレームワーク（KMDF）',
    'User-Mode Driver Framework': 'ユーザーモードドライバーフレームワーク（UMDF）',
    'The power manager': '電源マネージャー',
    'Connected Standby and Modern Standby': 'Connected Standby と Modern Standby',
    'Power manager operation': '電源マネージャーの動作',
    'Driver power operation': 'ドライバーの電源処理',
    'Driver and application control of device power': 'ドライバーとアプリケーションによるデバイス電源の制御',
    'Power management framework': '電源管理フレームワーク',
    'Power availability requests': '電源利用可能性の要求',
    'Security ratings': 'セキュリティ評価基準',
    'Trusted Computer System Evaluation Criteria': '信頼できるコンピューターシステム評価基準（TCSEC）',
    'The Common Criteria': 'Common Criteria（共通基準）',
    'Security system components': 'セキュリティシステムの構成要素',
    'Virtualization-based security': '仮想化ベースのセキュリティ（VBS）',
    'Credential Guard': 'Credential Guard',
    'Device Guard': 'Device Guard',
    'Protecting objects': 'オブジェクトの保護',
    'Access checks': 'アクセスチェック',
    'Security identifiers': 'セキュリティ識別子（SID）',
    'Virtual service accounts': '仮想サービスアカウント',
    'Security descriptors and access control': 'セキュリティ記述子とアクセス制御',
    'Dynamic Access Control': '動的アクセス制御（DAC）',
    'The AuthZ API': 'AuthZ API',
    'Conditional ACEs': '条件付き ACE',
    'Account rights and privileges': 'アカウント権利と特権',
    'Account rights': 'アカウント権利',
    'Privileges': '特権',
    'Super privileges': '特別な特権',
    'Access tokens of processes and threads': 'プロセスとスレッドのアクセストークン',
    'Security auditing': 'セキュリティ監査',
    'Object access auditing': 'オブジェクトアクセス監査',
    'Global audit policy': 'グローバル監査ポリシー',
    'Advanced Audit Policy settings': '詳細監査ポリシーの設定',
    'AppContainers': 'AppContainer',
    'Overview of UWP apps': 'UWP アプリの概要',
    'The AppContainer': 'AppContainer',
    'Logon': 'ログオン',
    'Winlogon initialization': 'Winlogon の初期化',
    'User logon steps': 'ユーザーログオンの手順',
    'Assured authentication': '保証された認証',
    'Windows Biometric Framework': 'Windows 生体認証フレームワーク',
    'Windows Hello': 'Windows Hello',
    'User Account Control and virtualization': 'ユーザーアカウント制御（UAC）と仮想化',
    'File system and registry virtualization': 'ファイルシステムとレジストリの仮想化',
    'Elevation': '昇格',
    'Exploit mitigations': 'エクスプロイト緩和策',
    'Process-mitigation policies': 'プロセス緩和ポリシー',
    'Control Flow Integrity': '制御フロー整合性（CFI）',
    'Security assertions': 'セキュリティアサーション',
    'Application Identification': 'アプリケーション識別',
    'AppLocker': 'AppLocker',
    'Software Restriction Policies': 'ソフトウェア制限ポリシー',
    'Kernel Patch Protection': 'カーネルパッチ保護',
    'PatchGuard': 'PatchGuard',
    'HyperGuard': 'HyperGuard',
}

# Some source TOC labels already include their English acronym in parentheses.
# Translate those exact display strings as well as the bare chapter titles above.
chapter_trans.update({
    'Trusted Computer System Evaluation Criteria（TCSEC）': '信頼できるコンピューターシステム評価基準（TCSEC）',
    'Windows Driver Foundation（WDF）': 'Windows ドライバーフレームワーク（WDF）',
    'Kernel-Mode Driver Framework（KMDF）': 'カーネルモードドライバーフレームワーク（KMDF）',
    'User-Mode Driver Framework（UMDF）': 'ユーザーモードドライバーフレームワーク（UMDF）',
    'Windows Notification Facility（WNF）': 'Windows 通知機能（WNF）',
    'Windows Biometric Framework': 'Windows 生体認証フレームワーク',
    'Hypervisor-Enforced Code Integrity': 'ハイパーバイザー強制コード整合性',
    'Windows Management Instrumentation（WMI）': 'Windows 管理基盤（WMI）',
    'Event Tracing for Windows（ETW）': 'Windows イベントトレース（ETW）',
    'Windows Error Reporting（WER）': 'Windows エラー報告（WER）',
    'Resilient File System（ReFS）': '回復性ファイルシステム（ReFS）',
    'Minstore I/O': 'Minstore の I/O',
})

unified_aside = ''

# 3. Reader Header Bar
unified_header = """<header>
<button id="tocToggle" aria-label="目次を開閉">☰ 目次</button>
<label id="sizeLabel" style="margin-left:auto">文字 <button id="smaller" aria-label="文字を小さく">−</button> <button id="larger" aria-label="文字を大きく">＋</button></label>
</header>"""

# 4. Intro block
unified_intro = """<div class="intro">
<div style="margin-top:10px;padding:8px 12px;background:var(--panel);border-radius:4px;font-size:14px;">
<strong>翻訳作業中：</strong> 日本語の箇所には章の要約も含まれます。日本語の本文がないページは英語原文を表示します。
</div>
</div>"""

# Pages to omit:
# Part 1: page-1 (Cover), page-2 (Title Page), page-3 (Copyright), page-4..page-11 (Contents)
p1_omit = {f"page-{i}" for i in range(1, 12)} | {"page-117", "page-209"}

# Part 2: p2-page-1 (Cover), p2-page-2 (Title), p2-page-3 (Copyright), p2-page-4..p2-page-18 (Contents at a Glance / Contents)
p2_omit = {f"p2-page-{i}" for i in range(1, 19)}

# The added page summaries preserve the complete source in a collapsed disclosure.
preserve_source_pages = {f"page-{i}" for i in range(788, 802)}
preserve_source_pages |= {f"p2-page-{i}" for i in range(236, 275)}
preserve_source_pages |= {f"p2-page-{i}" for i in (284, 285, 292, 293, 335)}
preserve_source_pages |= {f"p2-page-{i}" for i in range(808, 913)}

def render_plain_translation(text):
    if re.search(r"<(?:p|h[1-6]|ul|ol|table|pre|div|details)\b", text, re.I):
        return text
    out = []
    list_tag = None
    paragraph = []
    def flush_paragraph():
        if paragraph:
            out.append("<p>" + " ".join(paragraph) + "</p>")
            paragraph.clear()
    def close_list():
        nonlocal list_tag
        if list_tag:
            out.append(f"</{list_tag}>")
            list_tag = None
    for line in text.splitlines():
        line = line.strip()
        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        bullet = re.match(r"^[-*]\s+(.*)$", line)
        number = re.match(r"^\d+[.)]\s+(.*)$", line)
        if not line:
            flush_paragraph(); close_list(); continue
        if heading:
            flush_paragraph(); close_list(); level = len(heading.group(1))
            out.append(f"<h{level}>{heading.group(2)}</h{level}>"); continue
        item = bullet or number
        if item:
            flush_paragraph(); wanted = "ul" if bullet else "ol"
            if list_tag != wanted:
                close_list(); out.append(f"<{wanted}>"); list_tag = wanted
            out.append(f"<li>{item.group(1)}</li>"); continue
        close_list(); paragraph.append(line)
    flush_paragraph(); close_list()
    return "\n".join(out)

# 5–6. Use the original text whenever a translation is missing or empty.
original_pre_marker = '<!-- original-pre -->'
reader_controls = re.compile(r'<details>.*?</details>|<div class="pagebar">.*?</div>', re.DOTALL)


def render_pages(html, omit, prefix=''):
    pages = re.findall(r'<section class="page" id="(page-\d+)"[^>]*>(.*?)</section>', html, re.DOTALL)
    for source_id, content in pages:
        pid = prefix + source_id
        if pid in omit:
            continue
        body = translated_dict.get(pid, '').strip()
        lang = ''
        if original_pre_marker in body:
            blocks = re.findall(r'<pre>.*?</pre>', reader_controls.sub('', content), flags=re.DOTALL)
            if body.count(original_pre_marker) != len(blocks):
                raise ValueError(f'{pid}: original-pre marker count does not match the source')
            original_blocks = iter(blocks)
            body = re.sub(original_pre_marker, lambda _: next(original_blocks), body)
        elif not body:
            body = reader_controls.sub('', content).strip()
            lang = ' lang="en"'
        if body:
            if lang == '':
                body = render_plain_translation(body)
            if pid in preserve_source_pages:
                source = reader_controls.sub('', content).strip()
                source = re.sub(r'<h([1-6])([^>]*)>(.*?)</h\1>', r'<p><strong>\3</strong></p>', source, flags=re.DOTALL)
                body += '<details class="source-english"><summary>原文（英語）</summary>' + source + '</details>'
            yield f'<section class="page" id="{pid}" aria-label="{pid}"{lang}>{body}</section>'
        else:
            # Keep the URL target for a blank source page, but don't render a page border.
            yield f'<div id="{pid}" aria-hidden="true"></div>'


body_sections = [*render_pages(p1_html, p1_omit), *render_pages(p2_html, p2_omit, prefix='p2-')]

# Give headings semantic, readable anchors and derive the sidebar from those
# same headings, so its labels and destinations cannot drift apart.
toc_entries = []
used_heading_ids = set()
for index, section in enumerate(body_sections):
    section_match = re.match(r'<section class="page" id="([^"]+)"[^>]*>(.*?)</section>', section, re.DOTALL)
    if not section_match:
        continue
    section_id, content = section_match.groups()

    def add_heading_id(match):
        level, attrs, title_html = match.groups()
        title = html_module.unescape(re.sub(r'<[^>]+>', '', title_html)).strip()
        title = chapter_trans.get(title, title)
        slug = re.sub(r'[^\w\-]+', '-', title, flags=re.UNICODE).strip('-')[:72] or f'section-{index}'
        anchor = slug
        suffix = 2
        while anchor in used_heading_ids:
            anchor = f'{slug}-{suffix}'
            suffix += 1
        used_heading_ids.add(anchor)
        toc_entries.append((int(level), anchor, title))
        rendered_title = html_module.escape(title) if title != html_module.unescape(re.sub(r'<[^>]+>', '', title_html)).strip() else title_html
        return f'<h{level}{attrs} id="{anchor}">{rendered_title}</h{level}>'

    content = re.sub(r'<h([2-6])([^>]*)>(.*?)</h\1>', add_heading_id, content, flags=re.DOTALL)
    content = re.sub(r'(<table\b.*?</table>)', r'<div class="table-scroll" role="region" tabindex="0" aria-label="表。横にスクロールできます">\1</div>', content, flags=re.DOTALL)
    body_sections[index] = f'<section class="page" id="{section_id}" aria-label="{section_id}">{content}</section>'

toc_links = []
group_title = None
group_anchor = None
group_children = []
def flush_toc_group():
    if group_title is None:
        return
    child_markup = ''.join(group_children)
    toc_links.append(f'<details class="toc-group" data-toc-group><summary><a href="#{html_module.escape(group_anchor, quote=True)}">{html_module.escape(group_title)}</a></summary><template>{child_markup}</template></details>')
for level, anchor, title in toc_entries:
    escaped_anchor = html_module.escape(anchor, quote=True)
    escaped_title = html_module.escape(title)
    if level == 2:
        flush_toc_group()
        group_title, group_anchor, group_children = title, anchor, []
    elif group_title is not None:
        indent = min(max(level - 2, 0), 4)
        group_children.append(f'<a class="toc-level-{indent}" href="#{escaped_anchor}">{escaped_title}</a>')
    else:
        toc_links.append(f'<details class="toc-group"><summary><a href="#{escaped_anchor}">{escaped_title}</a></summary></details>')
flush_toc_group()
unified_aside = '<aside aria-label="目次"><h2>目次</h2>' + ''.join(toc_links) + '</aside>'

# Tables stay within the viewport; readers can scroll wide tables independently.
head_html = head_html.replace('</style>', '''
.table-scroll{max-width:100%;overflow-x:auto;overscroll-behavior-inline:contain;margin:1.25em 0;border:1px solid var(--line);border-radius:5px;-webkit-overflow-scrolling:touch}
.table-scroll table{width:max-content;min-width:100%;border-collapse:collapse;margin:0}
.table-scroll th,.table-scroll td{padding:7px 10px;border:1px solid var(--line);vertical-align:top}
.table-scroll th{background:var(--panel)}
.toc-group{margin:0;border-bottom:1px solid var(--line)}.toc-group summary{list-style:none;cursor:pointer}.toc-group summary::-webkit-details-marker{display:none}.toc-group summary>a{display:block}.toc-group>div{padding-left:12px}
.source-english{margin-top:1em;border-top:1px solid var(--line);padding-top:.5em}.source-english>summary{cursor:pointer;color:var(--muted)}.source-english h1,.source-english h2,.source-english h3,.source-english h4,.source-english h5,.source-english h6{font-size:1em;margin:.75em 0}.toc-level-1{padding-left:14px!important}.toc-level-2{padding-left:28px!important}.toc-level-3{padding-left:42px!important}.toc-level-4{padding-left:56px!important}
@media(max-width:900px){.table-scroll{max-width:calc(100vw - 40px)}.page{min-width:0}main{min-width:0;overflow-x:hidden}}
</style>''')

# 7. Footer & Script
script_and_footer = """<footer>
Windows Internals 第7版 Web Reader (日本語統合版)<br>
書籍の著作権は各権利者（Pavel Yosifovich, Alex Ionescu, Mark E. Russinovich, David A. Solomon, Microsoft Press）に帰属します。
</footer>
</main>
<script>
document.querySelectorAll('details').forEach(d=>d.addEventListener('toggle',()=>{if(d.open){const i=d.querySelector('img');if(i.dataset.src){i.src=i.dataset.src;delete i.dataset.src}}}));
document.getElementById('tocToggle').onclick=()=>{if(innerWidth<=900)document.body.classList.toggle('mobile-toc');else document.body.classList.toggle('toc-hidden')};
document.querySelector('aside').addEventListener('click',e=>{if(e.target.closest('a'))document.body.classList.remove('mobile-toc')});
document.querySelectorAll('aside details[data-toc-group]').forEach(d=>d.addEventListener('toggle',()=>{if(d.open&&!d.dataset.loaded){d.append(d.querySelector('template').content.cloneNode(true));d.querySelector('template').remove();d.dataset.loaded='true'}}));
document.querySelectorAll('table').forEach(t=>{if(!t.closest('.table-scroll')){const w=document.createElement('div');w.className='table-scroll';w.setAttribute('role','region');w.setAttribute('tabindex','0');w.setAttribute('aria-label','表。横にスクロールできます');t.replaceWith(w);w.append(t)}});
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
