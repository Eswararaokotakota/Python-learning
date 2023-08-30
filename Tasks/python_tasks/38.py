# 38.write a Program to print following pattern
# example1 : input : 3
# output:
# 1
# 1 2
# 1 2 3


inp = int(input("Enter a number to be printed :"))
# inp = 3
for i in range(1,inp+1):
    for j in range(i):
        print(j+1,"",end="")
    print("")