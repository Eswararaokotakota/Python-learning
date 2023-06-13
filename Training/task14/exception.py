import re

def integerfind():#To find the integer in a ProjectName
    #Detects the integer in a charecter
    # print("If any integer exists in ProjectName, It will gives you exception")
    try:
        ProjectName = input("Enter ProjectName: ")
        result = bool(re.search(r"\d", ProjectName)) 
        if result == True:
            print(x)
        print("Good")
    except:
        print("'Numbers not accepted in Field Name'")

def stringfind():#To find the string in a LaneNumber
    #Detects charactres insted of numbers
    # print("Generates an excepton if any charecter entered in lane number")
    try:
        LaneNumber= int(input("Enter LaneNumber : "))
        print("Good")
    except:
        print("'Characters are not accepted in Lane Number'")

def specialCharfind():#To find the special charecters in the name feild
    # formDirection = input("Enter the ProjectName: ")
   try:
    specialChar = '[!@#$%^&*()><?:;{]}'
    s = input("enter special char: ")
    if any(c in specialChar for c in s):
        print(x) #Placed an undefined variable to generate an error and jump into the exception block
    else:
        print("Good")
   except:
    print("Special Characters not accepted in Field Name")



integerfind() 
stringfind()
specialCharfind()