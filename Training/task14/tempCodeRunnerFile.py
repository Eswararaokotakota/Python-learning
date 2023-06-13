



str = input("Enter any value: ")
 
if str.isdigit():
    print("User input is an Integer ")
else:
    print("User input is string ")





def tryexcept():
    integer= "23df"

    try:
        int(integer)
    except:
        print("not int")

    #Detects the numbers in a string
    try:
        ProjectName= int(input("Enter ProjectName : "))
        FromDirection= int(input("Enter From Direction : "))
        ToDirection= input("Enter To Direction : ")

    except ValueError:
        print("Input should be integers")


    #Detects the special charecters
    try:
        ProjectName= input("Enter ProjectName : ")
        
    except:
        pass


    #Detects charactres insted of numbers
    try:
        LaneNumber= int(input("Enter LaneNumber : "))
    except:
        
        print("'Characters are not accepted in Lane Number'")