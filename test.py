import sqlite3 as sl
con=sl.connect('test.db')
cursor = con.cursor()


cursor.execute("CREATE TABLE db (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, speed FLOAT, gust FLOAT, direction FLOAT, pressure FLOAT, temperature FLOAT, timestamp STRING)")
               
speed, gust, direction, pressure, temperature, timestamp = 5.5, 5.6, 33, 1020, 23, "kovas"
print(speed, gust, direction, pressure, temperature, timestamp)

cursor.executemany("insert into db values (?,?,?,?,?,?)", [speed, gust, direction, pressure, temperature, timestamp])
print("aaa")

