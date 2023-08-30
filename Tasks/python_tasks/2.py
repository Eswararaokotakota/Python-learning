#to check whether a number is divisible by 6
number = int(input("enter a number:"))
check_point = number%6
if check_point == 0:
    print("The number you have entered is divisible by '6' " "\U0001F44D" )
else:
    print("Not divisible by '6' ","\U0001F44E")