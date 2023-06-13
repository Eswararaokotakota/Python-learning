import mysql.connector as connection

def connceting_to_database(): #this is an example code to connect to the sql database server
    try:
        mydb = connection.connect(host="localhost",user="root", passwd="mysql",use_pure=True)
        # check if the connection is established

        query = "SHOW DATABASES"
        print("conncetion_done")
        cursor = mydb.cursor() #create a cursor to execute queries
        cursor.execute(query)
        print(cursor.fetchall())

    except Exception as e:
        mydb.close()
        print(str(e))
#establishing the connection between our python code with the mysql server database
my_connection = connection.connect(host="localhost", user="root", passwd="delhi123", use_pure=True)
#creating a cursor to start at first line
cursor = my_connection.cursor()
#getting the databases list
cursor.execute("show databases") # In this way we are giving the commands to the sql
# printing the all data base names by fetching them
print(cursor.fetchall())

cursor.execute("create database to_do_database") #This will create a databse 
# cursor.execute("Drop Database eswar_database1")  #This drop databse is used to delete a database

# cursor.execute("use eswar_database") #we are telling to use eswar_database to store and get the data
# #Here we are creating a table
# cursor.execute("create table test_table(x1 int(5), x2 VARCHAR(2), x3 DATE)") #(date = yy-mm-dd) 
# #will creates a table with x1,x2,x3 columns with respected datatypes
 #VARCHAR is a variable wich will hole both numbers abd charectors
# cursor.execute("select * from test_table")

####Now we are inserting the values in to the table
cursor.execute("insert into test_table values(6234, 'es', '2000-10-10')") #here we just created the data not uploadedin our database
#To upload(commit) the data we need to execute a line
my_connection.commit() #now it will push the data to the table and now you are able to see the data in sql ui
cursor.execute("select * from test_table")
# print(cursor.fetchall)
for i in cursor.fetchall():
    print(i)

#wecan select the perticulat columns
cursor.execute("select x1,x2 from test_table") #will gives you only two columns data
for i in cursor.fetchall():
    print(i)

print("Done...!")