import os
import sqlite3

# ==================================================
# DBファイル作成
# ==================================================
base_dir = os.path.dirname(__file__)
database = os.path.join(base_dir, 'data.sqlite')

# ==================================================
# SQL
# ==================================================
# 接続
conn = sqlite3.connect(database)
print('▼▼▼▼▼▼▼▼▼▼ コネクションの接続 ▼▼▼▼▼▼▼▼▼▼')
print()
# カーソル
cur = conn.cursor()
# テーブル削除SQL
drop_sql = """
    DROP TABLE IF EXISTS items;
"""
cur.execute(drop_sql)
print('（１）対象テーブルがあれば削除')
# テーブル作成SQL
create_sql = """
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        item_name STRING UNIQUE NOT NULL, 
        price INTEGER NOT NULL)
    """
cur.execute(create_sql)
print('（２）テーブル作成')
# データ登録SQL
insert_sql = """
    INSERT INTO items (item_name, price) VALUES (?, ?)
    """
insert_data_list = [
    ('団子', 100), ('肉まん', 150), ('どら焼き', 200)
]
cur.executemany(insert_sql, insert_data_list)
conn.commit()
print('（３）データ登録：実行')
# データ参照（全件）SQL
select_all_sql = """
    SELECT * FROM items
    """
cur.execute(select_all_sql)
print('（４）---------- 全件取得：実行 ----------')
data = cur.fetchall()
print(data)
# データ参照（1件）SQL
select_one_sql = """
    SELECT * FROM items WHERE item_id = ?
    """
id = 3
cur.execute(select_one_sql, (id,))
print('（５）---------- １件取得：実行 ----------')
data = cur.fetchone()
print(data)
# データ更新SQL
update_sql = """
    UPDATE items SET price=? WHERE item_id= ?
    """
price = 500
id = 1
cur.execute(update_sql, (price, id))
print('（６）---------- データ更新：実行 ----------')
conn.commit()
cur.execute(select_one_sql, (id,))
data = cur.fetchone()
print('確認のため１件取得：実行', data)
# データ削除SQL
delete_sql = """
    DELETE FROM items WHERE item_id= ?
    """
id = 3
cur.execute(delete_sql, (id,))
conn.commit()
print('（７）---------- データ削除：実行 ----------')
cur.execute(select_all_sql)
data = cur.fetchall()
print('確認のため全件取得：実行', data)
# 閉じる
conn.close()
print()
print('▲▲▲▲▲▲▲▲▲▲ コネクションを閉じる ▲▲▲▲▲▲▲▲▲▲')
