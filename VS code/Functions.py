#Functions are like sub programs we can call in the code later 


def userdetails():
    a = input("enter name :")
    print("Hi!", a)

userdetails()


#Inside the function paranthasis()if we write anything that can be aclled as argument
#we can change it lated by a values 
def argument(callme):
    print(callme+" you are nice")

argument("eswar")
argument("boom")

#we can use multiple arguments but later we need to call all otherwise it gives error
def function(callmebro, callmebro1):
    print(callmebro, "",callmebro1)

function("bro!","nothing")#if i dont call two arguments it will rise an error
'''function("eswar")'''# //it will gives an error**

#you can assign someting to the argument later by its name and an assignment operator
def function1(eswr1, eswar2, eswar3):
    print("hello! ",eswar2)
function1(eswr1 ="eswra",eswar2="rao",eswar3="kttakota")

#If you dont know how meny arguments you will add, you can just use a *argument(star with argument)
def function2(*arg):
    print("padmavathi "+arg[2])
function2("happy aa","tiles vesthunnaru anta gaa","sheddu bondhi")#it will take a tuple of items

#If you use ** two stars it will take distonory of items
def function3(**args):
    print(args["pin"])

function3(name="eswar",pin=413,branch="ECE")

#
