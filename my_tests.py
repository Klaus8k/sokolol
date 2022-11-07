import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

# data = [(33,23),(44,43),(44,43)]
# cur.executemany('insert into test_table values(?,?)', data)
# con.commit()


print(cur.execute('select * from test_table').fetchall())
con.close()




# print(dir(con)).0