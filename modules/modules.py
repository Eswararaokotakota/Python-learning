import calculator as cal #I imported a module which i have made my own module calculator with functionsc(calculator.py)

a = int(input("enter number: "))
b = int(input("enter number: "))

select = str(input("what you want to do? add, sub, mul, percent \n"))
if select == "add":
    print(cal.add(a,b))

elif select == "mul":
    print(cal.mul(a,b))

elif select == "sub":
    print(cal.sub(a,b))

elif select == "percent":
    print(cal.percent(a,b))
   
else:
    print("enter proper math")
    
