import mysql.connector as connecton

my_database =connecton.connect(host = "localhost", user="root", passwd = "mysql", use_pure=True)
cursor = my_database.cursor()

data_bases_lst = cursor.execute("show databases")
print(cursor.fetchall())