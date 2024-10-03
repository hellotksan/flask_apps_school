from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email

# ==================================================
# Formクラス
# ==================================================
# 入力クラス
class InputForm(FlaskForm):
    name = StringField('名前：', validators=[DataRequired('必須入力です')])
    email = EmailField('メールアドレス：',
                       validators=[Email('メールアドレスのフォーマットではありません')])
    submit = SubmitField('送信')