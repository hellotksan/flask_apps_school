# メモ

## 仮想環境の作成

```bash
python -m venv .venv
```

## pythonモジュールのインストール

```bash
pip install -r requirements.txt
```

## 実行ポリシーの変更

1. **管理者権限で PowerShell を開く**

   - 「スタート」メニューから「PowerShell」と検索し、`Windows PowerShell` または `Windows PowerShell (管理者)` を右クリックして「管理者として実行」を選択します。

2. **実行ポリシーを確認**
   現在の実行ポリシーを確認するには、以下のコマンドを実行します。

   ```powershell
   Get-ExecutionPolicy -List
   ```

3. **実行ポリシーを変更する**
   次のコマンドを実行して、スクリプトの実行を許可します。`-Scope CurrentUser`オプションを使って現在のユーザーのみに設定を適用します。

   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

   - これで、ローカルに保存されたスクリプト（例えば仮想環境のアクティベーションスクリプト）が実行可能になります。

4. **アクティベート**

```powershell
.venv\Scripts\activate
```

### 仮想環境のディアクティベート

仮想環境の使用を終了したい場合は以下のコマンドで仮想環境を抜けることができます。

```powershell
deactivate
```

## サーバ立ち上げ

```bash
cd src/hello-sample
flask --app app run
```