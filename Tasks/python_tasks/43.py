# 43.write a Program to print following pattern(Read about ord(), chr() functions in python)
# example1 : input : 3
# output:
# A
# B C
# D E F


# inp = int(input("Enter a number to be printed :"))

inp = int(input("Enter a number to be printed :"))
# inp = 8
if inp <= 8:
    char = 65
    for i in range(inp):
        for j in range(i):
            print(chr(char),end=" ")
            char+=1
        print("")
else:
    print("\u26A0\ufe0f  ","Entered number should be lessthat '9'")
        