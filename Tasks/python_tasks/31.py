# 31.Write a Program to reverse a number

# inp = int(input("enter number:"))
inp = 54144
length = len(str(inp))
inpp = str(inp)
# print(inpp[::-1])
for i in range(len(str(inp))):
    inpp = str(inp)
    print(inpp[length-1],end="")
    length-=1
