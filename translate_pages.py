# Translation definitions for Front matter and Chapter 1
pages_ja = {}
pages_ja['page-1'] = """<figure><img loading="lazy" width="904" height="1102" src="assets/85b3906b3df76f4d3e3d5dc1.webp" alt="表紙画像"><figcaption>Windows Internals 第7版</figcaption></figure>"""

pages_ja['page-2'] = """<h2>Windows Internals 第7版</h2>
<h2>Part 1: システムアーキテクチャ、プロセス、スレッド、メモリ管理、他</h2>
<h3>Pavel Yosifovich, Alex Ionescu, Mark E. Russinovich, David A. Solomon 著</h3>"""

pages_ja['page-3'] = """<p><strong>発行：</strong> Microsoft Press（Microsoft Corporation）<br>
One Microsoft Way, Redmond, Washington 98052-6399</p>
<p>Copyright © 2017 by Pavel Yosifovich, Alex Ionescu, Mark E. Russinovich and David A. Solomon</p>
<p>本書の著作権は著者に帰属します。発行者の書面による事前の許可なく、本書のいかなる部分も電子的・機械的手段を問わず転載・複製・配信することを禁じます。</p>
<p>ISBN: 978-0-7356-8418-8</p>
<hr style="border:none;border-top:1px solid var(--line);margin:2em 0;">
<p><em>「多大なる忍耐と励ましでこの過酷な執筆を支えてくれた妻のIdit、そして子供たちのDanielle、Amit、Yoavへ感謝を込めて。」</em><br>—— Pavel Yosifovich</p>
<p><em>「夢を追う私を導き鼓舞してくれた両親、そして幾多の夜を共に耐えてくれた家族へ。」</em><br>—— Alex Ionescu</p>
<p><em>「夢を追い続ける勇気を与えてくれた私たちの両親へ。」</em><br>—— Mark E. Russinovich & David A. Solomon</p>"""

pages_ja['page-12'] = """<h2>はじめに</h2>
<p>『Windows Internals 第7版』は、Microsoft Windows 10 および Windows Server 2016 オペレーティングシステムのコアコンポーネントが内部でどのように動作しているかを深く理解したいと願う、上級開発者・セキュリティ研究者・システム管理者を対象としています。</p>
<p>この知識を身につけることで、開発者はWindowsプラットフォーム向けの設計判断の意図を正確に把握し、複雑な不具合を迅速にデバッグできるようになります。また、OSが「ボンネットの下（内部）」でどう動いているかを知ることは、システム管理者にとっても性能特性の把握やトラブルシューティングの強力な武器となります。さらにセキュリティ研究者にとっては、ソフトウェアやOSが悪用・誤用されるメカニズムを解明し、現代のWindowsが提供する各種防御機構やセキュリティ機能を正しく評価するための基盤となります。</p>

<h3>本書の歴史</h3>
<p>本書の初版は、Windows NT 3.1 のリリース直前に Helen Custer が執筆した『Inside Windows NT』（Microsoft Press、1992年）に遡ります。これはWindows NTに関して世界で最初に出版された書籍であり、そのアーキテクチャと設計思想に貴重な洞察を与えました。</p>
<p>第2版（1998年）は David Solomon によって執筆され、Windows NT 4.0 を対象に技術的深度が大幅に増強されました。第3版『Inside Windows 2000』（2000年）からは Mark Russinovich が共著として加わり、起動・停止の仕組み、サービス、レジストリ、ファイルシステムドライバ、ネットワーク、Plug and Play、電源管理、WMI、ジョブオブジェクト、ターミナルサービスなど、膨大な新機能の内部構造が網羅されました。</p>
<p>第4版（2004年）は Windows XP / Windows Server 2003 に対応し、Sysinternalsツールの活用法やクラッシュダンプの解析手法が拡充されました。第5版（2009年、Windows Vista / Server 2008対応）からは Alex Ionescu が共著者に加わり、イメージローダー、ユーザーモードデバッグ、ALPC、Hyper-Vなどの解説が追加されました。続く第6版（2012年）では、Windows 7 / Windows Server 2008 R2 で導入されたカーネルの刷新と、最新ツール群を用いた実践的な実験が大幅にアップデートされました。</p>"""

pages_ja['page-13'] = """<h3>第7版における主な変更点</h3>
<p>前版（第6版）の刊行以降、Windowsは度重なるバージョンアップを経て Windows 10 および Windows Server 2016 へと到達しました。Windows 10 は以降の継続的プラットフォームと位置づけられ、製造工程向けリリース（RTM）後も定期的に新バージョン（例: 2017年3月完成版を示す「バージョン1703」など）がリリースされています。これは、Windows 7 の時代から数えて実質6世代以上の進化を遂げたことを意味します。</p>
<p>また、Windows 8 以降、マイクロソフトはOSの「コア統合（Convergence）」を強力に推進してきました。Windows 8 と Windows Phone 8 でカーネルが共通化され、Windows 8.1 世代でアプリプラットフォームが統合、そして Windows 10 において、デスクトップ/ノートPC、サーバー、Xbox One、スマートフォン（Windows 10 Mobile）、HoloLens、IoT機器に至るまで、すべてのフォームファクタが単一の「OneCore」上で稼働するという壮大な統合が結実しました。</p>
<p>この大統合の完了により、カーネルアーキテクチャは極めて強固で安定したものとなりました。まさに本書が過去半世紀近くの変更を一挙にまとめ直す最適な時期となったのです。第7版では、Windows 8 から Windows 10 バージョン 1703 までの内部進化を網羅しており、新たに Pavel Yosifovich を共著者として迎え入れています。</p>

<h3>実践的な実験（EXPERIMENT）</h3>
<p>Windowsのソースコードを直接閲覧できなくても、カーネルデバッガーや Sysinternals ツール、そして本書のために作成された専用ユーティリティを駆使することで、OS内部の挙動を余すところなく観察できます。</p>
<p>本書には、読者自身の手でOSの内部挙動を確かめられるステップ・バイ・ステップの「実験（EXPERIMENT）」セクションが随所に用意されています。ただ文章を読むだけでなく、実際のツールの画面でカーネルの動きを目の当たりにすることで、Windowsの動作原理への理解がはるかに確固たるものになるはずです。ぜひ実際に手を動かしながら読み進めてみてください。</p>"""

pages_ja['page-14'] = """<h3>本書で扱わないトピック</h3>
<p>Windowsは極めて巨大かつ多機能なオペレーティングシステムです。本書はWindowsの「基盤となるシステムコンポーネント」に焦点を絞っており、すべての関連技術を網羅しているわけではありません。例えば、分散オブジェクト基盤である COM+ や、マネージドコード環境の基礎である Microsoft .NET Framework の詳細などは対象外です。また、本書はあくまで「OS内部構造（Internals）」の解説書であり、一般的なエンドユーザー向け操作ガイドや、アプリケーションプログラミング入門、システム管理手順書ではないため、それら基本操作の解説は割愛しています。</p>

<h3>免責事項と注意点</h3>
<p>本書で解説する内部構造・データ構造・未公開APIなどの挙動は、将来のWindowsのバージョンやアップデートによって予告なく変更される可能性があります。</p>
<p>「変更される可能性がある」というのは、必ず変わるという意味ではありませんが、不変である保証はどこにもありません。ドキュメント化されていない未公開インターフェースやOSの内部仕様に依存したアプリケーションは、将来のWindowsで正常に動作しなくなる危険があります。とりわけ、カーネルモードで動作するドライバが未公開の内部構造に直接アクセスしている場合、OSの更新によってブルースクリーン（BSoD）やシステムクラッシュを引き起こし、重大なデータ損失を招く恐れがあります。製品開発においては、必ず公式に公開・サポートされているAPIをご使用ください。</p>"""

pages_ja['page-15'] = """<h3>本書の構成</h3>
<p>本書は前版と同様に Part 1 と Part 2 の2分冊で構成されています。このリーダーでは両パートをシームレスに通読できます。</p>
<ul>
  <li><strong>第1章 概念とツール（Concepts and tools）</strong>：Windows内部構造を理解するための必須の用語・基本概念、および本書全体で使用する主要な調査ツールを紹介します。</li>
  <li><strong>第2章 システムアーキテクチャ（System architecture）</strong>：Windowsを構成する主要コンポーネントとその全体構造について掘り下げて解説します。</li>
  <li><strong>第3章 プロセスとジョブ（Processes and jobs）</strong>：Windowsにおけるプロセスの実装メカニズムや操作方法、プロセス群を統括制御するジョブオブジェクト（コンテナ基盤）を詳解します。</li>
  <li><strong>第4章 スレッド（Threads）</strong>：スレッドの生成・スケジューリング・コンテキストスイッチの仕組みを詳細に解説します。</li>
  <li><strong>第5章 メモリ管理（Memory management）</strong>：メモリマネージャーが物理メモリと仮想アドレス空間をどのように管理・マッピングしているかを解き明かします。</li>
  <li><strong>第6章 I/O システム（I/O system）</strong>：デバイスドライバと連携して各種ハードウェア周辺機器と通信を行うI/O機構の全体像を解説します。</li>
  <li><strong>第7章 セキュリティ（Security）</strong>：現代のWindowsに組み込まれた強固なアクセス制御機構や脆弱性攻撃緩和策（エクスプロイト対策）を詳解します。</li>
  <li><strong>Part 2（第8章〜第12章）</strong>：システムメカニズム（トラップ・ALPC・WMI等）、仮想化技術（Hyper-V・VBS・コンテナ）、管理・診断・トレース、キャッシュとファイルシステム、起動と終了のシーケンスを扱います。</li>
</ul>

<h3>表記規則</h3>
<ul>
  <li><strong>太字</strong>：入力するコマンド、クリックするボタン、UIメニューの項目名などを表します。</li>
  <li><em>斜体</em>：新出用語や重要な概念を強調する際に使用します。</li>
  <li><code>等幅フォント</code>：関数名、構造体名、レジストリキー、ファイルパス、ソースコードなどを表します。</li>
  <li><strong>キーの組み合わせ</strong>：<code>Ctrl+Alt+Delete</code> のようにプラス記号（+）で区切られたキーは、それらを同時に押すことを意味します。</li>
</ul>"""

pages_ja['page-16'] = """<h3>サンプルファイルと関連リソース</h3>
<p>学習をより深めるための付属コンテンツやサンプルツールは、以下の公式ページおよび GitHub リポジトリから入手できます。</p>
<ul>
  <li>Microsoft Press 公式ダウンロード：<a href="https://aka.ms/winint7ed/downloads" target="_blank" rel="noopener">https://aka.ms/winint7ed/downloads</a></li>
  <li>本書専用ツールのソースコード：<a href="https://github.com/zodiacon/windowsinternals" target="_blank" rel="noopener">https://github.com/zodiacon/windowsinternals</a></li>
</ul>

<h3>謝辞</h3>
<p>まず、本プロジェクトに新たに加わってくれた Pavel Yosifovich に心から感謝します。彼の熱意と参画なくして、本書の刊行はあり得ませんでした。過去6世代分の膨大なWindowsの進化を日夜分析・執筆し続けた彼の献身こそが、この第7版を形作った原動力です。</p>
<p>また、Windows開発チームのメンバーをはじめとするマイクロソフトの技術エキスパートたちによる徹底した技術レビューと惜しみない協力がなければ、本書がこれほどの精度と深みを持つことはできませんでした。貴重な情報提供とサポートをいただいた以下の皆様に深く御礼申し上げます（アルファベット順）：<br>
Akila Srinivasan, Alessandro Pilotti, Andrea Allievi, Andy Luhrs, Arun Kishan, Ben Hillis, Bill Messmer, Chris Kleynhans, Deepu Thomas, Eugene Bak, Jason Shirk, Jeremiah Cox, Joe Bialek, John Lambert, John Lento, Jon Berry, Kai Hsu, Ken Johnson, Landy Wang, Logan Gabriel, Luke Kim, Matt Miller, Matthew Woolman, Mehmet Iyigun, Michelle Bergeron, Minsang Kim, Mohamed Mansour, Nate Warfield, Neeraj Singh, Nick Judge, Pavel Lebedynskiy, Rich Turner, Saruhan Karademir, Simon Pope, Stephen Finnigan, Stephen Hufnagel。</p>
<p>さらに、10年以上前から Alex Ionescu に IDA Pro Advanced および Hex-Rays のライセンスを快く提供してくださっている Hex-Rays 社の Ilfak Guilfanov 氏に改めて感謝いたします。</p>"""

