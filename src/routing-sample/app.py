from flask import Flask


app = Flask(__name__)


# TOPページ
@app.route('/')
def index():
    return '<h1>Topページ</h1>'


# 一覧
@app.route('/list')
def item_list():
    return '<h1>商品一覧ページ</h1>'


# 詳細
@app.route('/detail')
def item_detail():
    return '<h1>商品詳細ページ</h1>'


if __name__ == '__main__':
    app.run()
