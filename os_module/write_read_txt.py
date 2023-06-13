import os

path = "E:\\Coding\\Python\\os_module\\"

txt_file = open(path+"text_file.txt","a")
data = input("Type something :  ")
txt_file.write(data+"\n")

txt_file.close()

#reading the written file 

reader = open(path+"text_file.txt","r")
read_data = reader.read()
read_5bytes = reader.read(2)#willread 5 bytes only means first 5 letters
print(read_data+"\n")
print(read_5bytes+"done!")