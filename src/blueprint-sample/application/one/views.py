from flask import Blueprint, render_template

# ==================================================
# Blueprintの定義
# ==================================================
one_bp = Blueprint('one_app', __name__, url_prefix='/one')

# ==================================================
# ルーティング
# ==================================================
@one_bp.route('/')
def show_template():
    return render_template('one/index.html')
