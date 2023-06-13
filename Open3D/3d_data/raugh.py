numbers=[]
for i in range(1000):
    numbers.append(i)  #step-1

#step-2
for i in numbers:
    if (i%2)==0:
        print("Number is even ----------",i)
    else:
        print("This is odd ---------",i)