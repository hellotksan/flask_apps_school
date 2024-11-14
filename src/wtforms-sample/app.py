from flask import Flask, render_template, request
from forms import UserInfoForm


# インスタンス生成
app = Flask(__name__)


# ルーティング
# ユーザー情報：入力
@app.route('/', methods=['GET', 'POST'])
def show_enter():
    # フォームの作成
    form = UserInfoForm(request.form)
    # POST
    if request.method == "POST" and form.validate():
        return render_template('result.html', form=form)
    # POST以外と「form.validate()がfalse」
    return render_template('enter2.html', form=form)


if __name__ == '__main__':
    app.run()