pages_ja['page-17'] = """<p>最後に、本書の企画・編集・出版を実現してくださった Microsoft Press の素晴らしいスタッフの方々にお礼を申し上げます。アクイジションエディターとしての最後の仕事を務めてくれた Devon Musgrave、プロジェクトエディターとして本書を統括してくれた Kate Shoup、そして品質向上に多大な貢献をしてくれた Shawn Morningstar、Kelly Talbot、Corina Lebegioara に感謝します。</p>

<h3>正誤表とサポート</h3>
<p>書籍および付属コンテンツの正確性には万全を期していますが、万一誤りを見つけられた場合は、以下の Microsoft Press 公式サイトにて既知の正誤表をご確認いただくか、新規のご報告をお寄せください。</p>
<p><a href="https://aka.ms/winint7ed/errata" target="_blank" rel="noopener">https://aka.ms/winint7ed/errata</a></p>
<p>※ 本書に関する書籍内容のお問い合わせは <code>mspinput@microsoft.com</code> で受け付けています（ソフトウェア自体の製品サポート窓口ではありません）。</p>"""
# Chapter 1: Pages 18 - 25

pages_ja['page-18'] = """<h2>第1章 概念とツール</h2>
<p>本章では、本書を通じて頻繁に登場する Microsoft Windows オペレーティングシステムの最重要概念と基本用語——Windows API、プロセス、スレッド、仮想メモリ、カーネルモードとユーザーモード、オブジェクト、ハンドル、セキュリティ、レジストリなど——について解説します。また、Windowsの内部構造を読者自身の手で調査・探究できる強力なツール群（カーネルデバッガー、パフォーマンスモニター、Sysinternalsの主要ユーティリティなど）や、より深い内部情報を得るためのリソースである Windows Driver Kit (WDK) や Windows SDK の活用方法についても紹介します。</p>
<p>本章で取り上げる内容は、以降のすべての章を読み進める上での必須の共通土台となります。確実に理解を深めておきましょう。</p>

<h3>Windows オペレーティングシステムのバージョン</h3>
<p>本書が対象とするのは、執筆時点での最新クライアントおよびサーバーOSである <strong>Windows 10</strong>（x86/ARM向けの32ビット版、およびx64向けの64ビット版）と <strong>Windows Server 2012 R2 / Windows Server 2016</strong>（64ビット版のみ）です。特に断りのない限り、解説する内容はこれらすべてのバージョンに共通して適用されます。参考として、歴代のWindows製品名・内部バージョン番号・リリース時期を表1-1に示します。</p>

<p><strong>表1-1：Windows OSのリリース履歴</strong></p>
<table style="width:100%;border-collapse:collapse;margin:1em 0;font-size:14px;">
<thead><tr style="border-bottom:2px solid var(--line);text-align:left;">
<th style="padding:6px;">製品名</th><th style="padding:6px;">内部バージョン</th><th style="padding:6px;">リリース日</th>
</tr></thead>
<tbody>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows NT 3.1</td><td style="padding:6px;">3.1</td><td style="padding:6px;">1993年7月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows NT 3.5</td><td style="padding:6px;">3.5</td><td style="padding:6px;">1994年9月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows NT 3.51</td><td style="padding:6px;">3.51</td><td style="padding:6px;">1995年5月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows NT 4.0</td><td style="padding:6px;">4.0</td><td style="padding:6px;">1996年7月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows 2000</td><td style="padding:6px;">5.0</td><td style="padding:6px;">1999年12月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows XP</td><td style="padding:6px;">5.1</td><td style="padding:6px;">2001年8月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows Server 2003</td><td style="padding:6px;">5.2</td><td style="padding:6px;">2003年3月</td></tr>"""

pages_ja['page-19'] = """<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows Server 2003 R2</td><td style="padding:6px;">5.2</td><td style="padding:6px;">2005年12月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows Vista</td><td style="padding:6px;">6.0</td><td style="padding:6px;">2007年1月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows Server 2008</td><td style="padding:6px;">6.0 (SP1)</td><td style="padding:6px;">2008年3月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows 7</td><td style="padding:6px;">6.1</td><td style="padding:6px;">2009年10月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows Server 2008 R2</td><td style="padding:6px;">6.1</td><td style="padding:6px;">2009年10月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows 8</td><td style="padding:6px;">6.2</td><td style="padding:6px;">2012年10月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows Server 2012</td><td style="padding:6px;">6.2</td><td style="padding:6px;">2012年10月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows 8.1</td><td style="padding:6px;">6.3</td><td style="padding:6px;">2013年10月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows Server 2012 R2</td><td style="padding:6px;">6.3</td><td style="padding:6px;">2013年10月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows 10</td><td style="padding:6px;">10.0 (ビルド 10240)</td><td style="padding:6px;">2015年7月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows 10 バージョン 1511</td><td style="padding:6px;">10.0 (ビルド 10586)</td><td style="padding:6px;">2015年11月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows 10 バージョン 1607 (Anniversary Update)</td><td style="padding:6px;">10.0 (ビルド 14393)</td><td style="padding:6px;">2016年7月</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows Server 2016</td><td style="padding:6px;">10.0 (ビルド 14393)</td><td style="padding:6px;">2016年10月</td></tr>
</tbody></table>

<p>表を見るとわかるように、Windows 7 以降、内部バージョン番号の付け方は直感的な製品名から乖離しています。Windows 7 の内部バージョンは「7.0」ではなく「6.1」でした。これは、Windows XPの絶大な普及の後、Windows Vistaがバージョンを「6.0」へ引き上げた際に、多くの既存アプリが「メジャーバージョン5以上、かつマイナーバージョン1以上」という安易な判定ロジックを組んでいたために誤判定を起こして動作しなくなった教訓に基づいています。互換性問題を避けるため、Windows 7（6.1）、Windows 8（6.2）、Windows 8.1（6.3）とメジャーバージョンを据え置き続けました。しかし Windows 10 に至り、内部バージョンもついに <strong>10.0</strong> へと刷新されました。</p>

<blockquote><p><strong>注意：</strong> Windows 8 以降、従来の <code>GetVersionEx</code> API 関数は後方互換性維持のため、実際がどのOSであっても既定で「6.2」（Windows 8）を返すよう仕様変更され、非推奨（deprecated）となりました。OSのバージョン番号を直接調べる手法は、帯域外で個別インストールされる機能もあるため現代では推奨されません。正確なOSバージョンを判定する必要がある場合は、<code>VerifyVersionInfo</code> 関数や、新しいバージョンヘルパーAPI（<code>IsWindows8OrGreater</code>、<code>IsWindows10OrGreater</code>、<code>IsWindowsServer</code> など）を使用するか、実行可能ファイルのマニフェストで対象OSのサポートを明示的に宣言する必要があります（詳細はPart 2 第8章「システムメカニズム」を参照）。</p></blockquote>"""

pages_ja['page-20'] = """<p>現在のWindowsのバージョン情報は、コマンドラインで <code>ver</code> コマンドを実行するか、ファイル名を指定して実行（Win+R）から <code>winver</code> を実行することでグラフィカルに確認できます。図に Windows 10 Enterprise バージョン 1511 での <code>winver</code> 実行画面を示します。</p>

<figure><img loading="lazy" width="282" height="249" src="assets/1c09474e9a9d5381921685df.webp" alt="winverの実行画面"><figcaption>図：winver によるバージョン情報の表示</figcaption></figure>

<p>画面にはWindowsのビルド番号（この例では <code>10586.218</code>）も表示されています。これは先行プレビューを受け取る Windows Insider にとって有用であるだけでなく、どのセキュリティ修正パッチレベルが適用されているかを把握する上でも極めて重要です。</p>

<h3>Windows 10 と将来のバージョン</h3>
<p>Windows 10 の登場にあたり、マイクロソフトはこれまでよりも速い頻度でOSを継続アップデートしていく方針を打ち出しました。旧来のように「Windows 11」のような大きな別売パッケージを出すのではなく、Windows Update（または企業のサービシングモデル）を通じて稼働中の Windows 10 が最新のバージョンへと順次アップデートされていきます。本書の執筆時点までに、2015年11月（サービス提供年月を示す「バージョン1511」）と、2016年7月（「バージョン1607」、通称 Anniversary Update）の2つのメジャーアップデートが提供されています。</p>

<blockquote><p><strong>注意：</strong> マイクロソフト社内では、Windowsのビルドは依然として「波（Wave）」として管理されています。例えば、Windows 10 の初期リリースはコードネーム「Threshold 1」、2015年11月の更新は「Threshold 2」と呼ばれました。続くアップデート群は「Redstone 1」（RS1＝バージョン1607）、Redstone 2（RS2＝バージョン1703、Creators Update）、Redstone 3（RS3＝Fall Creators Update）と呼ばれています。</p></blockquote>

<h3>Windows 10 と OneCore</h3>
<p>Windows 10 の技術的到達点の中で最も象徴的なのが <strong>OneCore</strong> の完成です。今日のWindowsは、従来のデスクトップPCやノートPCだけでなく、サーバー、スマートフォン（Windows 10 Mobile）、Xbox One、ウェアラブルホログラフィックPCである HoloLens、そしてRaspberry Piなどの小型IoTデバイスに至るまで、極めて広範な機器で動作しています。</p>"""

pages_ja['page-21'] = """<p>これらのデバイスは形状（フォームファクタ）も性能も大きく異なります。例えば HoloLens で物理マウスやキーボードをサポートしてもあまり意味がないため、そうしたデバイス用の Windows 10 では一部の機能が省かれています。しかし、<strong>カーネル、コアデバイスドライバ、およびベースプラットフォームのバイナリ自体はすべてのデバイスで本質的に同一</strong>です（パフォーマンスやハードウェア要件に応じたレジストリやポリシー設定の差異は存在します。第3章「プロセスとジョブ」の「APIセット」節でその具体例を解説します）。</p>

<p>本書では、どのデバイスで稼働しているかにかかわらず、根底にある <strong>OneCore カーネルの内部構造</strong>を解き明かします。ただし、スマートフォンやXbox One上で直接実験を行うのは困難（または公式に不可能）なため、本書で紹介する各種の「実験」は主に手元で容易に検証できるデスクトップ環境（マウス・キーボード付きPC）を対象としています。</p>

<h3>基本概念と用語</h3>
<p>ここからは、Windowsの全体像を理解する上で不可欠となる最重要概念を紹介していきます。プロセス、スレッド、仮想メモリなどの多くは、以降の章でさらに詳しく深掘りされます。</p>

<h3>Windows API</h3>
<p><strong>Windows API</strong>（アプリケーションプログラミングインターフェース）は、Windows OSファミリーが提供するユーザーモードの公式システムプログラミングインターフェースです。Windows APIを介してアプリケーションを作成することで、基礎となるハードウェアの差異や将来のOSバージョンの違いを意識することなく、安定して動作するソフトウェアを構築できます。</p>"""

pages_ja['page-22'] = """<h4>Windows APIの多様な形態（フレーバー）</h4>
<p>Windows APIは当初、純粋なC言語スタイルの関数群として誕生しました。現在では開発者が利用できる関数は数万点にも及びます。Windowsの黎明期において、C言語は他の言語からも容易に呼び出せる「最大公約数」であり、OSの低レベルサービスを公開するのに最も適した選択肢でした。しかし、関数の膨大化に伴い、命名規則の一貫性の欠如や、C++の名前空間のような論理的グループ分けができないという限界が顕在化しました。この問題を克服するために導入されたのが <strong>COM（Component Object Model）</strong> です。</p>

<p>COMはもともと、Word文書の中にExcelの表やグラフを埋め込むような、Officeアプリ間でのデータ交換・複合文書連携を実現する技術「OLE（Object Linking and Embedding）」のために考案されました。初期のOLEはDDE（Dynamic Data Exchange）という古いWindowsメッセージング機能を利用していましたが、その制約が厳しかったため、新たな通信基盤としてCOM（1993年頃に「OLE 2」として登場）が開発されたのです。</p>

<p>COMは2つの根本原則の上に成り立っています。第1に、クライアントはオブジェクトと直接ではなく「インターフェース」（論理的に関連する一連のメソッドが厳格に定義された規約）を介して通信します。第2に、各インターフェースは <code>IUnknown</code> を基本型とし、参照カウントによる生存期間管理（<code>AddRef</code> / <code>Release</code>）と、他のインターフェースを取得する仕組み（<code>QueryInterface</code>）を共通して備えています。</p>

<h4>The Windows Runtime (WinRT)</h4>
<p>Windows 8 の登場とともに導入されたのが <strong>Windows Runtime（WinRT）</strong> です。WinRTは、スマートフォン、タブレット、PCなど多様な画面サイズや入力方式に適応した、新しいアプリケーションモデル「Windows アプリ（当初はストアアプリやModernアプリと呼ばれ、現在は Universal Windows Platform: UWP アプリとして知られる）」を支えるコアAPI基盤です。</p>"""

