import os
# from pickle import TRUE
# os.getcwd  gets current distonory
a = os.getcwd()
print(a)
#we can create a folder directory by using os.mkdir
os.mkdir("E:\\Coding\\Python\\os_module\\creating_file") #created a folder success fully


#We can also delete the distonory that exists
#HERE WE ARE CREATING AND DELETING IT 
os.rmdir("E:\\Coding\\Python\\os_module\\creating_file")


#We can get the list of files consisting in a folder
b = os.listdir("E:\\Coding")
print(b,"---Got the list of files in a folder---")


#Check if file path is correct or not
my_path = "E:/Coding/Python/os_module/sample_directory/"

path_check = os.path.isdir(my_path)

# check = TRUE
if (path_check):
    print("The selected path exist!. You can move forward")
else:
    print("Path doesn't exists")#Done! it's working bro

path_txt = "E:\\Coding\\Python\\os_module\\"
#writing some string data in to a file 
txt_file = open(path_txt+'txt_file.txt','a')
text = input("Enter text : ") # asks you to enter the text
txt_file.write(text+"\n")#will writes the text in the fsile
#process done 

#Now we will read the data from the file
path_txt = "E:\\Coding\\Python\\os_module\\txt_file.txt"
reader = open(path_txt,"r")
read_txt = reader.read()
print(read_txt)
txt_file.close()

