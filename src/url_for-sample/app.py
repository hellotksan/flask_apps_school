from flask import Flask, url_for

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# ==================================================
# ルーティング
# ==================================================
@app.route('/')
def show_index():
    return 'Indexページ'

@app.route('/hello/')
@app.route('/hello/<name>')
def show_hello(name=None):
    return f'Hello, {name}'

# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('show_index'))
        print(url_for('show_hello'))
        print(url_for('show_hello', name='tarou'))