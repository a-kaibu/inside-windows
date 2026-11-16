# inside-windows

Windows Internals Part 1 / Part 2 のブラウザーリーダー。

公開先: https://a-kaibu.github.io/inside-windows/

- `index.html`: 2冊への入口
- `part1.html`, `part2.html`: 目次、本文検索、文字サイズ変更、原本ページ表示
- `assets/`: 外部ファイルに分離したWebP画像。画像は必要になったときに読み込みます。

PDFの自動変換のため、表やコードの配置は原本ページ表示で確認してください。
書籍の著作権は各権利者に帰属します。

`main` へのpushでGitHub ActionsがGitHub Pagesへデプロイします。

各巻の読書位置はlocalStorageへ個別に保存され、同じブラウザーで再び開くと復元されます。本文のブロックと相対位置を保存するため、画面幅の変更にも対応します。URLで別のページを指定した場合は、その指定を優先します。
