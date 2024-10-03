from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# JWT設定
# 任意の秘密キーを設定
app.config["JWT_SECRET_KEY"] = "secret-key"
# JWTとアプリケーションの紐づけ
jwt = JWTManager(app)

# ユーザーデータのサンプル
users = {
    "user1": {
        "password": "pass1",
        'name': 'マイクロ太郎',
        'email': 'microtarou@example.com',
        'phone': '080-1234-5678'
    },
    "user2": {
        "password": "pass2",
        'name': 'サービス次郎',
        'email': 'servicejirou@example.com',
        'phone': '080-9876-5432'
    },
}

# ==================================================
# ルーティング
# ==================================================
# ログイン
@app.route("/login", methods=["POST"])
def login():
    # データ取得
    user_id = request.json.get("id", None)
    password = request.json.get("password", None)

    # 認証チェック
    if user_id not in users or users[user_id]["password"] != password:
        return jsonify({"error": "認証失敗：無効な資格情報です"}), 401

    # トークン取得
    access_token = create_access_token(identity=users[user_id])
    # トークンをJSONで返却
    return jsonify(access_token=access_token)

# ユーザー情報取得
@app.route("/info", methods=["GET"])
@jwt_required()
def git_info(): 
    # get_jwt_identity()関数を使用して、ユーザー情報取得
    current_user = get_jwt_identity()
    print(current_user)
    return jsonify(current_user)

# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run()