pages_ja['page-23'] = """<p>アーキテクチャの観点から見ると、WinRTはCOMの強固な土台の上に構築されており、基本COMインフラに多数の現代的な拡張を加えたものです。例えば、COMのタイプライブラリを発展させ、.NETメタデータ形式に基づく完全な型メタデータ（<code>.winmd</code> ファイルに格納）を標準で保持しています。API設計の観点からも、名前空間による整然とした階層構造、一貫した命名規約、オブジェクト指向プログラミングパターンが徹底されており、従来のクラシックなC言語形式Windows APIよりもはるかに洗練されています。</p>

<p>Windowsアプリ（UWP）は、従来のデスクトップアプリ（クラシックWindowsアプリ）とは異なる厳格なセキュリティ・ライフサイクルルールに従います（詳細はPart 2 第9章で解説）。</p>

<p>各種APIとアプリケーションの関係は単純な二者択一ではありません。デスクトップアプリからWinRT APIの一部を呼び出すこともできますし、逆にWindowsアプリからWin32やCOM APIの一部を利用することも可能です。ただし重要な点として、<strong>バイナリレベルではWinRT APIも依然として従来のWindows基盤バイナリとWindows APIの上に成り立っている</strong>ということです。.NETが内部で従来のWindows APIを呼び出しているのと同様に、WinRTはOSにとって完全に新しい「ネイティブ」カーネル層を意味するものではありません。</p>

<p>開発者は、C++、C#（その他.NET言語）、JavaScriptなど様々な言語からWinRTを快適に呼び出すことができます。マイクロソフトは各言語向けに「言語プロジェクション」を提供しており、例えばC++向けには <code>C++/CX</code>（現在はC++/WinRTに進化）、.NET向けにはネイティブコードのように透過的に呼べるCOM相互運用レイヤー、JavaScript向けには <code>WinJS</code> などが用意されています。</p>

<h4>The .NET Framework</h4>
<p><strong>.NET Framework</strong> は現代のWindowsに不可欠な構成要素として標準同梱されています。表1-2に各Windowsバージョンで既定インストールされている .NET Framework のバージョンを示します（上位のバージョンを後から導入することも可能です）。</p>

<p><strong>表1-2：Windowsの既定の .NET Framework バージョン</strong></p>
<table style="width:100%;border-collapse:collapse;margin:1em 0;font-size:14px;">
<thead><tr style="border-bottom:2px solid var(--line);text-align:left;">
<th style="padding:6px;">Windows バージョン</th><th style="padding:6px;">.NET Framework バージョン</th>
</tr></thead>
<tbody>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows 8</td><td style="padding:6px;">4.5</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows 8.1</td><td style="padding:6px;">4.5.1</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows 10 (初期版)</td><td style="padding:6px;">4.6</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows 10 バージョン 1511</td><td style="padding:6px;">4.6.1</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Windows 10 バージョン 1607</td><td style="padding:6px;">4.6.2</td></tr>
</tbody></table>"""

pages_ja['page-24'] = """<p>.NET Framework は主に以下の2つの巨大な構成要素から成り立っています：</p>
<ul>
  <li><strong>共通言語ランタイム（CLR: Common Language Runtime）</strong>：.NETの実行時エンジンです。CIL（共通中間言語）コードを実行時にCPUの機械語へと変換する JIT（Just-In-Time）コンパイラ、自動メモリ管理を行うガベージコレクター（GC）、型検証、コードアクセスセキュリティなどの高度なランタイムサービスを提供します。CLR自体はインプロセスCOMサーバー（DLL）として実装されており、Windows APIを内部でフル活用しています。</li>
  <li><strong>.NET Framework クラスライブラリ（FCL: Framework Class Library）</strong>：UI、ネットワーク通信、データベースアクセス、ファイルI/O、暗号化など、クライアントやサーバーアプリが必要とするあらゆる機能を網羅した膨大な型（クラス・インターフェース）のライブラリです。</li>
</ul>

<p>これらの機構と高水準言語（C#, Visual Basic, F#）により、開発者の生産性とアプリケーションの安全性・信頼性が飛躍的に向上します。図1-1に .NET Framework と Windows OS の階層関係を示します。</p>

<figure><img loading="lazy" width="358" height="223" src="assets/d7a7e4fe0af9260b76f81a00.webp" alt=".NET Framework と Windows OS の関係"><figcaption>図1-1：.NET Framework と Windows OS の階層構造</figcaption></figure>

<h3>サービス、関数、ルーチン</h3>
<p>Windowsのドキュメントや技術解説では、文脈によって意味が異なる用語がいくつかあります。例えば「サービス」という言葉は、OSの呼び出し可能なルーチンを指すこともあれば、デバイスドライバを指すことも、バックグラウンドのサーバープロセスを指すこともあります。本書では混乱を避けるため、以下の定義に統一しています：</p>
<ul>
  <li><strong>Windows API 関数</strong>：Windows APIとして公式に文書化され、外部から呼び出し可能なサブルーチン（例: <code>CreateProcess</code>, <code>CreateFile</code>, <code>GetMessage</code>）。</li>
  <li><strong>ネイティブシステムサービス（システムコール）</strong>：ユーザーモードから呼び出し可能な、OS内部の文書化されていない基盤サービス（例: <code>NtCreateUserProcess</code>。Windows APIの <code>CreateProcess</code> が内部で呼び出す真のシステムサービス）。</li>
  <li><strong>カーネルサポート関数（カーネルルーチン）</strong>：カーネルモードでのみ呼び出し可能な、OS内部のサブルーチン（例: デバイスドライバがシステムヒープからメモリを確保する際に呼ぶ <code>ExAllocatePoolWithTag</code>）。</li>
</ul>"""

pages_ja['page-25'] = """<ul>
  <li><strong>Windows サービス</strong>：Windowsのサービスコントロールマネージャー（SCM）によって管理・起動されるバックグラウンドプロセス（例: UNIXの cron や at に相当する <code>schtasks</code> を支えるタスクスケジューラサービス）。※レジストリ上はデバイスドライバも「サービス」として定義されますが、本書ではそれらは単にドライバと呼び、サービスとは呼びません。</li>
  <li><strong>ダイナミックリンクライブラリ（DLL）</strong>：複数のアプリケーションから実行時に動的にロード・共有できるサブルーチンのバイナリライブラリ（例: Cランタイムの <code>Msvcrt.dll</code>、Windowsサブシステムの中核である <code>Kernel32.dll</code>）。WindowsはDLLのコードセクションを物理メモリ上で1箇所のみに展開し、それを参照する全プロセス間で共有させるため、メモリを大幅に節約できます。なお、.NETアセンブリもDLL形式で配布されますが、機械語のエクスポート関数ではなく、CLRが解析するコンパイル済みメタデータを含んでいます。</li>
</ul>

<h3>プロセス（Processes）</h3>
<p>日常の会話では「プログラム」と「プロセス」が同義に使われがちですが、内部構造においては明確に異なります。<strong>プログラムはディスク上に置かれた静的な命令列（実行ファイル）</strong>に過ぎません。これに対し、<strong>プロセスはそのプログラムのインスタンスを実行する際に必要な、OS上のあらゆるリソースを束ねる「動的なコンテナ」</strong>です。</p>

<p>最も高い抽象レベルにおいて、Windowsのプロセスは以下の要素で構成されています：</p>
<ul>
  <li><strong>専用のプライベート仮想アドレス空間</strong>：そのプロセスのみが利用できるメモリ番地の集合。</li>
  <li><strong>実行可能プログラム</strong>：初期コードとデータが定義され、仮想アドレス空間内にマッピングされるイメージ。</li>
  <li><strong>オープンされたハンドルのリスト</strong>：セマフォ、同期オブジェクト、ファイルなど、プロセス内の全スレッドからアクセス可能なシステムリソースへの参照テーブル。</li>
  <li><strong>セキュリティコンテキスト（アクセストークン）</strong>：実行ユーザー、所属グループ、付与された特権、UACの仮想化状態、セッションID、サンドボックス情報（AppContainer IDなど）を保持するトークン。</li>
  <li><strong>プロセスID（PID）</strong>：OS内で一意に識別するための数値（内部的にはクライアントIDの一部）。</li>
  <li><strong>少なくとも1つの実行スレッド</strong>：スレッドの存在しない「空のプロセス」も理論上作成できますが、コードを実行できないため実用的な意味はありません。</li>
</ul>

<p>プロセスの内部状態を調査・監視・操作するためのツールは多数存在します。Windows標準のタスクマネージャーから、デバッグツール、そして極めて多機能な Sysinternals ツールまで、それぞれの特徴を以下の実験を通じて確認していきましょう。</p>"""
# Chapter 1: Pages 26 - 35

pages_ja['page-26'] = """<p>プロセスの活動状況を観察するツールとして最も広く使われているのが、Windows標準の「タスクマネージャー」です（Windowsカーネル内には「タスク」という概念は存在しないため、この名称はやや奇妙ですが歴史的なものです）。以下の実験で基本的な機能を見てみましょう。</p>

<h4>実験：タスクマネージャーによるプロセス情報の確認</h4>
<p>タスクマネージャーは以下のいずれかの方法で素早く起動できます：</p>
<ul>
  <li><code>Ctrl + Shift + Esc</code> キーを押す</li>
  <li>タスクバーの何もないところを右クリックし、<strong>タスク マネージャー</strong> を選択する</li>
  <li><code>Ctrl + Alt + Delete</code> キーを押し、画面から <strong>タスク マネージャー</strong> を選択する</li>
  <li>ファイル名を指定して実行（Win+R）から <code>taskmgr.exe</code> を実行する</li>
</ul>

<p>初回起動時や最小化表示時は「簡易表示」モードになっており、トップレベルの可視ウィンドウを持つアプリのみが表示されます。</p>

<figure><img loading="lazy" width="187" height="166" src="assets/9110ee50be4758bec71f76f7.webp" alt="タスクマネージャーの簡易表示"><figcaption>図：タスクマネージャーの簡易表示モード</figcaption></figure>

<p>この画面では詳細な情報が得られないため、左下の <strong>詳細</strong> ボタンをクリックしてフル表示に切り替えます。既定では「プロセス」タブが表示されます。</p>

<figure><img loading="lazy" width="223" height="215" src="assets/8546556391580688f277db8f.webp" alt="タスクマネージャーのプロセス一覧"><figcaption>図：タスクマネージャーの「プロセス」タブ</figcaption></figure>

<p>「プロセス」タブには、アプリ、バックグラウンドプロセス、Windowsプロセスの分類ごとにプロセスが一覧表示され、CPU・メモリ・ディスク・ネットワークの4つの主要負荷列が表示されます。列ヘッダーを右クリックすることで、PID（プロセスID）や状態、発行元、コマンドラインなどの追加列を自由に表示できます。展開可能なプロセスでは、そのプロセスが所有するトップレベルウィンドウの一覧も確認できます。</p>"""

pages_ja['page-27'] = """<p>さらに詳細なシステム情報を得るには、「詳細」タブに切り替えます（プロセスを右クリックして「詳細の表示」を選択すると、そのプロセスが選択された状態で直接切り替わります）。</p>

<blockquote><p><strong>注意：</strong> Windows 7 のタスクマネージャーにおける「プロセス」タブが、Windows 8 以降の「詳細」タブに相当します。また、Windows 7 の「アプリケーション」タブ（ウィンドウ単位の一覧）に相当する機能が、Windows 8 以降の新しい「プロセス」タブに統合されています。</p></blockquote>

<figure><img loading="lazy" width="330" height="331" src="assets/b8c60cd4670bf78f80c41e1b.webp" alt="タスクマネージャーの詳細タブ"><figcaption>図：タスクマネージャーの「詳細」タブ</figcaption></figure>

<p>「詳細」タブはより高密度で、OS内部のプロセス一覧をフラットに表示します。ウィンドウの有無にかかわらず全プロセスが網羅され、極めて多彩な列を選択できます。列ヘッダーを右クリックして「列の選択」をクリックすると、表示可能な膨大な項目がダイアログに現れます。</p>

<figure><img loading="lazy" width="188" height="197" src="assets/62941789a387e65fc1d9b9f6.webp" alt="タスクマネージャーの列の選択ダイアログ"><figcaption>図：タスクマネージャーの列の選択</figcaption></figure>"""

