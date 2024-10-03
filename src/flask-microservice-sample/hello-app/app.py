from flask import Flask, render_template, request
import requests

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# 認証サービスのエンドポイント
LOGIN_URL = "http://localhost:5001/login"
INFO_URL = "http://localhost:5001/info"

# 認証処理
def authenticate(id, password):
    login_data = {
        "id": id,
        "password": password,
    }
    # 認証サービス実行
    response = requests.post(LOGIN_URL, json=login_data)

    # トークンを返す、失敗時は何もしない
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        pass

# ==================================================
# ルーティング
# ==================================================
@app.route("/", methods=["GET", "POST"])
def shwo_login():
    if request.method == "POST":
        # 入力データ取得
        id = request.form.get("id")
        password = request.form.get("password")
        
        # 認証サーバーからトークン取得
        access_token = authenticate(id, password)
        
        # トークンがない場合は認証失敗
        if access_token:
            # ヘッダーにアクセストークンを含める
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(INFO_URL, headers=headers)
                        
            # ユーザー情報取得判定
            if response.status_code == 200:
                user_info = response.json()
                # テンプレート表示    
                return render_template('index.html', user=user_info)
            else:
                return '<h1 style="color: red;">Error：アクセストークン処理に失敗しました</h1>', 401
        else:
            return '<h1 style="color: red;">Error：認証サービスの認証に失敗しました</h1>', 401
    # GETの時テンプレート表示
    return render_template("login.html")
