from flask import Flask

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# ==================================================
# ルーティング
# ==================================================
# コンバーターなし
@app.route('/dynamic/<value>')
def dynamic_default(value):
    print(f'型:{type(value)}, 値:{value}')
    return f'<h1>渡された値は「{value}」です</h1>'

# コンバーターあり
@app.route('/dynamic2/<int:number>')
def dynamic_converter(number):
    print(f'型:{type(number)}, 値:{number}')
    return f'<h1>渡された値は「{number}」です</h1>'

# コンバーターあり複数値渡し
@app.route('/dynamic3/<value>/<int:number>')
def dynamic_converter_multiple(value, number):
    print(f'型:{type(value)}, 値:{value}')
    print(f'型:{type(number)}, 値:{number}')
    return f'<h1>渡された値は「{value}と{number}」です</h1>'
# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run()