from forms import InputForm
import os
from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


# 入力
@app.route('/', methods=['GET', 'POST'])
def input():
    form = InputForm()
    # POST
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('output'))
    # GET
    if 'name' in session:
        form.name.data = session['name']
    if 'email' in session:
        form.email.data = session['email']
    # GETリクエストの場合、またはフォームの値がバリデーションを通過しなかった場合
    return render_template('input.html', form=form)


# 出力
@app.route('/output')
def output():
    return render_template('output.html')


if __name__ == '__main__':
    app.run()
