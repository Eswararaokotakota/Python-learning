
for x in "banana":
    print(x)

text ="iam an embedded engineer"
print("embedded" in text)

text1 ="i am learning python now"
if "learning" in text1:
    print("yes i know you are learning python")

text2 = "now learning about string operations in python"
print("python" not in text2)

text3 = "this is awesome that i can do meny operations in python"
if "bomb" not in text3:
    print("man! bomb not in python")
    print("check once",text3)

#string slicing
text4 = "now iam learning slicing in python"
print(text4[4:30])
print(len(text4))

text5 = "this is awesome experiance"
print(text5[:20])

text6 = "this is also awesome"
print(text6[3:])

#We can do negative indexing with strings wow
text7 = "this is soo suprising"
print(text7[-9:-1])
print(len(text7))


#We ca modify the strings 
text8 = "now learning modifications of string"
print(text8.upper())

text9 = "This is grabbing my INTERRESR wery well"
print(text9.lower())

text10 = "we can replace the charecter in the string E"
print(text10.replace("E","F"))

text11 ="We can makes list from string using split"
print(text11.split(","))
#The above will do the whole texta as single item 
#but if we place a , in between words it will creates a superate item
text12 = "We, can, makes list, from string, using, split"
a = text12.split(",")
print(a)
print(a[2])#here we are calling the items stored in the list

text13 = "making every word first letter uppercase"
print(text13.title())

#We can add two strings
a = "Good one"
b = "pandago"
c = a + b
print(c)
d = a + "  " + b#adds a space between
print(d)

#Format method will iserts the number in the string
age = 21
text14 = "Iam eswar, my age {}"# flower brackets are must and should
print(text14.format(age))

#we can do formating to multiple numbers
age = 21
likenumber = 3
roolnumber = 413
text15 = "hi,iam eswar, my age is {}, liked number{}, roll number{}"
print(text15.format(age,likenumber,roolnumber))


#to print double quotes"" in the print method we need to use ex-scape character
text15 = "abba aaru \"pandago\" good one aaa"
print(text15)

#to print data in new line
print("pandago\naaaru")
print("good")
print("\naaaru")


#encoding a string
text16 = "lets see this will be encoded or not"
print(text16.encode())