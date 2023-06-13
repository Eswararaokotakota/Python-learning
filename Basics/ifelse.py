a = 19
b = 15
if a < b:
    print("b is bigger")
elif a > b :
    print("a is bigger")
elif a == b:
    print("Both are equal")
elif a != b:
    print("both are not equal")
else:
    print("a and b doesnt exists")

#single line if else statement
print("A is big") if a>b else("b is grater")

#single line if condition
x=10
y=20
z=30
if x<y:print("x is bigger man")

#and or condidions
#AND operation
if x<y and y<z:
    print("yedhoti")
#if any condition is true returns true
if x>y or y>x:
    print("sarle inka")

#NESTED IF  9IF INSIDE IF
if x<y:
    print("x is smaller")
    if y<z:
        print("y is also smaller")
    else:
        print("boom")
else:
    print("x and y are bigger")


#If you want if condition with no operation you can use "PASS" method to get free from error
if x<y:
    pass



print("conditions done")