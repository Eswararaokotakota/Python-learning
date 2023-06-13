import matplotlib.pyplot as plt
import random

x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
for i in range(0,20): 
    a = random.randrange(1,100)
    x.append(a)
for i in range(0,20):
    a = random.randrange(1,100)
    y.append(a)
for i in range(0,20):
    a = random.randrange(1,100)
    x1.append(a)
for i in range(0,20):
    a = random.randrange(1,100)
    y1.append(a)
for i in range(0,20):
    a = random.randrange(1,100)
    x2.append(a)
for i in range(0,20):
    a = random.randrange(1,100)
    y2.append(a)
for i in range(0,20):
    a = random.randrange(1,100)
    x3.append(a)
for i in range(0,20):
    y3.append(i)


plt.plot(x,y,x1,y1,x2,y2,x3,y3)
plt.show()