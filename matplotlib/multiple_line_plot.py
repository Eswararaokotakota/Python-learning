import numpy as np
import matplotlib.pyplot as plt

plt.title("Multi point plot")
x_axis = np.array([1,4,12,40])
y_axis = np.array([5,8,5,34])
plt.plot(x_axis,y_axis)
plt.show()
#will prints the points and joins them with a line

plt.title("Multi dot plot")
plt.plot(x_axis,y_axis,"o")
plt.show()
#will prints the dots in the graph


#If we dont give the x_axis values it will autometicall takes from 0,1,2,3, so on....
plt.title("x_axis not given")
b = np.array([1,2,5,8,9])
plt.plot(b)
plt.show()