pages_ja['page-28'] = """<p>特に重要な表示列の意味は以下の通りです：</p>
<ul>
  <li><strong>スレッド（Threads）</strong>：そのプロセス内で稼働しているスレッドの総数です。スレッドを持たないプロセスは直接生成できず、存在しても何も処理できないため、通常は常に1以上となります。もしスレッド数が0のプロセスが残っている場合、何らかの理由（多くはバグのあるドライバの処理待ち）でプロセスが正常に破棄できず残留していることを示します。</li>
  <li><strong>ハンドル（Handles）</strong>：そのプロセス内のスレッドによってオープンされている、カーネルオブジェクト（ファイル、イベント、レジストリキー等）へのハンドル総数です。</li>
  <li><strong>状態（Status）</strong>：UIを持たない純粋なバックグラウンドプロセスの場合、通常は「実行中」となります（スレッド自体はイベント待ちやI/O完了待ちでブロックしていてもプロセスとしては稼働中とみなされます）。すべてのスレッドが一時停止状態にある場合は「中断（Suspended）」となります。これは通常自然には起きず、未公開ネイティブAPIの <code>NtSuspendProcess</code> などを外部ツール（Process Explorer等）から呼び出した場合に生じます。一方、UIを持つプロセスの場合、「実行中」はウィンドウのメッセージキューが応答している（イベントを処理できる）状態を意味します。Windowsストアアプリ（UWPアプリ）の場合は、ユーザーがアプリを最小化してバックグラウンドに回ると、5秒後にCPUやネットワーク消費を抑えるために自動的に「中断」状態へと移行します。これはバッテリー駆動機器（ノートPC・タブレット・スマートフォン）にとって極めて重要な省電力機構です。3つ目の状態が「応答なし（Not Responding）」です。これはUIスレッドが5秒以上にわたってメッセージキューの確認を行わなかった場合に発生します。スレッドが高負荷な計算に専念しているか、I/O待ちでブロックされているためUIがフリーズした状態であり、Windowsは該当ウィンドウを半透明化（ゴースト化）してタイトルバーに「(応答なし)」を付加します。</li>
</ul>

<p>各プロセスは、自身を起動した「親プロセス（作成者プロセス）」への参照（親PID）を保持しています。ただし、親プロセスがすでに終了している場合、この情報は更新されません。そのため、存在しない古い親PIDを指し続けるケースが多々ありますが、システムの安定性には何の影響もありません。Process Explorer などの高度なツールでは、PIDの再利用による誤認を防ぐため、親プロセスの開始日時も厳密に照合してツリーを構築します。</p>"""

pages_ja['page-29'] = """<blockquote><p><strong>親プロセスと作成者プロセスの違い：</strong> 特定のユーザーアプリケーションが起動したように見えるプロセスであっても、内部ではプロセスの生成APIを代行呼び出しする「ブローカープロセス（支援プロセス）」が介在している場合があります。このような場合、ブローカーをそのまま親としてツリー表示すると利用者が混乱するため（またハンドルやアドレス空間の継承の観点からも不適切な場合があるため）、親プロセスの「付け替え（Re-parenting）」が行われます。この具体例は第7章「セキュリティ」で解説します。</p></blockquote>

<h4>実験：プロセーツリーの観察（tlist /t）</h4>
<p>一般的なツールではあまり表示されませんが、プロセスには「親プロセスID（作成元PID）」という属性があります。この値はパフォーマンスモニターやプログラムから取得可能です。Windows Debugging Tools に含まれる <code>tlist.exe</code> に <code>/t</code> オプションを付けて実行すると、プロセスの親子関係をインデント付きのツリー形式で出力できます。以下に出力例を示します：</p>

<pre>System Process (0)
System (4)
smss.exe (360)
csrss.exe (460)
wininit.exe (524)
services.exe (648)
svchost.exe (736)
unsecapp.exe (2516)
WmiPrvSE.exe (2860)
RuntimeBroker.exe (3104)
SearchUI.exe (3504) Cortana
svchost.exe (788)
sihost.exe (3664)
taskhostw.exe (3032) Task Host Window
spoolsv.exe (1644)
svchost.exe (1936)
OfficeClickToRun.exe (1324)
MSOIDSVC.EXE (1256)</pre>"""

pages_ja['page-30'] = """<pre>MSOIDSVCM.EXE (2264)
MBAMAgent.exe (2072)
MsMpEng.exe (2116)
SearchIndexer.exe (1000)
SearchProtocolHost.exe (824)
svchost.exe (3328)
TrustedInstaller.exe (6052)
lsass.exe (664)
csrss.exe (536)
winlogon.exe (600)
dwm.exe (1100) DWM Notification Window
explorer.exe (3148) Program Manager
OneDrive.exe (4448)
cmd.exe (5992) C:\windows\system32\cmd.exe - tlist  /t
conhost.exe (3120) CicMarshalWnd
tlist.exe (5888)
SystemSettingsAdminFlows.exe (4608)</pre>

<p>ツリー表示では、インデントによって親子関係が表現されます。すでに親プロセスが終了してしまっているプロセス（上記の例の <code>explorer.exe</code> など）は、親を遡ることができないため最左端に配置されます。Windowsが記録しているのは「直近の親PID」のみであり、親の親（祖父母）といった家系図全体のリンクを辿る仕組みは保持していないからです。括弧内の数字はPIDであり、末尾のテキストはそのプロセスが作成したウィンドウのタイトルです。</p>

<p>Windowsが親PID以上のリンクを保持していないことは、以下の簡単な手順で実際に確かめられます：</p>
<ol>
  <li><code>Win + R</code> を押し、<code>cmd</code> と入力して Enter を押しコマンドプロンプトを開く。</li>
  <li><code>title Parent</code> と入力してウィンドウのタイトルを "Parent" に変更する。</li>
  <li><code>start cmd</code> と入力し、2つ目のコマンドプロンプトを起動する。</li>
  <li>2つ目のウィンドウで <code>title Child</code> と入力してタイトルを "Child" に変更する。</li>
  <li>2つ目のウィンドウから <code>mspaint</code> と入力してペイントを起動する。</li>
  <li>2つ目のウィンドウ（Child）で <code>exit</code> と入力して閉じる。ペイントはそのまま残る。</li>
  <li>タスクマネージャーを開き、「プロセス」タブで "Parent"（最初のcmd）を見つける。</li>
  <li>右クリックして「詳細の表示」へ移動し、該当の <code>cmd.exe</code> を右クリックして <strong>プロセスのツリーの終了</strong> を選択する。</li>
</ol>"""

pages_ja['page-31'] = """<figure><img loading="lazy" width="349" height="364" src="assets/ac850d7d88b0e5074dae37e7.webp" alt="タスクマネージャーでのコマンドプロセッサツリー"><figcaption>図：タスクマネージャー上でのプロセスの階層</figcaption></figure>

<p>「プロセスのツリーの終了」を実行すると、最初のコマンドプロンプト（Parent）は終了しますが、<strong>ペイント（mspaint）は終了せずにそのままデスクトップに残り続けます</strong>。中間プロセス（Child）が先に終了してしまっていたため、祖父にあたる Parent と孫にあたるペイントの間の論理的リンクが完全に切断されており、OS側から子孫関係を特定できなかったためです。</p>

<h4>Sysinternals Process Explorer</h4>
<p>マイクロソフトの Sysinternals ツール群に含まれる <strong>Process Explorer</strong> は、市販・無償を問わず世界中のあらゆるツールの中で、Windowsのプロセスとスレッドに関する最も深く正確な情報を可視化できる決定版ユーティリティです。本書の随所で行う実験でも主役として活躍します。Process Explorer の主な特徴は以下の通りです：</p>
<ul>
  <li>プロセスのセキュリティトークン詳細（所属グループ、付与特権、整合性レベル、仮想化状態）</li>
  <li>プロセス、スレッド、DLL、ハンドルの生成・消滅を色分けハイライト表示</li>
  <li>サービスホストプロセス（<code>svchost.exe</code> 等）内部で実行されている具体的なサービス名と説明の一覧</li>
</ul>"""

pages_ja['page-32'] = """<ul>
  <li>緩和策ポリシー（Mitigation Policies）やプロセス保護レベル（Protected Process Light: PPL 等）の可視化</li>
  <li>ジョブオブジェクトに所属するプロセスとその制限設定の詳細</li>
  <li>.NET アプリケーションの詳細（AppDomain一覧、ロード済みアセンブリ、CLRパフォーマンスカウンタ）</li>
  <li>Windows Runtime をホストする Modern/UWP プロセスのパッケージ情報</li>
  <li>プロセスおよび各スレッドの正確な起動日時</li>
  <li>DLLだけでなく、メモリマップトファイルを含む完全なマッピングファイル一覧</li>
  <li>個別のスレッドやプロセス全体をワンクリックで一時停止（サスペンド）および再開</li>
  <li>暴走した単一スレッドの強制終了</li>
  <li>一定期間に最もCPUを消費したプロセスの的確な特定</li>
  <li>折りたたみ可能な完全なプロセーツリー表示</li>
  <li>プロセスがオープンしている全ハンドル（名前なしハンドル含む）の一覧表示</li>
  <li>スレッドのCPUサイクル数に基づく極めて正確なCPU消費率の把握（第4章「スレッド」で詳解）</li>
  <li>メモリマネージャーの詳細（コミットチャージのピーク値、ページプール/非ページプールのカーネルメモリ消費量など）</li>
</ul>

<p>それでは、Process Explorer の基本操作を体験してみましょう。</p>"""

pages_ja['page-33'] = """<h4>実験：Process Explorer によるプロセス内部の観察</h4>
<p>Sysinternals の公式サイトから最新の Process Explorer をダウンロードして実行します。標準ユーザー権限でも動作しますが、右クリックして <strong>管理者として実行</strong> すると、専用のカーネルドライバがロードされ、より多くの内部情報が開放されます。</p>

<p>初回起動時に最も重要なのが「シンボルの設定」です。シンボルが設定されていないと、プロセスのプロパティで「スレッド」タブを開いた際に警告が出たり、関数名が表示されずメモリアドレスのみとなってしまいます。シンボルが正しく設定されると、スレッドの開始関数やコールスタック（関数呼び出し履歴）がシンボル名（関数名）で表示され、各スレッドが内部で何を実行しているかが一目瞭然となります。シンボルを利用するには、Windows SDK に含まれる <strong>Debugging Tools for Windows</strong> がインストールされている必要があります。メニューの <strong>Options → Configure Symbols</strong> を開き、Dbghelp.dll のパスとシンボルパスを以下のように設定します：</p>

<figure><img loading="lazy" width="269" height="147" src="assets/bc299bfa7a6177bfa3b308a1.webp" alt="シンボル設定画面"><figcaption>図：Process Explorer のシンボルパス設定</figcaption></figure>

<p>シンボルパスに <code>srv*c:\symbols*http://msdl.microsoft.com/download/symbols</code> と指定すると、必要なシンボルファイルがマイクロソフトの公式シンボルサーバーから自動的にダウンロードされ、ローカルの <code>C:\symbols</code> フォルダにキャッシュされます。</p>

<blockquote><p><strong>ヒント：</strong> システム環境変数 <code>_NT_SYMBOL_PATH</code> に上記と同じシンボルパス文字列を設定しておくと、Process Explorer だけでなく、WinDbg などのデバッガーや Visual Studio も共通して自動的にこのシンボルサーバーを参照するようになるため、個別の設定の手間が省けます。</p></blockquote>"""

pages_ja['page-34'] = """<p>Process Explorer を起動すると、上部ペインにプロセーツリーがグラフィカルに表示されます。下部ペイン（View → Show Lower Pane）を開くことで、選択中のプロセスが保持するハンドル一覧や、ロードされているDLLおよびメモリマップトファイルの一覧を瞬時に確認できます。また、プロセスの名前にマウスカーソルを合わせると、ツールチップでフルパスやコマンドラインが表示されます。特定のプロセスでは以下のような付加情報もツールチップに表示されます：</p>
<ul>
  <li><code>svchost.exe</code> などのサービスホスト内部で稼働しているサービス名</li>
  <li><code>taskhostw.exe</code> などのタスクホスト内部で稼働しているスケジュールタスク名</li>
  <li>コントロールパネル等から呼ばれた <code>rundll32.exe</code> の呼び出し先ターゲット</li>
  <li><code>dllhost.exe</code>（COMサロゲート）内でホストされている COM クラス情報</li>
  <li><code>WmiPrvSE.exe</code> などの WMI ホストが提供しているプロバイダ情報</li>
  <li>UWP/Windowsストアアプリのパッケージメタデータ</li>
</ul>

<figure><img loading="lazy" width="562" height="390" src="assets/00806f91cd73b0f134142718.webp" alt="Process Explorer のメイン画面"><figcaption>図：Process Explorer によるプロセス詳細の可視化</figcaption></figure>

<p>以下の手順で Process Explorer の基本操作を体験してみましょう：</p>
<ol>
  <li><strong>プロセスの色分け</strong>：既定ではサービスホストはピンク色、自身が起動した通常プロセスは青色などで色分けされています。これらは <strong>Options → Configure Colors</strong> から自由にカスタマイズ可能です。</li>
  <li><strong>ツールチップの確認</strong>：プロセス名の上にマウスを置くと、実行ファイルのフルパスやコマンドライン、ホスト中のサービス名などがポップアップ表示されます。</li>
</ol>"""

