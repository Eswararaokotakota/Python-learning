'''if in python code a variable is not defined and then the python will stops and returns an error'''
'''But if we use exception method, we can leave that error and do next process'''
# 1. The '''try''' block lets you test a block of code for errors.

# 2. The '''except''' block lets you handle the error.

# 3. The '''else''' block lets you execute code when there is no error.

# 4. The finally block lets you execute code, regardless of the result of the try- and except blocks.

#exception   ---excuse even error---
'''will generates an error because x is not defined''' 
# print(x)
# print("Will not be printed because error occured before this line")
x = "hehe"
try:
    print(x)
except:
    print("it will be printed be cause we used try ---Error? No problem just executing next line---")


'''you can exicute a code when you get a specific error  CRAZY KADHA!!'''
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Somthing is wrong babai, define that variable")

#we can use else if no error occured "we can use this for no error confirmation"
try:
    x = "Eswara Rao"
    print(x)
except:
    print("Error vachindhi roii")
else:
    print("No error man your try code is correct")

'''For a real world example read code below'''
#The try block will raise an error when trying to write to a read-only file:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  

'''
#if any error occured as you know then you can pass a word for that error for better understanding of user
x = -1
if x < 0:
    raise Exception("sorry, no number below zero")
    #will generates error and shows this ''' # commented because it stopes execution


x = "Eswar"
if not type(x) is int:
    raise TypeError("FUCK...! that",x,"is string bro!!" )

