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

1. **Flask でハローワールドを作成する**

   - [src/hello-sample](src/hello-sample)

2. **ルーティングについて学ぶ**

   - デコレーターの例: [src/decorator_sample.py](src/decorator_sample.py)
   - 基本的なルーティング: [src/routing-sample](src/routing-sample)

3. **動的ルーティングについて学ぶ**

   - [src/dynamicrouting-sample](src/dynamicrouting-sample)

4. **jinja2 テンプレートの利用**

   - フィルターやエラーハンドリングの例: [src/templates-sample](src/templates-sample)

5. **フォームの使用方法**

   - [src/form-sample](src/form-sample)

6. **WTForms を使ってみよう**
   - [src/wtforms-sample](src/wtforms-sample)

---