pages_ja['page-35'] = """<ol start="3">
  <li><strong>表示列の追加</strong>：<strong>View → Select Columns</strong> を開き、「Process Image」タブで「Image Path（実行ファイルパス）」にチェックを入れて列を追加してみましょう。</li>
  <li><strong>ツリー表示とソートの切り替え</strong>：「Process」列ヘッダーをクリックすると、プロセス名によるアルファベット順ソートに切り替わり、ツリー表示が一時的に解除されます。もう一度クリックすると逆順（Z〜A）になり、3回目をクリックすると元のプロセーツリー表示に戻ります。</li>
  <li><strong>自身のプロセスのみに絞り込む</strong>：<strong>View</strong> メニューの <strong>Show Processes from All Users</strong> のチェックを外すと、現在のログオンユーザーが所有するプロセスのみに一覧を絞り込めます。</li>
  <li><strong>差分ハイライトの確認</strong>：<strong>Options → Difference Highlight Duration</strong> を「3 seconds」に変更します。この状態で何か新しいアプリケーション（メモ帳や電卓など）を起動すると、新プロセスが3秒間鮮やかな緑色でハイライトされます。そのアプリを終了すると、今度は3秒間赤色でハイライトされてから一覧から消えます。バックグラウンドで一瞬だけ起動して消えるプロセスの追跡に極めて有用です。</li>
  <li><strong>プロセスのプロパティ探索</strong>：任意のプロセスをダブルクリックすると、詳細なプロパティウィンドウが開きます。スレッド、環境変数、セキュリティ、パフォーマンスなど多彩なタブが用意されており、本書の以降の実験でも頻繁に登場します。</li>
</ol>

<h3>スレッド（Threads）</h3>
<p><strong>スレッド</strong> は、WindowsがCPUの実行時間を割り当てる（スケジュールする）基本単位です。スレッドが存在しなければ、プロセス内のプログラムコードが実行されることはありません。1つのスレッドは以下のコア要素で構成されています：</p>
<ul>
  <li><strong>CPUレジスタ群の状態（プロセッサコンテキスト）</strong>：プログラムカウンタ（命令ポインタ）、スタックポインタ、汎用レジスタなどの値。</li>
  <li><strong>2つのスタック</strong>：カーネルモードで実行中に使用するカーネルスタックと、ユーザーモードで実行中に使用するユーザースタック。</li>
  <li><strong>スレッドローカルストレージ（TLS）</strong>：ランタイムライブラリやDLLがスレッド専用の変数を格納するためのプライベート記憶域。</li>
  <li><strong>スレッドID（TID）</strong>：システム内でスレッドを一意に識別するID（内部的にはクライアントIDの一部であり、PIDとTIDは同一のID空間から採番されるため重複することはありません）。</li>
</ul>

<p>さらに、特定のスレッドはクライアントになりすまして処理を行うために、プロセスとは独立した独自の「セキュリティコンテキスト（アクセストークン）」を保持することもあります（マルチスレッドサーバーなどで頻繁に使用されます）。</p>
<p>CPUレジスタ群、スタック、プライベート記憶域などの情報はまとめて <strong>スレッドコンテキスト</strong> と呼ばれます。これらはCPUアーキテクチャ（x86、x64、ARM）に強く依存するため、OS内部構造としてもアーキテクチャ依存の <code>CONTEXT</code> 構造体として定義されており、<code>GetThreadContext</code> API 関数から取得できます。</p>
<p>あるスレッドから別のスレッドへと実行を切り替える処理は「コンテキストスイッチ」と呼ばれ、カーネルのスケジューラが介入するため一定のCPUオーバーヘッドを伴います。Windowsはこの切り替えコストを最小限に抑えるための仕組みとして、<strong>ファイバー（Fibers）</strong> と <strong>ユーザーモードスケジューリング（UMS）</strong> の2つの機構を提供しています。</p>"""
# Chapter 1: Pages 36 - 45

pages_ja['page-36'] = r"""<blockquote><p><strong>注意：</strong> 64ビット版Windows上で動作する32ビットアプリケーションのスレッドは、32ビット用と64ビット用の両方のコンテキストを保持しています。これらは <strong>Wow64</strong>（Windows-on-Windows 64-bit）が32ビットモードと64ビットモードを相互に切り替える際に使用されます。このスレッドは2つのユーザースタックと2つの <code>CONTEXT</code> ブロックを持ち、通常の Windows API は64ビット側のコンテキストを返します（32ビット側のコンテキストを取得するには <code>Wow64GetThreadContext</code> を使用します。詳細はPart 2 第8章を参照）。</p></blockquote>

<h4>ファイバー（Fibers）</h4>
<p><strong>ファイバー</strong> は、Windows標準の優先度ベースのカーネルスケジューラに頼らず、アプリケーション自身の手で実行単位をスケジューリングできるようにする「軽量スレッド」です。カーネルからは完全に不可視であり、すべて <code>Kernel32.dll</code> のユーザーモード空間で協調的に実装されています。</p>
<p>ファイバーを使用するには、まず <code>ConvertThreadToFiber</code> 関数を呼び出して通常のスレッドを稼働中のファイバーへと変換します。その後、<code>CreateFiber</code> を呼び出して追加のファイバーを作成します。ただし通常のスレッドと異なり、ファイバーは生成されても自動的には実行されず、<code>SwitchToFiber</code> 関数を明示的に呼び出して切り替えることで初めて実行が開始されます。呼び出されたファイバーは、自ら終了するか、あるいは別のファイバーを明示的に指定して <code>SwitchToFiber</code> を呼び出すまでCPUを占有し続けます。</p>

<blockquote><p><strong>注意：</strong> 現代のプログラミングにおいて、ファイバーの使用は原則として推奨されません。カーネルから見えないため、スレッドローカルストレージ（TLS）の共有による競合、ファイバーローカルストレージ（FLS）の複雑さ、ブロッキングI/Oによる全体停止など多くの難点があるためです。さらに、複数プロセッサ上での並列実行ができず、協調マルチタスクに縛られます。特別な理由がない限り、Windowsカーネルのスケジューラに任せて通常のスレッドを使用するのが最善です。</p></blockquote>

<h4>ユーザーモードスケジューリング（UMS）</h4>
<p><strong>ユーザーモードスケジューリング（UMS）</strong> は、64ビット版Windowsでのみサポートされている、ファイバーの利点を活かしつつ欠点を大幅に解消した高度な実行機構です。UMSスレッドはカーネル側にも独立したスレッド状態を持っているため、<strong>カーネルから可視</strong>であり、ブロッキングシステムコールを発行したりリソース競合を適切に処理できます。</p>
<p>2つ以上のUMSスレッドがユーザーモードで処理を行っている間は、カーネルスケジューラを介さずにユーザーモード内で極めて高速に実行権を切り替えることができます。カーネルから見れば「同じ1つのスレッドが走り続けている」ように見え、オーバーヘッドがありません。そして、UMSスレッドがカーネルに入る操作（システムコール等）を行うと、専用のカーネルスレッドへと切り替わります（ダイレクトコンテキストスイッチ）。複数プロセッサ上での真の並行動作には制約があるものの、単なる協調マルチタスクを超えたプリエンプティブなモデルを実現しています。</p>"""

pages_ja['page-37'] = r"""<p>スレッドはそれぞれ独立した実行コンテキストを持ちますが、<strong>同一プロセス内のすべてのスレッドは、そのプロセスの仮想アドレス空間および各種システムリソースを完全に共有</strong>しています。つまり、同一プロセス内の任意のスレッドは、プロセス内の全メモリに対して完全な読み書きアクセス権を持っています。</p>
<p>一方、あるプロセスのスレッドが他のプロセスのメモリ空間を誤って参照してしまうことは、仮想記憶の保護機構により原則として起こり得ません（共有メモリセクションを介して意図的にアドレス空間を共有している場合や、同一ユーザー権限を持つ別プロセスが <code>ReadProcessMemory</code> / <code>WriteProcessMemory</code> などのデバッグAPIを使用して意図的にアクセスする場合を除きます）。</p>

<p>仮想アドレス空間と1つ以上のスレッドに加え、各プロセスはセキュリティコンテキストと、オープンされた各種カーネルオブジェクト（ファイル、共有メモリ、ミューテックス、イベント、セマフォ等）へのハンドルテーブルを保持しています（図1-2）。</p>

<figure><img loading="lazy" width="395" height="224" src="assets/f24c68537f751eccd376f18a.webp" alt="プロセスとそのリソース"><figcaption>図1-2：プロセスとスレッド、および各種リソースの構造</figcaption></figure>

<p>プロセスのセキュリティ情報は <strong>アクセストークン</strong> というカーネルオブジェクトに格納されています。アクセストークンには、プロセスのユーザー識別情報、グループSID、特権一覧などが含まれます。既定ではスレッドは独自のトークンを持ちませんが、必要に応じてスレッド単位でアクセストークンを割り当てることができ、これによりクライアントユーザーの権限になりすまして処理を行う（インパーソネーション）ことが可能になります。</p>

<h3>ジョブ（Jobs）</h3>
<p>Windowsでは、プロセスをさらに大きな単位で統括管理するための <strong>ジョブオブジェクト（Job Object）</strong> という機構を提供しています。ジョブを使用すると、関連する複数のプロセスを1つのグループとしてまとめ上げ、グループ全体に対して共通の制限や属性を強制できます。</p>"""

pages_ja['page-38'] = r"""<p>ジョブオブジェクトが提供する代表的な制御機能には以下のようなものがあります：</p>
<ul>
  <li>グループ全体、またはプロセス単位での最大CPU使用時間の制限</li>
  <li>プロセス単位、またはジョブ全体のコミットメモリ（仮想メモリ）消費上限の設定</li>
  <li>プロセスの優先順位クラスの強制固定</li>
  <li>使用できるCPUコア（プロセッサアフィニティ）の制限</li>
  <li>UI制限（クリップボードアクセス、デスクトップ切り替え、ウィンドウ作成、システム終了の制限など）</li>
  <li>セキュリティ制限（特定トークンの強制、管理者特権の剥奪など）</li>
</ul>

<p>ジョブオブジェクトは、現代のWindowsにおいて極めて重要な役割を果たしています。例えば、ChromiumやEdgeなどのモダンWebブラウザは、タブやレンダリングプロセスを隔離・制限するためにジョブオブジェクトをフル活用しています。また、Windows 10 / Server 2016 で導入された <strong>Windows コンテナ（Docker support）</strong> のリソース分離基盤としてもジョブが中核で使われています。</p>

<blockquote><p><strong>注意：</strong> Process Explorer では、ジョブによって管理されているプロセスを茶色のハイライトで識別できます（Options → Configure Colors から有効化可能）。また、ジョブに属するプロセスのプロパティには「Job」タブが追加され、所属ジョブの詳細や課されている各種制限をリアルタイムで確認できます。</p></blockquote>

<p>プロセスとジョブの内部構造については第3章で、スレッドとスケジューリングアルゴリズムについては第4章で詳しく解説します。</p>

<h3>仮想メモリ（Virtual memory）</h3>
<p>Windowsは、フラット（線形）なアドレス空間に基づく <strong>仮想記憶（仮想メモリ）システム</strong> を実装しています。これにより、各プロセスにはまるで自分自身が巨大でプライベートな連続したメモリ空間を独占しているかのような錯覚（抽象化）が与えられます。仮想メモリが提供する論理的なメモリ配置は、背後にある物理RAMの実際の配置とは全く異なっていても構いません。プログラムの実行時、CPUのメモリ管理ユニット（MMU）とOSのメモリマネージャーが協調し、仮想アドレスを物理アドレスへと動的に変換（マッピング）します（図1-3）。</p>

<figure><img loading="lazy" width="422" height="268" src="assets/d2aa3e460e2059344a6d3331.webp" alt="仮想メモリの物理マッピング"><figcaption>図1-3：仮想アドレス空間から物理メモリへのマッピング</figcaption></figure>"""

