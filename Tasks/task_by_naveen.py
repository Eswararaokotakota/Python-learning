# # a = 0
# # for a in range(1,1000):
# #     if(a%1 == a and a%a == 1 ):
# #         print(a)

# # print("out from loop")
# i = 0
# while (i<=998):
#     i+=1
#     if (i%i == 0 and i/1 == i):
#         print(i)
i=2
while (i<=9):
    j=i
    while(j==1):
        if(i%j == 0 and i//j == 1):
            print(i)
        j-=1
    i+=1

print("executed")

