import os

os.mkdir("C:\\Users\\Eswar\\Desktop\\removed.txt")
#we need to imoprt os because deleting file need interraction of os in your system 
'''os.remove("C:\\Users\\Eswar\\Desktop\\removed.txt")''' #successfully deleted the file
#if file doesnt exists then returns an error, We can solve this error below 

#we can check if the file exists to delete 
if os.path.exists("C:\\Users\\Eswar\\Desktop\\removed.txt"):
    os.remove("C:\\Users\\Eswar\\Desktop\\removed.txt")
else:
    print("file doesnt exists")