pages_ja['page-39'] = r"""<p>仮想アドレス空間の大きさは、ハードウェアアーキテクチャ（32ビットか64ビットか）によって劇的に異なります。</p>
<ul>
  <li><strong>32ビット x86 システム</strong>：仮想アドレス空間の理論上の最大値は 4 GB です。既定では、Windowsはこの空間を綺麗に半分に分割し、下位 2 GB（<code>0x00000000</code> 〜 <code>0x7FFFFFFF</code>）をユーザープロセス専用のプライベート空間に、上位 2 GB（<code>0x80000000</code> 〜 <code>0xFFFFFFFF</code>）をOS自身の保護されたシステム空間（カーネル空間）として割り当てます（図1-4）。下位半分のマッピングは実行中のプロセスが切り替わるたびにそのプロセスのものへと切り替わりますが、上位半分はどのプロセスの実行中であっても常に共通のOSシステムコードとデータが常駐します。※特別なブート設定（<code>/3GB</code>）と <code>IMAGE_FILE_LARGE_ADDRESS_AWARE</code> フラグを用いることで、ユーザー空間を 3 GB、カーネル空間を 1 GB に変更することも可能です。</li>
</ul>

<figure><img loading="lazy" width="452" height="267" src="assets/9e10eefcc1a1b743969e165a.webp" alt="32ビットの仮想アドレス空間レイアウト"><figcaption>図1-4：32ビット Windows における仮想アドレス空間の分割</figcaption></figure>

<ul>
  <li><strong>64ビット システム（x64 / ARM64）</strong>：64ビットCPUの理論上のアドレス空間は 16 EB（エクサバイト＝約160億GB）という途方もない広さですが、現在のハードウェアとOSの実装では、そのうち実用的な一部を使用しています。Windows 8.1 以前の64ビット版では各プロセスに 8 TB のユーザー空間と 8 TB のシステム空間（計 16 TB）が割り当てられていましたが、<strong>Windows 10 / Server 2016 ではこれが大幅に拡大され、プロセスごとに 128 TB のユーザー空間と 128 TB のシステム空間（計 256 TB）</strong> がサポートされています。これにより、大規模データベースやインメモリ処理がメモリ不足に陥る心配は事実上なくなりました。</li>
</ul>"""

pages_ja['page-40'] = r"""<p>図1-5に64ビットWindowsにおける仮想アドレス空間の分割レイアウトを示します。</p>

<figure><img loading="lazy" width="491" height="270" src="assets/10bacdc1a6d3377d64bbd49b.webp" alt="64ビットの仮想アドレス空間レイアウト"><figcaption>図1-5：64ビット Windows における広大な仮想アドレス空間</figcaption></figure>

<p>仮想メモリの詳細な動作原理、ページングファイル、ワーキングセット、アドレス変換テーブル（PTE）などの内部構造については、第5章「メモリ管理」で徹底的に解説します。</p>

<h3>カーネルモードとユーザーモード（Kernel mode vs. user mode）</h3>
<p>誤動作を起こしたユーザープログラムや悪意のあるソフトウェアが、OS全体を巻き込んでクラッシュさせたり他のプロセスのデータを不正に盗み取ったりすることを防ぐため、Windowsは現代のプロセッサがハードウェアレベルで提供する <strong>2つのプロセッサ実行モード</strong> を利用しています。</p>
<ul>
  <li><strong>ユーザーモード（User mode）</strong>：通常のアプリケーションが実行される制限付きモードです。ユーザーモードで動作するコードは、ハードウェアの制御レジスタへの直接アクセスや、他のプロセスのプライベートメモリへの自由なアクセスがCPUレベルで厳格に禁止されています。また、OSのシステム空間メモリにアクセスしようとすると直ちにハードウェア例外（アクセス違反、一般保護違反）が発生し、OSによってそのプロセスだけが安全に強制終了されます。</li>
  <li><strong>カーネルモード（Kernel mode / 特権モード）</strong>：オペレーティングシステムのコア部分（カーネル、エグゼクティブ、デバイスドライバ等）が実行される完全な特権モードです。カーネルモードコードはCPUのすべての特権命令を実行でき、システム全体の物理メモリやハードウェアデバイスへ無制限にアクセスできます。</li>
</ul>

<blockquote><p><strong>注意：</strong> x86およびx64プロセッサは、コードとデータの保護のために 0 から 3 までの 4 つの特権レベル（リング: Ring）を定義しています。Windowsはこのうち「Ring 0」をカーネルモードに、「Ring 3」をユーザーモードに割り当て、中間の Ring 1 と Ring 2 は使用していません。これは、ARMなど他のCPUアーキテクチャがハードウェア的に2つの特権レベルしか持たないため、OSの移植性と設計のシンプルさを保つための賢明な選択でした。</p></blockquote>"""

pages_ja['page-41'] = r"""<p>Windowsの各プロセスは独立したプライベートなユーザー空間を持っていますが、<strong>カーネルモードで動作するOSコードとデバイスドライバは、システム全体で単一の仮想アドレス空間（システム空間）を共有</strong>しています。</p>
<p>仮想メモリの各ページには、読み書きを行うためにCPUがどのモードにある必要があるかを示す属性ビット（U/Kビット）が付与されています。システム空間のページはカーネルモードからしかアクセスできませんが、ユーザー空間のページはユーザーモードとカーネルモードの双方からアクセス可能です。また、データ実行防止（DEP: Data Execution Prevention）が有効な場合、コードを含まないデータ領域のページには「実行不可（NX: No-Execute）」属性が付与され、バッファオーバーフロー攻撃などによる不正なシェルコード実行がCPUレベルで阻止されます。</p>

<p>ここで極めて重要な事実があります。それは、<strong>カーネルモードで動作するコンポーネント間には、メモリ保護の壁が存在しない</strong>ということです。いったんカーネルモードに入ると、サードパーティ製のデバイスドライバであってもOSの全メモリに完全な読み書きアクセス権限を持ち、Windowsのセキュリティ機構を自由に回避できてしまいます。したがって、カーネルモードで動作するコードにたった1つのバグ（バッファ破壊や不正ポインタ参照）があるだけで、システム全体がブルースクリーン（BSoD）となり停止してしまいます。</p>

<p>このリスクを低減するため、マイクロソフトは歴史的にカーネルドライバの品質向上策を強化し続けてきました：</p>
<ul>
  <li><strong>Driver Verifier</strong>：ドライバ開発者が潜在的なバッファオーバーランやメモリリークを検出するための強力なカーネル検証機能（第6章で解説）。</li>
  <li><strong>カーネルモードコード署名（KMCS）</strong>：64ビット版Windows 8.1以降、すべてのカーネルドライバは信頼された認証局による暗号署名が義務付けられ、未署名ドライバのロードは管理者権限であっても完全にブロックされます（テストモードでのみ例外許可）。</li>
  <li><strong>Windows 10 の SHA-2 EV署名・SysDev証明義務化</strong>：Windows 10 Anniversary Update（バージョン1607）以降、新規の全ドライバは SHA-2 拡張検証（EV）ハードウェア証明書での署名に加え、マイクロソフトの SysDev ポータルに提出して Microsoft による直接の電子署名（アテステーション署名）を受けることが必須となりました。</li>
  <li><strong>Windows Server 2016 の厳格な WHQL 認証</strong>：サーバー環境ではさらに厳格化され、単なるアテステーション署名ではロードできず、正式な Windows 認定試験（WHQL）に合格した署名入りドライバのみが実行を許されます。</li>
</ul>"""

pages_ja['page-42'] = r"""<p>また、エンタープライズ環境では後述する「Device Guard（コード整合性ポリシー）」を用いて、許可された特定の信頼ドライバ以外の一切のロードをハードウェア仮想化レベルで封じ込めることも可能です。</p>

<p>ユーザーアプリケーションがファイルアクセスなどのOS機能を呼び出す際、CPUはユーザーモードからカーネルモードへと切り替わります（システムコール）。例えば、Windows API の <code>ReadFile</code> を呼び出すと、最終的にファイルを読み取る内部カーネルルーチンを呼ぶ必要があります。このルーチンは保護されたシステムデータ構造を操作するため、カーネルモードで実行されなければなりません。プロセッサの特殊なトラップ命令（x86の <code>sysenter</code> や x64の <code>syscall</code>）が発行されると、CPUは特権モードに遷移してカーネル内のシステムディスパッチャへとジャンプします。そしてカーネル処理を終えると、再びユーザーモードに戻ってアプリケーションの実行を再開します。</p>

<blockquote><p><strong>注意：</strong> ユーザーモードからカーネルモードへの移行（およびその逆）は、スレッドスケジューリングには一切影響を与えません。<strong>モード遷移はコンテキストスイッチではありません</strong>。同一のスレッドが、単にCPUの特権レベルを切り替えながら処理を継続しているだけです。</p></blockquote>

<p>このように、通常のスレッドは稼働時間の一部をユーザーモードで、一部をカーネルモードで消費しています。特にグラフィックスやGUI処理の多くもカーネル（<code>win32k.sys</code>）で動作しているため、画面描画を多用するアプリは多くの時間をカーネルモードで過ごします。表1-3に、CPUの実行モード比率を計測するための代表的なパフォーマンスカウンタを示します。</p>

<p><strong>表1-3：モード関連のパフォーマンスカウンタ</strong></p>
<table style="width:100%;border-collapse:collapse;margin:1em 0;font-size:14px;">
<thead><tr style="border-bottom:2px solid var(--line);text-align:left;">
<th style="padding:6px;">オブジェクト：カウンタ</th><th style="padding:6px;">説明</th>
</tr></thead>
<tbody>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Processor: % Privileged Time</td><td style="padding:6px;">CPU（個別または全体）がカーネルモードで実行されていた時間の割合</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Processor: % User Time</td><td style="padding:6px;">CPU（個別または全体）がユーザーモードで実行されていた時間の割合</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Process: % Privileged Time</td><td style="padding:6px;">該当プロセスの全スレッドがカーネルモードで実行されていた時間の割合</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Process: % User Time</td><td style="padding:6px;">該当プロセスの全スレッドがユーザーモードで実行されていた時間の割合</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Thread: % Privileged Time</td><td style="padding:6px;">個別スレッドがカーネルモードで実行されていた時間の割合</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Thread: % User Time</td><td style="padding:6px;">個別スレッドがユーザーモードで実行されていた時間の割合</td></tr>
</tbody></table>"""

pages_ja['page-43'] = r"""<h4>実験：カーネルモード時間とユーザーモード時間の計測</h4>
<p>Windows付属の「パフォーマンス モニター」を使用すると、システムがカーネルモードとユーザーモードのどちらでどの程度時間を費やしているかを視覚的にリアルタイム監視できます：</p>
<ol>
  <li>スタートメニューを開き、「パフォーマンス モニター」（<code>perfmon</code>）と入力して起動する。</li>
  <li>左側のツリーで「モニタリング ツール → パフォーマンス モニター」を選択する。</li>
  <li>既定で表示されている折れ線グラフのカウンタを選択し、ツールバーの削除（×）ボタンまたは <code>Delete</code> キーを押して削除する。</li>
  <li>ツールバーの追加（＋）ボタンをクリックする。</li>
  <li>一覧から <strong>Processor</strong> を展開し、<code>Ctrl</code> キーを押しながら <strong>% Privileged Time</strong> と <strong>% User Time</strong> の両方を選択して「追加」をクリックし、「OK」を押す。</li>
  <li>コマンドプロンプトを開き、<code>dir \\%computername%\c$ /s</code> などを実行して大量のファイル走査（高負荷なファイルシステムI/O）を発生させてみる。</li>
</ol>

<figure><img loading="lazy" width="591" height="426" src="assets/18f36dad166b8a4bd7fe543a.webp" alt="パフォーマンスモニターの実行画面"><figcaption>図：カーネルモード時間とユーザーモード時間の監視グラフ</figcaption></figure>

<p>ディスクやネットワークの激しいI/O中には、カーネルモード時間（Privileged Time）が跳ね上がることがグラフから確認できます。</p>"""

pages_ja['page-44'] = r"""<p>タスクマネージャーでも簡単に確認できます。「パフォーマンス」タブを開き、CPUグラフを右クリックして <strong>カーネル時間を表示する</strong> にチェックを入れると、全体のCPU使用率のうちカーネルモードが占める割合が濃い青色で重ねて表示されるようになります。</p>

<h3>ハイパーバイザー（Hypervisor）</h3>
<p>近年のWindowsにおける最大のアーキテクチャ的進化の1つが、<strong>Hyper-V ハイパーバイザー</strong> のOS基盤への深い統合です。ハイパーバイザーはCPUのハードウェア仮想化支援機能（Intel VT-x や AMD-V）を利用して、CPUの特権リングである Ring 0 よりもさらに下層の <strong>Ring -1（VMX rootモード）</strong> で稼働する超低レベルの仮想化ソフトウェア層です。</p>

<p>かつてハイパーバイザーは、サーバー上で複数の仮想マシン（VM）を動かすためだけの機能でした。しかし Windows 10 および Windows Server 2016 において、マイクロソフトはハイパーバイザーを <strong>ホストOS自体の防衛機構</strong> として活用する革新的なアーキテクチャ「<strong>VBS（仮想化ベースのセキュリティ: Virtualization-Based Security）</strong>」を導入しました。</p>

<p>VBSが有効なシステムでは、たとえWindowsカーネル自体であってもハードウェアの最高特権ではなく、ハイパーバイザー上で動作する1つの仮想マシン（VTL 0: 通常ワールド）に格下げされます。そして、それとは完全にハードウェアレベルでメモリが隔絶された、よりセキュアな隔離空間（VTL 1: セキュアワールド）が作成され、そこに <strong>セキュアカーネル（Secure Kernel）</strong> や分離型LSASS（Credential Guard）が配置されます。</p>

<p>これにより、万一悪意のあるカーネルドライバによって通常カーネル（Ring 0）が完全に侵害されたとしても、攻撃者はハイパーバイザーによって保護されたセキュアワールドのメモリを盗み見ることも改ざんすることもできません。Pass-the-Hash攻撃で狙われるユーザーの資格情報（パスワードハッシュ）や暗号キーはセキュアワールド内で厳重に防衛され、システムの根本的な乗っ取りが阻止されます（詳細は第7章およびPart 2 第9章で詳解）。</p>"""

