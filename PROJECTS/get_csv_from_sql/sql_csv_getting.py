from mysql import connector
import pandas as pd

my_database =connector.connect(host = "192.168.29.71", user="root", passwd = "delhi123", use_pure=True)
cursor = my_database.cursor()
data_bases_lst = cursor.execute("show databases")
print(cursor.fetchall())
cursor.execute("use roadrunner")
cursor.execute("SHOW TABLES")
for table_name in cursor:
    print(table_name)

cursor.execute("select * from pavement_distress")    
# for i in cursor.fetchall():
#     print(i)
data = cursor.fetchall()
print(data)
df = pd.DataFrame(data)
df.to_csv("pavement_distress.csv")