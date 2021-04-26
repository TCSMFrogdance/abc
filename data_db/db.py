import sqlite3

conn = sqlite3.connect('C:/Users\TUAN_ANH/Desktop/Desktop/abc/data_db/ABC.db')
cur = conn.cursor()
cur.execute("SELECT sales.StoreID, sales.Sales FROM sales INNER JOIN stores ON sales.StoreID=stores.StoreID")

print(cur.fetchall())

