from flask import Blueprint, render_template, redirect, url_for, flash
from models import db, User
from forms import LoginForm, SignUpForm
from flask_login import login_user, logout_user, login_required

# authのBlueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# ==================================================
# ルーティング
# ==================================================
# ログイン（Form使用）
@auth_bp.route("/", methods=["GET", "POST"])
def login():
    # Formインスタンス生成
    form = LoginForm()
    if form.validate_on_submit():
        # データ入力取得
        username = form.username.data
        password = form.password.data
        # 対象User取得
        user = User.query.filter_by(username=username).first()
        # 認証判定
        if user is not None and user.check_password(password):
            # 成功
            # 引数として渡されたuserオブジェクトを使用して、ユーザーをログイン状態にする
            login_user(user)
            # 画面遷移
            return redirect(url_for("memo.index"))
        # 失敗
        flash("認証不備です")
    # GET時
    # 画面遷移
    return render_template("auth/login_form.html", form=form)

# ログアウト
@auth_bp.route("/logout")
@login_required
def logout():
    # 現在ログインしているユーザーをログアウトする
    logout_user()
    # フラッシュメッセージ
    flash("ログアウトしました")   
    # 画面遷移
    return redirect(url_for("auth.login"))

# サインアップ（Form使用）
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    # Formインスタンス生成
    form = SignUpForm()
    if form.validate_on_submit():
        # データ入力取得
        username = form.username.data
        password = form.password.data
        # モデルを生成
        user = User(username=username)
        # パスワードハッシュ化
        user.set_password(password)
        # 登録処理
        db.session.add(user)
        db.session.commit()
        # フラッシュメッセージ
        flash("ユーザー登録しました")   
        # 画面遷移 
        return redirect(url_for("auth.login"))
    # GET時
    # 画面遷移
    return render_template("auth/register_form.html", form=form)
