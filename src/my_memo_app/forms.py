# ▼▼▼ リスト 11-2の修正 ▼▼▼
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError
from models import Memo, User
# ▲▲▲ リスト 11-2の修正 ▲▲▲

# ==================================================
# Formクラス
# ==================================================
# メモ用入力クラス
class MemoForm(FlaskForm):
    # タイトル
    title = StringField('タイトル：', validators=[DataRequired('タイトルは必須入力です'), 
                            Length(max=10, message='10文字以下で入力してください')])
    # 内容
    content = TextAreaField('内容：')
    # ボタン
    submit = SubmitField('送信')

    # カスタムバリデータ
    def validate_title(self, title):
        # StringFieldオブジェクトではなく、その中のデータ（文字列）をクエリに渡す必要があるため
        # 以下のようにtitle.dataを使用して、StringFieldから実際の文字列データを取得する
        memo = Memo.query.filter_by(title=title.data).first()
        if memo:
            raise ValidationError(f"タイトル '{title.data}' は既に存在します。\
                                  別のタイトルを入力してください。")

# ▼▼▼ リスト 11-2の追加 ▼▼▼
# ログイン用入力クラス
class LoginForm(FlaskForm):
    username = StringField('ユーザー名：', 
                           validators=[DataRequired('ユーザー名は必須入力です')])
    # パスワード：パスワード入力
    password = PasswordField('パスワード: ',
                             validators=[Length(4, 10,
                                    'パスワードの長さは4文字以上10文字以内です')])
    # ボタン
    submit = SubmitField('ログイン')
    
    # カスタムバリデータ
    # 英数字と記号が含まれているかチェックする
    def validate_password(self, password):
        if not (any(c.isalpha() for c in password.data) and \
            any(c.isdigit() for c in password.data) and \
            any(c in '!@#$%^&*()' for c in password.data)):
            raise ValidationError('パスワードには【英数字と記号：!@#$%^&*()】を含める必要があります')

# サインアップ用入力クラス
class SignUpForm(LoginForm):
    # ボタン
    submit = SubmitField('サインアップ')

    # カスタムバリデータ
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('そのユーザー名は既に使用されています')
# ▲▲▲ リスト 11-2の追加 ▲▲▲

# ▼▼▼ リスト 14-6の追加 ▼▼▼
# Wiki用入力クラス
class WikiForm(FlaskForm):
    # タイトル
    keyword = StringField('検索ワード：', render_kw={"placeholder": "入力してください"})
    # ボタン
    submit = SubmitField('Wiki検索')
# ▲▲▲ リスト 14-6の追加 ▲▲▲
