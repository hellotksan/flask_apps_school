from flask import Flask
from flask_migrate import Migrate
# ▼▼▼ リスト 11-3の追加 ▼▼▼
from models import db, User
from flask_login import LoginManager
# ▲▲▲ リスト 11-3の追加 ▲▲▲
# ▼▼▼ リスト 12-11の追加 ▼▼▼
from auth.views import auth_bp
from memo.views import memo_bp
from wiki.views import wiki_bp     # 14-5追記
# ▲▲▲ リスト 12-11の追加 ▲▲▲

# ==================================================
# Flask
# ==================================================
app = Flask(__name__)
# 設定ファイル読み込み
app.config.from_object("config.Config")
# dbとFlaskとの紐づけ
db.init_app(app)
# マイグレーションとの紐づけ（Flaskとdb）
migrate = Migrate(app, db)
# ▼▼▼ リスト 11-3の追加 ▼▼▼
# LoginManagerインスタンス
login_manager = LoginManager()
# LoginManagerとFlaskとの紐づけ
login_manager.init_app(app)
# ▼▼▼ リスト 11-9の追加 ▼▼▼
# ログインが必要なページにアクセスしようとしたときに表示されるメッセージを変更
login_manager.login_message = "認証していません：ログインしてください"
# ▲▲▲ リスト 11-9の追加 ▲▲▲
# 未認証のユーザーがアクセスしようとした際に
# ▼▼▼ リスト 12-11の修正 ▼▼▼
# リダイレクトされる関数名を設定する(ブループリント対応)
login_manager.login_view = 'auth.login'
# blueprintをアプリケーションに登録
app.register_blueprint(auth_bp)
app.register_blueprint(memo_bp)
app.register_blueprint(wiki_bp)     # 14-5追記
# ▲▲▲ リスト 12-11の修正 ▲▲▲

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# ▲▲▲ リスト 11-3の追加 ▲▲▲

# viewsのインポート
from views import *

# ==================================================
# 実行
# ==================================================
if __name__ == "__main__":
    app.run()