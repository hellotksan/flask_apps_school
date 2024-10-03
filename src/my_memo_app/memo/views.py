from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Memo
from forms import MemoForm
from flask_login import login_required, current_user  # <= リスト13-2追加

# memoのBlueprint
memo_bp = Blueprint('memo', __name__, url_prefix='/memo')

# ==================================================
# ルーティング
# ==================================================
# 一覧
@memo_bp.route("/")
@login_required
def index():
    # メモ全件取得
    memos = Memo.query.filter_by(user_id=current_user.id).all() # <= リスト13-2 変更
    # 画面遷移
    return render_template("memo/index.html", memos=memos)


# 登録（Form使用）
@memo_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    # Formインスタンス生成
    form = MemoForm()
    if form.validate_on_submit():
        # データ入力取得
        title = form.title.data
        content = form.content.data
        # 登録処理
        memo = Memo(title=title, content=content, user_id=current_user.id)  # <= 13-3変更
        db.session.add(memo)
        db.session.commit()
        # フラッシュメッセージ
        flash("登録しました")          
        # 画面遷移
        return redirect(url_for("memo.index"))
    # GET時
    # 画面遷移
    return render_template("memo/create_form.html", form=form)

# 更新（Form使用）
@memo_bp.route("/update/<int:memo_id>", methods=["GET", "POST"])
@login_required
def update(memo_id):
    # データベースからmemo_idに一致するメモを取得し、
    # 見つからない場合は404エラーを表示
    target_data = Memo.query.filter_by(id=memo_id, user_id=current_user.id).first_or_404()  # <= 13-4変更
    # Formに入れ替え
    form = MemoForm(obj=target_data)
    
    if request.method == 'POST' and form.validate():
        # 変更処理
        target_data.title = form.title.data
        target_data.content = form.content.data
        db.session.merge(target_data)
        db.session.commit()
        # フラッシュメッセージ
        flash("変更しました")        
        # 画面遷移
        return redirect(url_for("memo.index"))
    # GET時
    # 画面遷移
    return render_template("memo/update_form.html", form=form, edit_id = target_data.id)

# 削除
@memo_bp.route("/delete/<int:memo_id>")
@login_required
def delete(memo_id):
    # データベースからmemo_idに一致するメモを取得し、
    # 見つからない場合は404エラーを表示
    memo = Memo.query.filter_by(id=memo_id, user_id=current_user.id).first_or_404()  # <= 13-5変更
    # 削除処理
    db.session.delete(memo)
    db.session.commit()
    # フラッシュメッセージ
    flash("削除しました")
    # 画面遷移
    return redirect(url_for("memo.index"))

# wiki結果反映
@memo_bp.route('/create_from_search', methods=['POST'])
@login_required
def create_from_search():
    # 入力値の取得
    title = request.form['title']
    content = request.form['content']
    new_memo = Memo(title=title, content=content, user_id=current_user.id)
    # 追加処理
    db.session.add(new_memo)
    db.session.commit()
    # フラッシュメッセージ
    flash("wikiからデータ登録しました")          
    # 画面遷移
    return redirect(url_for("memo.index"))
