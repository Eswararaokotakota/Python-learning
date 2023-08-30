# n= 5 
# m = int((n/2)+1)
# point1 = int((m/2)+1)
# point2 = 0

# for j in range(n):
#     print(" "*point1,"*"," "*point2,"*")
#     point1-=1
#     point2+=1
#     if j == int(n/2):
#         print("ok")
#         print(" "*point1,"*"," "*point2,"*")
#         point1+=1
#         point2-=1
#     print("")
n = 6
m=0

for i in range(int(n)):
    print(i)
    if i == 0 :
        print("  "*n,"  $")
        continue
    
    elif i >= n/2 and i<n:
        print("as")
        print("  "*n,"$","  "*m,"$")
        n+=1
        m-=2
        
    elif i>0  and i<=(n/2)-1:
        print("  "*n,"$","  "*m,"$")
        n-=1
        m+=2
        continue
    elif i==n-1:
        print("hu")
        print("  "*n,"  $")

   
        