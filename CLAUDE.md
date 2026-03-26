# my-first-repo

GitHub学習用リポジトリ。Claude Codeの使い方を実践的に学ぶためのプロジェクト。

## ファイル構成

- `hello.py` — 練習用スクリプト（Hello GitHub!を出力）
- `todo.py` — CLIのTODOアプリ（tasks.jsonにデータ保存）
- `index.html` — ブラウザ用TODOアプリ（localStorageにデータ保存）

## 開発サーバーの起動

```bash
python3 -m http.server 8000
```

起動後、http://localhost:8000 でブラウザ用TODOアプリを確認できる。

## todo.py の使い方

```bash
python todo.py add <タスク名>   # タスクを追加
python todo.py complete <ID>    # タスクを完了
python todo.py list             # タスク一覧表示
```
