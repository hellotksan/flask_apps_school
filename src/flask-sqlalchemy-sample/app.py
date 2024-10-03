import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# ==================================================
# Flaskに対する設定
# ==================================================
import os
# 乱数を設定
app.config['SECRET_KEY'] = os.urandom(24)
# DBファイルの設定
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ★db変数を使用してSQLAlchemyを操作できる
db = SQLAlchemy(app)

#==================================================
# モデル
#==================================================
# 課題
class Task(db.Model):
    # テーブル名
    __tablename__ = 'tasks'
    
    # 課題ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 内容
    content = db.Column(db.String(200), nullable=False)

    # 表示用
    def __str__(self):
        return f'課題ID：{self.id} 内容：{self.content}'

# ==================================================
# DB作成
# ==================================================
def init_db():
    with app.app_context():
        print('（１）テーブルを削除してから作成')
        db.drop_all()
        db.create_all()

        # データ作成
        print('（２）データ登録：実行')
        task01 = Task(content='風呂掃除')
        task02 = Task(content='洗濯')
        task03 = Task(content='買い物')
        db.session.add_all([task01, task02, task03])
        db.session.commit()

# ==================================================
# CRUD操作
# ==================================================
# 登録
def insert():
    with app.app_context():
        print('========== 1件登録 ==========')
        task04 = Task(content='請求書作成')
        db.session.add(task04)
        db.session.commit()
        print('登録 =>', task04) 

# 参照（全件）
def select_all():
    print('========== 全件取得 ==========')
    with app.app_context():
        tasks = Task.query.all()
        for task in tasks:
            print(task)

# 参照（１件）
def select_filter_pk(pk):
    print('========== １件取得 ==========')
    with app.app_context():
        target = Task.query.filter_by(id = pk).first()
        print('更新後 =>', target)
        
# 更新
def update(pk):
    print('========== 更新実行 ==========')
    with app.app_context():
        target = Task.query.filter_by(id = pk).first()
        print('更新前 =>', target)
        target.content = '課題を変更'
        db.session.add(target)
        db.session.commit()  

# 削除
def delete(pk):
    print('========== 削除処理 ==========')
    with app.app_context():
        target = Task.query.filter_by(id = pk).first()
        db.session.delete(target)
        db.session.commit()
        print('削除 =>', target)
        
# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    init_db()               # DB初期化
    insert()                # 1件登録処理
    update(1)               # 更新処理
    select_filter_pk(1)     # 1件取得（更新後の値を取得）
    delete(2)               # 削除処理
    select_all()            # 全件取得
