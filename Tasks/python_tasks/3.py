#to check whether a number is divisible by both 3 and 4

number = int(input("enter a number:"))
check_point3,check_point4 = number%3, number%4
print(check_point3,check_point4)
if (check_point3 and check_point4) == 0:
    print("The number you have entered is divisible by '3,4' " "\U0001F44D" )
else:
    print("Not divisible by '3,4' ","\U0001F44E")