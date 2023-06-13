# a = 0
# while a <= 10:
#     print(a)
#     a+=1

#using break mmethod we can exit from a loop with a condition
a = 0
while a<= 10:
    print(a)
    if a==5:
        break
    a+=1

#with the continue methode we can exit from loop and proceed to next instructions
a1 = 0
while a1 < 10:
    a1+=1
    print(a1)
    if a1 == 8 :
        continue
print("theis is other statemsnt printed after continue statement")

#Wwe can use alse if the condition in loop false by using an "else"
a2 = 0
while a2<=15:
    print(a2)
    a2+=1
else:
    print("exitted from a2 loop else")


#