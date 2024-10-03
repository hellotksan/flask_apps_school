from flask import Flask, request

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# ==================================================
# ルーティング
# ==================================================
# GETでデータ取得
@app.route('/get')
def do_get():
    name = request.args.get('name')
    return f'ハロー、 {name}さん！'

# POSTでデータ取得
@app.route('/', methods=['GET', 'POST'])
def do_get_post():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'こんにちは、 {name}さん！'
    return '''
        <h2>POSTで送信</h2>
        <form method="post">
            名前：<input type="text" name="name">
            <input type="submit" value="送信">
        </form>
    '''

# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run()