pages_ja['page-45'] = r"""<h3>ファームウェア（Firmware）</h3>
<p>Windowsが起動する際、最初にハードウェアの初期化を行いブートローダーを呼び出すのがファームウェアです。従来のレガシーな PC では <strong>BIOS</strong>（Basic Input/Output System）が使われていましたが、現代のWindows PCでは完全に <strong>UEFI</strong>（Unified Extensible Firmware Interface）へと移行しています。</p>
<p>UEFIは、従来の16ビットリアルモードで動作していたBIOSと異なり、64ビットネイティブコードで動作し、2.2 TBを超えるGPTディスクからのブートをサポートします。さらにWindowsのセキュリティにおいて不可欠な <strong>セキュアブート（Secure Boot）</strong> を実現します。セキュアブートは、電源投入直後からファームウェア自身、Windowsブートマネージャー、そしてWindowsカーネルに至るまでのすべてのブートコードのデジタル署名を検証し、ルートキットなどの不正コードがOS起動前に潜り込むのを物理的に防ぎます。</p>

<h3>ターミナルサービスとマルチセッション</h3>
<p>Windowsは、複数のユーザーが同時にマシンにログオンして独立したデスクトップ環境を安全に利用できるように設計された <strong>マルチセッション（ターミナルサービス / リモートデスクトップサービス）</strong> アーキテクチャを内蔵しています。</p>
<p>システム内の各プロセスは、特定の「<strong>セッション（Session）</strong>」に所属しています。セッションとは、特定の対話型ログオンユーザーに紐づくすべてのリソース（ウィンドウステーション、デスクトップ、クリップボード、プロセス群）を包括する論理的な分離境界です。</p>
<ul>
  <li><strong>セッション 0</strong>：OSのシステムサービスやバックグラウンドタスク専用の非対話型セッションです。Windows Vista 以降、セキュリティ強化のためユーザーログオンセッションから完全に隔離され、ユーザーと対話するUIを表示することは禁止されています（セッション0分離）。</li>
  <li><strong>セッション 1 以降</strong>：対話型ユーザーがログオンするたびに新しく作成されるセッションです。コンソールからログオンしたユーザーも、リモートデスクトップ（RDP）経由で接続したユーザーも、それぞれ独立したセッションIDが割り振られます。</li>
</ul>

<p>Windows Server では、リモートデスクトップサービス（RDS）の役割を有効化することで、数十人から数百人のユーザーが単一のサーバー上で同時にそれぞれのセッションでアプリケーションを実行できます。</p>"""
# Chapter 1: Pages 46 - 61

pages_ja['page-46'] = r"""<p>マルチセッション環境において、セッション間でのリソース衝突を防ぎつつ、GDIやUSERなどのGUIサブシステムメモリを効率的に管理するため、Windowsは「<strong>セッション空間（Session Space）</strong>」と呼ばれるセッション固有のカーネル仮想アドレス領域を使用しています（第5章「メモリ管理」で詳解）。</p>

<h3>オブジェクトとハンドル（Objects and handles）</h3>
<p>Windowsエグゼクティブ（OSカーネル上位層）の中核設計思想の1つが「<strong>オブジェクト指向設計</strong>」です。Windowsは、ファイル、ディレクトリ、プロセス、スレッド、セクション（共有メモリ）、ミューテックス、セマフォ、イベント、アクセストークン、レジストリキーなど、管理すべきあらゆるシステムリソースを <strong>エグゼクティブオブジェクト（カーネルオブジェクト）</strong> としてカプセル化して統一的に扱います。</p>

<p>ユーザーモードアプリケーションは、これらのカーネルオブジェクトのメモリ上の生のアドレス（ポインタ）を直接触ることはできません。代わりに、安全な不透明ポインタである「<strong>ハンドル（Handle）</strong>」を介してオブジェクトを間接的に参照・操作します。</p>
<p>プロセスがオブジェクトを作成またはオープンすると（例: <code>CreateFile</code> や <code>OpenProcess</code>）、OSはプロセスの「プロセスハンドルテーブル」に新しいエントリを登録し、そのインデックスであるハンドル値を返します。ハンドルはプロセスごとに固有のテーブルのインデックスであるため、プロセスAのハンドル値 <code>0x24</code> とプロセスBのハンドル値 <code>0x24</code> は通常全く別のオブジェクトを指しています。</p>"""

pages_ja['page-47'] = r"""<p>オブジェクトとハンドルによる抽象化は、Windowsに以下のような計り知れない利点をもたらしています：</p>
<ul>
  <li><strong>安全なリソース保護</strong>：すべてのカーネルデータ構造はユーザーモードから直接書き換えられることがなく、整合性が保たれます。</li>
  <li><strong>統一されたアクセス制御とセキュリティ</strong>：ハンドルをオープンする際、OSのセキュリティサブシステムが「要求されたアクセス権（読み取り、書き込み、終了など）」を検証し、許可された権限フラグをハンドルに記録します。以降の操作ではハンドルに付与された権限のみが許可されます。</li>
  <li><strong>厳格な生存期間（リファレンスカウント）管理</strong>：オブジェクトは「ハンドル参照カウント」と「カーネルポインタ参照カウント」の2種類の参照カウントを保持します。すべてのハンドルがクローズされ（<code>CloseHandle</code>）、カーネル内からの参照もゼロになった瞬間、オブジェクトは自動的かつ安全にメモリから解放され、リソースリークを防ぎます。</li>
  <li><strong>名前空間の統一管理</strong>：オブジェクトマネージャーは階層構造を持つ名前空間（オブジェクトディレクトリ）を保持しており、プロセス間で名前を指定してオブジェクトを共有（例: <code>\BaseNamedObjects</code> 内の共有ミューテックス）できます。</li>
</ul>

<h3>セキュリティ（Security）</h3>
<p>Windowsは誕生当初から、政府機関の厳格なセキュリティ評価基準（C2クラス、後のコモンクライテリア）を満たすよう設計された包括的なセキュリティアーキテクチャを備えています。</p>
<p>Windowsセキュリティモデルの中核を担うのが <strong>SRM（セキュリティリファレンスモニター: Security Reference Monitor）</strong> と呼ばれるカーネルコンポーネントです。SRMは、スレッドがオブジェクトへのハンドルをオープンしようとするたびに、以下の2つの情報を照合してアクセスを許可するか拒否するかを判定します：</p>
<ul>
  <li><strong>主体のセキュリティ属性（アクセストークン）</strong>：スレッドまたはプロセスに紐づくユーザーSID、所属グループSID、特権一覧。</li>
  <li><strong>客体のセキュリティ属性（セキュリティ記述子: Security Descriptor）</strong>：オブジェクトに付与された所有者情報、および <strong>DACL（随意アクセスコントロールリスト）</strong>。DACLには「誰に（どのSIDに）どのようなアクセス権を許可・拒否するか」を定義したエントリ（ACE）が並んでいます。</li>
</ul>"""

pages_ja['page-48'] = r"""<p>Windows Vista 以降では、従来のユーザー単位・グループ単位のアクセス制御に加え、強力な新セキュリティレイヤーが追加されてきました：</p>
<ul>
  <li><strong>整合性レベル（Mandatory Integrity Control: MIC）</strong>：すべてのプロセスとオブジェクトに「低」「中」「高」「システム」などの整合性レベルを割り当て、低整合性のプロセス（サンドボックス化されたブラウザ等）が高整合性のリソースを変更することを禁止する仕組み。</li>
  <li><strong>ユーザーアカウント制御（UAC）</strong>：管理者が通常業務を行う際は管理者特権を分離した「制限付きトークン」でアプリを実行し、システム変更時のみ明示的な昇格プロンプトを表示する機構。</li>
  <li><strong>AppContainer</strong>：Windowsストアアプリ（UWP）やEdgeブラウザで使用される強力な軽量サンドボックス。ネットワークアクセスやローカルファイルへのアクセスが細分化された「機能（Capabilities）」ごとに極めて厳密に制限されます。</li>
</ul>

<h3>レジストリ（Registry）</h3>
<p><strong>レジストリ</strong> は、WindowsのOS設定、ハードウェア構成、デバイスドライバ設定、インストール済みアプリケーションの構成情報などを一元管理する中央階層型データベースです。</p>
<p>レジストリはファイルシステムのフォルダ構造に似た階層構造を持ち、フォルダに相当する「<strong>キー（Key）</strong>」と、ファイルに相当する「<strong>値（Value）</strong>」から構成されます。ルートには <code>HKEY_LOCAL_MACHINE</code>（マシン全体の設定）、<code>HKEY_CURRENT_USER</code>（ログオンユーザーの設定）などの定義済みキーが存在します。ディスク上では「ハイブ（Hive）」と呼ばれるバイナリファイル（<code>SYSTEM</code>、<code>SOFTWARE</code>、<code>SAM</code>、<code>NTUSER.DAT</code> など）として保存されています。</p>
<p>第7章およびPart 2 第8章で、レジストリのメモリ内データ構造やトランザクション機構（KTM連携）などを詳解します。</p>"""

pages_ja['page-49'] = r"""<h3>Unicode</h3>
<p>Windows NT系のアーキテクチャは、その誕生当初から内部のすべての文字列処理を <strong>Unicode（UTF-16LE）</strong> で行うように設計されています。これにより、単一のグローバルなバイナリで世界中のあらゆる言語・文字セットをネイティブにサポートできます。</p>

<p>後方互換性のため、文字列を受け取る Windows API 関数の多くには「<strong>A版（ANSI / 従来の文字コード版）</strong>」と「<strong>W版（Wide character / Unicode版）</strong>」の2種類が用意されています。例えば、ファイルをオープンする <code>CreateFile</code> は関数そのものではなく、コンパイル時にマクロによって <code>CreateFileA</code> または <code>CreateFileW</code> へと展開されます：</p>
<pre>#ifdef UNICODE
#define CreateFile CreateFileW
#else
#define CreateFile CreateFileA
#endif</pre>

<p>重要な点として、<strong>Windowsカーネルおよびコアサブシステムは内部でUnicodeしか扱いません</strong>。もしアプリケーションが ANSI 版の <code>CreateFileA</code> を呼び出した場合、システムはユーザーモードの <code>Kernel32.dll</code> 内で文字列を ANSI から Unicode（UTF-16）へと一時変換した上で、内部の Unicode 版システムルーチンを呼び出します。そのため、Unicode 版（W版）のAPIを直接呼び出すほうが変換オーバーヘッドがなく、文字化けの危険もありません。</p>"""

pages_ja['page-50'] = r"""<h4>実験：サブシステムDLLのエクスポート関数の確認（Dependency Walker）</h4>
<p>Dependency Walker ツールを使用して、Windowsの基幹DLLが ANSI 版と Unicode 版の関数ペアをエクスポートしている様子を観察してみましょう：</p>
<ol>
  <li>Dependency Walker（<code>depends.exe</code>）をダウンロードして起動します。</li>
  <li>メニューの <strong>File → Open</strong> から、<code>C:\Windows\System32\kernel32.dll</code> を開きます。</li>
  <li>画面右上の「エクスポート関数一覧」で関数名をクリックしてアルファベット順にソートします。</li>
  <li><code>CreateFileA</code> を探すと、そのすぐ下に <code>CreateFileW</code> が並んでいることが確認できます。</li>
</ol>

<figure><img loading="lazy" width="534" height="215" src="assets/679198a6f2d754df12793781.webp" alt="Dependency Walker のエクスポート関数一覧"><figcaption>図：kernel32.dll における A版 / W版関数のエクスポート</figcaption></figure>

<p><code>CreateFileMappingA/W</code>、<code>CreateProcessA/W</code> など、文字列を引数に取るほぼすべてのAPIが二重に定義されていることが確認できます。</p>"""

