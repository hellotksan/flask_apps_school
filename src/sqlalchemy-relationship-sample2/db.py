import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# ==================================================
# DBファイル作成
# ==================================================
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
# データベースエンジンを作成
db_engine = create_engine(database, echo=True)
Base = declarative_base()

# ▼▼▼ リスト 6-7 修正 ▼▼▼
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
    # リレーション
    shops = relationship("Shop", secondary="stocks", back_populates="items")
    
# 店舗
class Shop(Base):
    # テーブル名
    __tablename__ = 'shops'
    # 店舗ID
    shop_id = Column(Integer, primary_key=True)
    # 店舗名
    shop_name = Column(String(255), nullable=False, unique=True)
    # リレーション
    items = relationship("Item", secondary="stocks", back_populates="shops")
    
# 在庫
class Stock(Base):
    # テーブル名
    __tablename__ = 'stocks'
    # 店舗ID
    shop_id = Column(Integer, ForeignKey('shops.shop_id'), primary_key=True)
    # 商品ID
    item_id = Column(Integer, ForeignKey('items.item_id'), primary_key=True)
    # 在庫
    stock = Column(Integer)
# ▲▲▲ リスト 6-7 修正 ▲▲▲

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

# ▼▼▼ リスト 6-8 追加 ▼▼▼
print('（３）データ参照：実行')
print('■：Shopの参照')
target_shop = session.query(Shop).filter_by(shop_id=1).first()
print(f'店舗名：{target_shop.shop_name}')
print('■：リレーションから商品の参照')
# target_shopが持つ商品情報を取得する
for item in target_shop.items:
    # itemに対応する在庫情報を取得する
    stock = session.query(Stock).filter_by(shop_id=target_shop.shop_id, item_id=item.item_id).first()
    # 在庫数を表示する
    print(f"商品名：{item.item_name} -> 在庫数: {stock.stock}")
# ▲▲▲ リスト 6-8 追加 ▲▲▲
