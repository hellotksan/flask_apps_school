from flask import Flask, g, request

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# ==================================================
# ルーティング
# ==================================================
@app.before_request
def before_request():
    g.user = get_user()

@app.route('/')
def do_hello():
    user = g.user
    return f'こんにちは、 {user}'

@app.route('/morning')
def do_morning():
    user = g.user
    return f'おはようございます、 {user}'

@app.route('/evening')
def do_evening():
    user = g.user
    return f'こんばんは、 {user}'

# ユーザー情報を取得する処理
def get_user():
    user_info = {
        "name": "G太郎",
        "age": 33,
        "email": "g.tarou@example.com"
    }
    return user_info

# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run()
