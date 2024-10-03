import os
from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ==================================================
# DBファイル作成
# ==================================================
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
# データベースエンジンを作成
db_engine = create_engine(database, echo=True)
Base = declarative_base()

# ==================================================
# モデル
# ==================================================
class Item(Base):
    # テーブル名
    __tablename__ = 'items'
    # 商品ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 商品名
    name = Column(String(255), nullable=False, unique=True)
    # 価格
    price = Column(Integer, nullable=False)

    # コンストラクタ
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 表示用関数
    def __str__(self):
        return f"Item(商品ID：{self.id}, 商品名：{self.name}, 価格：{self.price})"

# ==================================================
# テーブル操作
# ==================================================
print('（１）テーブルを作成')
Base.metadata.create_all(db_engine)

# セッションの生成
session_maker = sessionmaker(bind=db_engine)
session = session_maker()

print('（２）データ削除：実行')
session.query(Item).delete()
session.commit()

# データ作成
print('（３）データ登録：実行')
item01 = Item('団子', 100)
item02 = Item('肉まん', 150)
item03 = Item('どら焼き', 200)
session.add_all([item01, item02, item03])
session.commit()

print('（４）データ参照：実行')
item_all_list = session.query(Item).order_by(Item.id).all()
for row in item_all_list:
    print(row)

print('（５）データ更新１件：実行')
target_item = session.query(Item).filter(Item.id==3).first()
target_item.price = 500
session.commit()
target_item = session.query(Item).filter(Item.id==3).first()
print('確認用', target_item)

print('（６）データ更新複数件：実行')
target_item_list = session.query(Item).filter(or_(Item.id==1, Item.id==2)).all()
for target_item in target_item_list:
    target_item.price = 999
session.commit()
item_all_list = session.query(Item).order_by(Item.id).all()
print('確認')
for row in item_all_list:
    print(row)