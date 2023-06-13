from cv2 import line
import numpy as np
import matplotlib.pyplot as plt

#dotted lines(:)
x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,4,5,6])
plt.plot(x,y, ":")
plt.show()

#line(-)
x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,4,5,6])
plt.plot(x,y, "-")
plt.show()

#dotted bars line
x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,4,5,6])
plt.plot(x,y, "--")
plt.show()

#bar-dot line (-.)
x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,4,5,6])
plt.plot(x,y, "-.")
plt.show()

#we can also print the line by using line style 

x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,4,5,6])
plt.plot(x,y, linestyle="dotted")
plt.show()

plt.plot(x,y,linestyle="dashed")
plt.show()

#we can say linestyle as ls
plt.plot(x,y,ls="dashed")
plt.show()

#we can set the line color by calling color
plt.plot(x,y,color="grey") #any color
plt.show()

#we can also say the line size as we did for dot formatting
plt.plot(x,y, linewidth="20")
plt.show()