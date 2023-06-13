




from tkinter import E


print("eswar")
#printed successfully

#Conditional statements if, elif, else :
a = 30
b = 30
if b>a:
    print("B is bigger than a")
elif a==b:
    print("both are equal man")
else: 
    print("A is bigger than B")
#so for a conditional if elif else syatements the conditions should have the same space before it

#1 example for if statement
x = 9
r = x % 2
if r ==0:
    print("even")
else:
    print("odd")

#to tell weather the student pass or fail
#pass marks 35marks
Marks_gained = 58
Pass_marks = 35
if Marks_gained >= Pass_marks :
    print("COngrats! you are qualified")

    #you can also write a condition in brackets for good understanding of your code like if(condition):
    if (Marks_gained >= Pass_marks):
        print("woohooo you qualified")

#In python you don't need to mension the type of variable like float, int, string. the pthon autometically understands the variable type
number = 10
print(number)
number1 = 9.3
print(number1)
namestring = "string_name"
print(namestring)
#The output comes so you dont need to mension the variable : )

#getting input from user
name_get = input("enter your name")
print(name_get)
#it will asks yout to enter your name and then displays the name you have entered
num1 = input ("enter first number")
num2 = input("enter second number")
sum =int(num1+num2)
print ("The sum is",sum)
#it will prints the total sum value

n1 = int(input("enter num1 : "))
n2 = int(input("enter num2"))
product = n1*n2
print("product is", product)

#for loop while loop, if else, continu, break

#while loop
i=1
j=1
while i<=2:
    print("learning loops")
    i=i+1

while j<=3:
    print("practice well")
    j=j+1
 
#nested while loop
m=1
n=1
while m <= 3: 
    print("main")
    m+=1
    while n <= 2:
     print("nested while loop")
     n+=1
print("-----------nested loop up here----------")

#same as above but trying different logic while the inner loop reches to the certain value then the.main while loop starts
m=1
n=1
while m <= 3: 
    while n <= 3:
     print("nested while loop")
     n+=1
     if n==4:
         print("n reached 3")
    print("main")
    m+=1


#Experimenting with functions
# def my_funcion(e):
#     if a == 20:
#         print("you reached 20 the maximun number here")
#     else:("nothing just proceed")

# while a < 20:
#     a+=1
#     print(a)

# my_function(e)

def my_function():
    print("you called me right?")
    if a == 20:
        print("a reached 20 and this function calling is working")
    else:
        print("no problem still calling function is working")
a=0
while a< 20:
    a+=2
    print(a)  
    my_function()