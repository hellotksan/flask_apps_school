from flask import Flask


# インスタンス生成
app = Flask(__name__)


# ルーティング
@app.route('/')
def hello_world():
    return '<h1>Hello Flask!</h1>'
