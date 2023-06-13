#import matplotlib
import matplotlib.pyplot as plt #we are using the submodule in the matplotlib pyplot so imported only that module
import numpy as np

x_axis = np.array([1,10])
y_axis = np.array([1,100])
#we can give names 
plt.title("First plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x_axis,y_axis)
plt.show()  #will prints the line plot between the points
