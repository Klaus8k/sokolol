import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

# data = [(33,23),(44,43),(44,43)]
# cur.executemany('insert into test_table values(?,?)', data)
# con.commit()

def show_test_table():
    print(cur.execute('select * from test_table').fetchall())


show_test_table()
# fff



# print(dir(con)).0