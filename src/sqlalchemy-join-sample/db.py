import os
from sqlalchemy import create_engine, Column, Integer, String
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
# 商品
class Item(Base):
    # テーブル名
    __tablename__ = 'items'
    # 商品ID
    item_id = Column(Integer, primary_key=True)
    # 商品名
    item_name = Column(String(255), nullable=False, unique=True)
    # 価格
    price = Column(Integer, nullable=False)

# 店舗
class Shop(Base):
    # テーブル名
    __tablename__ = 'shops'
    # 店舗ID
    shop_id = Column(Integer, primary_key=True)
    # 店舗名
    shop_name = Column(String(255), nullable=False, unique=True)

# 在庫
class Stock(Base):
    # テーブル名
    __tablename__ = 'stocks'
    # 店舗ID
    shop_id = Column(Integer, primary_key=True)
    # 商品ID
    item_id = Column(Integer, primary_key=True)
    # 在庫
    stock = Column(Integer)

# ==================================================
# テーブル操作
# ==================================================
print('（１）テーブルを削除してから作成')
Base.metadata.drop_all(db_engine)
Base.metadata.create_all(db_engine)

# セッションの生成
session_maker = sessionmaker(bind=db_engine)
session = session_maker()

# データ作成
print('（２）データ登録：実行')
# 商品
item01 = Item(item_id=1, item_name='団子', price=100)
item02 = Item(item_id=2, item_name='肉まん', price=150)
item03 = Item(item_id=3, item_name='どら焼き', price=200)
item04 = Item(item_id=4, item_name='コンビーフ', price=500)
session.add_all([item01, item02, item03, item04])
session.commit()
# 店
shop01 = Shop(shop_id=1, shop_name='東京店')
shop02 = Shop(shop_id=2, shop_name='大阪店')
session.add_all([shop01, shop02])
session.commit()
# 在庫
stock01 = Stock(shop_id=1, item_id=1, stock=10)
stock02 = Stock(shop_id=1, item_id=2, stock=20)
stock03 = Stock(shop_id=1, item_id=3, stock=30)
stock04 = Stock(shop_id=2, item_id=1, stock=100)
stock05 = Stock(shop_id=2, item_id=2, stock=200)
stock06 = Stock(shop_id=2, item_id=3, stock=300)
session.add_all([stock01, stock02, stock03, stock04, stock05, stock06])
session.commit()

print('（３）データ参照：実行')
print('■：内部結合')
join_3tables_all = session.query(Shop, Item.item_name, Stock.stock).join\
    (Stock, Shop.shop_id == Stock.shop_id).join\
    (Item, Item.item_id == Stock.item_id).all()

for row in join_3tables_all:
    print(f'店：{row.Shop.shop_name} -> 商品名：{row.item_name} -> 在庫数：{row.stock}')

print('■' * 100)

print('■：外部結合')
outerjoin_2tables_all = session.query(Item, Stock.stock).outerjoin\
    (Stock, Item.item_id == Stock.item_id).all()

for row in outerjoin_2tables_all:
    print(f'商品名：{row.Item.item_name} -> 在庫数：{row.stock}')

# ▼▼▼ リスト 6-6 追加 ▼▼▼
# filter
target_A = session.query(Item).filter(Item.item_id == 1).filter(Item.price == 100).first() 
print(f'商品ID：{target_A.item_id} -> 商品名：{target_A.item_name} -> 金額：{target_A.price}')
# filter_by
target_B = session.query(Item).filter_by(item_id=1, price=100).first() 
print(f'商品ID：{target_B.item_id} -> 商品名：{target_B.item_name} -> 金額：{target_B.price}')
# ▲▲▲ リスト 6-6 追加 ▲▲▲