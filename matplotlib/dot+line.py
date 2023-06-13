from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt

a =np.array([2,3,5,10,17,20,25])
b = np.array([5,6,9,12,17,20,23])
plt.plot(a,b,marker="o")
plt.show()

# We can use meny types of markers for different type of representatiom
a =np.array([2,3,5,10,17,20,25])
b = np.array([5,6,9,12,17,20,23])
plt.plot(a,b,marker="D")
plt.show()

#we have someny types 
# d,D,*, , , . ,x,X,+,p,P,s,h,H,>,<,^,v,1,2,3,4,|,_   
a =np.array([2,3,5,10,17,20,25])
b = np.array([5,6,9,12,17,20,23])
plt.plot(a,b,"o:")
plt.show()