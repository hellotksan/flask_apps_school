from wtforms import Form
from wtforms.fields import (
    StringField, IntegerField, PasswordField, DateField, 
    RadioField, SelectField, BooleanField, TextAreaField,
    EmailField, SubmitField
)
# 使用するvalidatorをインポート
# 【リスト5.14】 で「ValidationError」を追加
from wtforms.validators import (
    DataRequired, EqualTo, Length, NumberRange, Email, ValidationError
)
# ==================================================
# Formクラス
# ==================================================
# ユーザー情報クラス
class UserInfoForm(Form):
    # 名前：文字列入力
    name = StringField('名前: ', validators=[DataRequired('名前は必須入力です')], 
                    render_kw={"placeholder": "（例）山田 太郎"})
    # 年齢：整数値入力
    age = IntegerField('年齢: ', validators=[NumberRange(18, 100, '入力範囲は18歳から100歳です')],
                    default=20)
    # パスワード：パスワード入力
    password = PasswordField('パスワード: ',
                    validators=[Length(1, 10,
                        'パスワードの長さは1文字以上10文字以内です'), 
        EqualTo('confirm_password', 'パスワードが一致しません')])
    # 確認用：パスワード入力
    confirm_password = PasswordField('パスワード確認: ')
    # Email：メールアドレス入力
    email = EmailField('メールアドレス：',
                    validators=[Email('メールアドレスのフォーマットではありません')])
    # 生年月日：日付入力
    birthday = DateField('生年月日: ', validators=[DataRequired('生年月日は必須入力です')], 
                        format="%Y-%m-%d", render_kw={"placeholder": "yyyy/mm/dd"})
    # 性別：ラジオボタン
    gender = RadioField(
        '性別: ', choices=[('man', '男性'), ('woman', '女性')], default='man'
    )
    # 出身地域：セレクトボックス
    area = SelectField('出身地域: ', choices=[('east', '東日本'), ('west', '西日本')])
    # 既婚：真偽値入力
    is_married = BooleanField('既婚？:')
    # メッセージ：複数行テキスト
    note = TextAreaField('備考: ')
    # ボタン
    submit = SubmitField('送信')

    # ▼▼▼ 【リスト5.14】 ▼▼▼ 
    # カスタムバリデータ
    # 英数字と記号が含まれているかチェックする
    def validate_password(self, password):
        if not (any(c.isalpha() for c in password.data) and \
            any(c.isdigit() for c in password.data) and \
            any(c in '!@#$%^&*()' for c in password.data)):
            raise ValidationError('パスワードには【英数字と記号：!@#$%^&*()】を含める必要があります')
    # ▲▲▲ 【リスト5.14】 ▲▲▲ 
