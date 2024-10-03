from flask import Blueprint, render_template

# ==================================================
# Blueprintの定義
# ==================================================
two_bp = Blueprint('two_app', __name__, url_prefix='/two')

# ==================================================
# ルーティング
# ==================================================
@two_bp.route('/')
def show_template():
    return render_template('two/index.html')