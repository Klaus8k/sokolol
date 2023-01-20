# # ------ Пример работы с sql-lite
# import sqlite3 

# con = sqlite3.connect('db.sqlite3')
# cur = con.cursor()

# # data = [(33,23),(44,43),(44,43)]
# # cur.executemany('insert into test_table values(?,?)', data)
# # con.commit()

# def show_test_table():
#     print(cur.execute('select * from test_table').fetchall())


# show_test_table()



# import getpass
# print(getpass.getuser())


a = '5'
b = '10'


c = '1'

print(id(a), id(b), id(c))
b = b[:1]

a = str(int(b) +4)

print(a, b, c)

print(id(a), id(b), id(c))


