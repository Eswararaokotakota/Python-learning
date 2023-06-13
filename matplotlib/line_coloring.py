import numpy as np
import matplotlib.pyplot as plt

# Prints the line red color
x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,43,54,65])
plt.plot(x,y, "r")
plt.show()

# we can mension colors as given below
# r, g, b, c, m, y, w, k  --k=black--  --w=white--

# If you mension the point then it will make the point as red
x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,41,45,63])
plt.plot(x,y, "or")
plt.show()  # Plots dots only with red color

# We can print both line and dot in a color 
x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,43,54,64])
plt.plot(x,y, "o-m")
plt.show()


#we can set the line color by calling color
plt.plot(x,y,color="grey") #any color
plt.show()

