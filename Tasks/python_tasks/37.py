# 37.write a Program to print following pattern
# example1 : input : 5
# output:
# 5 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5


inp = int(input("Enter a number to be printed :"))
for i in range(inp):
    for j in range (inp):
        print(inp,"",end="")
    print("")