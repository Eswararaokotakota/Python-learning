import math

a = 1.335
b = 1.260
z=3.2

c= a-b
d = math.sqrt((math.pow(z,2)-math.pow(c,2)))
percentage = (c/d)*100

print("Rise =",c,"\n","Camber =",percentage)