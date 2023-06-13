# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

# file1 = open("C:\\Users\\Eswar\\Desktop\\randome.txt","a")#a append, adds
# file1.write("boom boom shakalaka")
# file1.close()

# file1 = open("C:\\Users\\Eswar\\Desktop\\randome.txt","r")
# print(file1.read())
# file1.close()

#w will over writes the existing content
file2 = open("C:\\Users\\Eswar\\Desktop\\randome.txt","w")
for i in range(0,1000000):
    file2.write("count"+str(i))
    # file2.close()

# file2 = open("C:\\Users\\Eswar\\Desktop\\randome.txt","r")
# print(file2.read())
# file2.close()

# # To create a file we can use "x" and if file already exists the "x" method will returns an error
# file3 = open("C:\\Users\\Eswar\\Desktop\\randome_antaava.txt","x")
# file3 = open("C:\\Users\\Eswar\\Desktop\\randome_antaava.txt","w")
# file3.write("edhoti le em chestham")
# file3.close()
# file4 = open("C:\\Users\\Eswar\\Desktop\\randome_antaava.txt","r")
# print(file4.read())
# file4.close()

