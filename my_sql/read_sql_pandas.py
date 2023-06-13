import mysql.connector as connection
import pandas as pd

my_database =connection.connect(host = "localhost", user="root", passwd = "mysql", use_pure=True)

print(pd.read_sql("select * from eswar_database.test_table",my_database))

print(pd.read_sql("select x3,x1 from eswar_database.test_table", my_database))