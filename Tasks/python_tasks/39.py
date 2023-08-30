# 39.write a Program to print following pattern
# example1 : input : 3
# output:
#
# #
# # #



# inp = int(input("Enter a number to be printed :"))
inp = 5
for i in range(1,inp+1):
    for j in range(i):
        print("#","",end="")
    print("")
    
    