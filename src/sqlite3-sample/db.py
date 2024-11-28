import os
import sqlite3


base_dir = os.path.dirname(__file__)
database = os.path.join(base_dir, 'data.sqlite')

print('0. コネクションの接続', end="\n\n")

# 接続
conn = sqlite3.connect(database)
cur = conn.cursor()

print('1. すでに対象テーブルが存在すれば削除する', end="\n\n")

# テーブル削除SQL
drop_sql = """
    DROP TABLE IF EXISTS items;
"""

cur.execute(drop_sql)

print('2. テーブル作成', end="\n\n")

# テーブル作成SQL
create_sql = """
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name STRING UNIQUE NOT NULL,
        price INTEGER NOT NULL
    )
"""

cur.execute(create_sql)

print('3. データ登録', end="\n\n")

# データ登録SQL
insert_sql = """
    INSERT INTO items (item_name, price)
    VALUES (?, ?)
"""

insert_data_list = [
    ('団子', 100),
    ('肉まん', 150),
    ('どら焼き', 200)
]

cur.executemany(insert_sql, insert_data_list)
conn.commit()

print('4. 全件取得', end="\n\n")

# データ参照（全件）SQL
select_all_sql = """
    SELECT * FROM items
"""

cur.execute(select_all_sql)
data = cur.fetchall()

print(data, end="\n\n")

print('5. 1件取得', end="\n\n")

# データ参照（1件）SQL
select_one_sql = """
    SELECT * FROM items
    WHERE item_id = ?
"""

id = 3
cur.execute(select_one_sql, (id,))
data = cur.fetchone()

print(data, end="\n\n")

print('6. データ更新', end="\n\n")

# データ更新SQL
update_sql = """
    UPDATE items SET price= ?
    WHERE item_id= ?
"""

price = 500
id = 1
cur.execute(update_sql, (price, id))
conn.commit()

print('確認のため１件取得', end="\n\n")

cur.execute(select_one_sql, (id,))
data = cur.fetchone()

print(data, end="\n\n")

print('7. データ削除', end="\n\n")

# データ削除SQL
delete_sql = """
    DELETE FROM items
    WHERE item_id= ?
"""

id = 3
cur.execute(delete_sql, (id,))
conn.commit()

print('確認のため全件取得', end="\n\n")

cur.execute(select_all_sql)
data = cur.fetchall()

print(data, end="\n\n")

print('8. コネクションを閉じる')

conn.close()
