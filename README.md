# Flask Sample Apps

## プロジェクトについて

このリポジトリは、Flask の学習を目的として個人的に作成したものです。サンプルコードは以下の書籍に基づいていますので、利用時は参照元のライセンスをよく確認してください。

- 参照元リンク: [https://gihyo.jp/assets/files/book/2023/978-4-297-13641-3/download/Sample.zip](https://gihyo.jp/assets/files/book/2023/978-4-297-13641-3/download/Sample.zip)

## Python モジュールのインストール

必要なモジュールは次のコマンドでインストールしてください。

```bash
pip install -r requirements.txt
```

## 仮想環境での実行

仮想環境での実行を推奨します。手順については、[docs/how_to_run_on_venv.md](docs/how_to_run_on_venv.md)を参照してください。

## src フォルダの内容

このプロジェクトには、以下のようなサンプルが含まれています。

Chapter 1.

Chapter 2. **Flask に触れてみよう**

- Hello World with Flask

  - [src/hello-sample](src/hello-sample)

- ルーティングについて

  - デコレーターの例: [src/decorator_sample.py](src/decorator_sample.py)
  - 基本的なルーティング: [src/routing-sample](src/routing-sample)

- 動的ルーティング

  - [src/dynamicrouting-sample](src/dynamicrouting-sample)

Chapter 3. **jinja2 に触れてみよう**

- [src/templates-sample](src/templates-sample)

Chapter 4. **フィルターとエラーハンドリングに触れてみよう**

- [src/templates-sample](src/templates-sample)

Chapter 5. **Form に触れてみよう**

- フォームの使用方法

  - [src/form-sample](src/form-sample)

- WTForms

  - [src/wtforms-sample](src/wtforms-sample)

- Flask-WTF

  - [src/flask-wtf-sample](src/flask-wtf-sample)

Chapter 6. **データベースに触れてみよう**

- データベースの作成について

  - [src/sqlite3-sample](src/sqlite3-sample)

- ORM

  - [src/sqlalchemy-sample](src/sqlalchemy-sample)

- 結合を使おう

  - [src/sqlalchemy-join-sample](src/sqlalchemy-join-sample)

Chapter 7. **Flask でデータベースを使おう**

- Flask-SQLAlchemy を使おう

  - [src/flask-sqlalchemy-sample](src/flask-sqlalchemy-sample)

- Flask-Migrate を使おう

  - [src/flask-migrate-sample](src/flask-migrate-sample)

---