pages_ja['page-51'] = r"""<h3>Windows 内部の深掘り（Digging into Windows internals）</h3>
<p>本書で解説する内部構造の多くは、Windowsのソースコード解析やマイクロソフトのカーネル開発者との議論に基づいています。しかし、読者の皆様がそれらをただ鵜呑みにする必要はありません。Windowsには、内部で何が起きているかを読者自身の手で暴き、視覚的に確かめるための強力なツール群が用意されています。</p>
<p>本書の随所に登場する「実験（EXPERIMENT）」は、実際のツールを操作しながらOS内部の挙動を検証できるように設計されています。表1-4に本書で主に使用する代表的なツールの一覧を示します。</p>

<p><strong>表1-4：Windows内部調査ツールの概要</strong></p>
<table style="width:100%;border-collapse:collapse;margin:1em 0;font-size:14px;">
<thead><tr style="border-bottom:2px solid var(--line);text-align:left;">
<th style="padding:6px;">ツール名</th><th style="padding:6px;">実行ファイル</th><th style="padding:6px;">提供元</th><th style="padding:6px;">主な用途</th>
</tr></thead>
<tbody>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Autoruns</td><td style="padding:6px;">Autoruns.exe</td><td style="padding:6px;">Sysinternals</td><td style="padding:6px;">自動起動プログラム・拡張モジュールの完全調査</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">AccessChk</td><td style="padding:6px;">Accesschk.exe</td><td style="padding:6px;">Sysinternals</td><td style="padding:6px;">ファイル・キー・サービスへのアクセス権検証</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Dependency Walker</td><td style="padding:6px;">Depends.exe</td><td style="padding:6px;">外部ツール</td><td style="padding:6px;">DLLのインポート/エクスポート関数の解析</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Gflags</td><td style="padding:6px;">Gflags.exe</td><td style="padding:6px;">Debugging Tools</td><td style="padding:6px;">カーネル/プロセスのグローバルフラグ設定</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Handle</td><td style="padding:6px;">Handle.exe</td><td style="padding:6px;">Sysinternals</td><td style="padding:6px;">オープン中のハンドル検索（CLI）</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">WinObj</td><td style="padding:6px;">Winobj.exe</td><td style="padding:6px;">Sysinternals</td><td style="padding:6px;">オブジェクトマネージャー名前空間の探索</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Performance Monitor</td><td style="padding:6px;">Perfmon.exe</td><td style="padding:6px;">Windows標準</td><td style="padding:6px;">パフォーマンスカウンタの計測・記録</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Process Explorer</td><td style="padding:6px;">Procexp.exe</td><td style="padding:6px;">Sysinternals</td><td style="padding:6px;">プロセス・スレッド・ハンドルの究極の調査</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">Process Monitor</td><td style="padding:6px;">Procmon.exe</td><td style="padding:6px;">Sysinternals</td><td style="padding:6px;">ファイル・レジストリ・プロセスのリアルタイム追跡</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">WinDbg / KD</td><td style="padding:6px;">Windbg.exe / Kd.exe</td><td style="padding:6px;">Debugging Tools</td><td style="padding:6px;">カーネルおよびユーザーモードの深層デバッグ</td></tr>
<tr style="border-bottom:1px solid var(--line);"><td style="padding:6px;">LiveKd</td><td style="padding:6px;">Livekd.exe</td><td style="padding:6px;">Sysinternals</td><td style="padding:6px;">稼働中マシン上でのライブカーネルデバッグ</td></tr>
</tbody></table>"""

pages_ja['page-52'] = r"""<h3>パフォーマンスモニターとリソースモニター</h3>
<p>Windows標準の「<strong>パフォーマンス モニター（Performance Monitor / perfmon）</strong>」は、システム全体の詳細な稼働状態を監視するための最も包括的なツールです。数百ものOSオブジェクトに対して数千のカウンタが用意されており、CPU消費、メモリの各プール使用量、ディスクI/O、ネットワーク転送量などをリアルタイムにグラフ化・ロギングできます。</p>

<p>また、日常的な監視により適した「<strong>リソース モニター（Resource Monitor / resmon）</strong>」も標準搭載されています。CPU、メモリ、ディスク、ネットワークの4大リソースの状況を直感的に把握できます（図）。</p>

<figure><img loading="lazy" width="619" height="416" src="assets/d0822ba0355595e9d123a751.webp" alt="リソースモニターの画面"><figcaption>図：リソースモニターによるリソース活動の監視</figcaption></figure>

<p>リソースモニターでは、特定のプロセスにチェックを入れることで、そのプロセスに関連するディスクアクセスファイル名、オープンしているネットワーク接続（通信先IP、ポート番号、パケット損失率）、ロードしているモジュールなどをワンクリックで絞り込み表示できます。</p>"""

pages_ja['page-53'] = r"""<h3>カーネルデバッグ（Kernel debugging）</h3>
<p><strong>カーネルデバッグ</strong> は、Windowsの内部を極限まで深く解き明かすための最強の調査手法です。メモリ上に展開された未公開カーネルデータ構造の生の内容を検査したり、カーネル内の処理フローを追跡したりできます。</p>

<h4>カーネルデバッグ用シンボル（Symbols）</h4>
<p>デバッガーを真に役立つものにするためには、「<strong>シンボルファイル（.PDB）</strong>」が不可欠です。シンボルファイルには、関数名、グローバル変数名、データ構造体のメンバ名とオフセット配置情報が記録されています。製品版のWindowsバイナリ（<code>ntoskrnl.exe</code> など）には実行速度とファイルサイズ削減のためシンボル名は含まれていませんが、マイクロソフトは公式の <strong>シンボルサーバー</strong> を無償公開しており、デバッガーからインターネット経由でオンデマンド取得できるようにしています。</p>
<p>デバッガーで以下のシンボルパスを設定するだけで、必要なシンボルが自動取得されます：</p>
<p><code>srv*c:\symbols*http://msdl.microsoft.com/download/symbols</code></p>

<h4>Debugging Tools for Windows</h4>
<p>Windows SDK に同梱される「Debugging Tools for Windows」には、以下のデバッガーが含まれています：</p>
<ul>
  <li><strong>cdb / ntsd</strong>：コンソールUIベースのユーザーモードデバッガー</li>
  <li><strong>kd</strong>：コンソールUIベースのカーネルデバッガー</li>
  <li><strong>WinDbg</strong>：GUIを備えた、ユーザーモードおよびカーネルモード両用の高機能デバッガー</li>
</ul>"""

pages_ja['page-54'] = r"""<p>カーネルデバッグには主に以下の接続形態があります：</p>
<ul>
  <li><strong>リモートカーネルデバッグ（2台接続）</strong>：デバッグ対象のマシン（ターゲット）と、デバッガーを動かすマシン（ホスト）をネットワーク（KDNET）、USB、1394、シリアルケーブル等で接続します。ブレークポイントを設定してカーネルの実行を完全に一時停止させたり、ステップ実行することが可能です。</li>
  <li><strong>ローカルカーネルデバッグ（Local Kernel Debugging）</strong>：1台のマシン上で、自身が稼働中のカーネルをその場で直接参照する手法です（管理者権限のWinDbgから「File → Kernel Debug → Local」）。ブレークポイントによる停止はできませんが、稼働中システムのあらゆるカーネル構造体を読み取って検査できます。図1-6に64ビットWindows 10でのローカルカーネルデバッグ画面を示します。</li>
</ul>

<figure><img loading="lazy" width="551" height="304" src="assets/34550846eb33cad587b68ec3.webp" alt="ローカルカーネルデバッグ画面"><figcaption>図1-6：WinDbg によるローカルカーネルデバッグの実行画面</figcaption></figure>

<p>カーネルデバッガー内では、エクスクラメーションマーク（<code>!</code>）で始まる多数のデバッガー拡張コマンド（例: <code>!process</code>, <code>!thread</code>, <code>!pool</code>, <code>!vm</code>）が利用できるほか、構造体を表示する <code>dt</code>（Display Type）コマンドにより、数千に及ぶカーネルデータ構造のメンバ配置を詳細にダンプできます。</p>"""

pages_ja['page-55'] = r"""<h4>実験：カーネル構造体の型情報の表示（dt nt!_*）</h4>
<p>カーネルデバッガー（WinDbg や LiveKd）で <code>dt nt!_*</code> と入力すると、カーネルシンボルに含まれる膨大な構造体の一覧が表示されます：</p>
<pre>lkd> dt nt!_*
ntkrnlmp!_KSYSTEM_TIME
ntkrnlmp!_NT_PRODUCT_TYPE
ntkrnlmp!_KUSER_SHARED_DATA
ntkrnlmp!_ULARGE_INTEGER
ntkrnlmp!_TP_POOL
ntkrnlmp!_TEB
...</pre>

<p>ワイルドカードを使って特定の構造体を検索することも可能です。例えば割り込みオブジェクトの構造体を探すには <code>dt nt!_*interrupt*</code> と入力します：</p>
<pre>lkd> dt nt!_*interrupt*
ntkrnlmp!_KINTERRUPT_MODE
ntkrnlmp!_KINTERRUPT
ntkrnlmp!_INTERRUPT_CONNECTION_DATA
...</pre>

<p>構造体名が分かれば、<code>dt nt!_KINTERRUPT</code> のように入力することで、構造体内部のメンバ名、データ型、オフセットが綺麗に整形されて表示されます：</p>
<pre>lkd> dt nt!_KINTERRUPT
+0x000 Type             : Int2B
+0x002 Size             : Int2B
+0x008 InterruptListEntry : _LIST_ENTRY
+0x018 ServiceRoutine   : Ptr64     unsigned char
+0x028 MessageIndex     : Uint4B
+0x030 ServiceContext   : Ptr64 Void
+0x038 SpinLock         : Uint8B
+0x050 DispatchAddress  : Ptr64     void
+0x058 Vector           : Uint4B
+0x05c Irql             : UChar
...</pre>"""

pages_ja['page-56'] = r"""<h4>LiveKd ツール</h4>
<p>Sysinternals の <strong>LiveKd</strong> は、OSをデバッグモードで起動していなくても、稼働中のWindows上で即座に WinDbg や kd によるカーネルデバッグを可能にする画期的な無償ツールです。</p>
<p>LiveKd は稼働中システムの仮想メモリのスナップショット（仮想的なクラッシュダンプ）を透過的に生成してデバッガーに提示するため、マシンの再起動や2台接続の機材を用意することなく、手軽に安全にカーネル内部の生データを調査できます。<code>livekd -w</code> と実行すれば GUI の WinDbg が起動します。</p>

<h3>Windows Software Development Kit (Windows SDK)</h3>
<p><strong>Windows SDK</strong> は、Windowsアプリケーションを開発・デバッグするための公式開発キットです。マイクロソフトの公式サイトから無償でダウンロードできます。</p>
<p>Windows内部構造を探究する上での Windows SDK の最大の価値は、<strong>公式のC言語ヘッダーファイル群</strong>（<code>Include</code> フォルダ）と、付属する各種調査ツール（<code>Bin</code> フォルダ）にあります。APIの定義や各種フラグ定数の正確な値を確認する上で一級のリソースとなります。</p>

<h3>Windows Driver Kit (WDK)</h3>
<p><strong>Windows Driver Kit (WDK)</strong> は、デバイスドライバの開発者向けキットであり、Windows内部構造情報のまさに宝庫です。公式ドキュメント（カーネルモードドライバアーキテクチャ設計ガイド等）には、通常公開されないカーネルの動作原理や同期オブジェクトの振る舞いが詳細に解説されています。</p>
<p>さらに WDK に含まれるヘッダーファイル（特に <code>ntddk.h</code>, <code>ntifs.h</code>, <code>wdm.h</code>）には、カーネルが使用する内部データ構造体やシステムルーチンのプロトタイプが多数定義されており、カーネルデバッガーで構造体を調査する際のリファレンスとして極めて有用です。</p>"""

pages_ja['page-57'] = r"""<h3>Sysinternals ツール群</h3>
<p>本書で紹介する実験の多くは、<strong>Windows Sysinternals</strong>（<a href="https://technet.microsoft.com/sysinternals" target="_blank" rel="noopener">sysinternals.com</a>）の無償ツールを使用しています。著者の1人である Mark Russinovich が中心となって開発したこれらのツールは、世界中のWindows管理者やセキュリティ技術者のデファクトスタンダードとなっています。</p>
<p>最も著名な Process Explorer や Process Monitor のほか、Autoruns、Handle、WinObj など、OS内部の可視化において比類なき威力を発揮します。ツール群は頻繁にアップデートされているため、常に最新版をダウンロードして活用してください。</p>

<h3>まとめ（Conclusion）</h3>
<p>本章では、本書全体を通じて基礎となる Windows の主要なアーキテクチャ概念と基本用語（API、プロセス、スレッド、仮想メモリ、実行モード、オブジェクト、セキュリティ等）を整理し、内部構造を解明するための強力な調査ツール群の基本操作を紹介しました。</p>
<p>これでWindowsの内部世界を探究する準備が整いました。続く第2章では、システム全体の全体像と各コアコンポーネントがどのように結合しているかを解き明かす「システムアーキテクチャ」の旅へと進みましょう。</p>"""
