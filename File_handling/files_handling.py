# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

file1 = open("C:\\Users\\Eswar\\Desktop\\run detection code in ubantu.txt")

file2 = open("C:\\Users\\Eswar\\Desktop\\run detection code in ubantu.txt","r")
print(file2.read())#will prints the content in that text file

#we can also read a part of the file
file3 = open("C:\\Users\\Eswar\\Desktop\\run detection code in ubantu.txt","r")
print(file3.read(10))#will returns 10 charecters

#we can return one line by using readline method
file4 = open("C:\\Users\\Eswar\\Desktop\\run detection code in ubantu.txt","r")
print(file4.readline())
#we can print two lines by calling readline two times
file5 = open("C:\\Users\\Eswar\\Desktop\\run detection code in ubantu.txt","r")
print(file5.readline())
print(file5.readline())

#We can read everyline by looping
file6 = open("C:\\Users\\Eswar\\Desktop\\run detection code in ubantu.txt","r")
for x in file6:
    print(x)
file6.close()
