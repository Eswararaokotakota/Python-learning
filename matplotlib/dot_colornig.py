import numpy as np
import matplotlib.pyplot as eswar

# To set color to the dot(marker) border we use markeredgecolor as "mec"
x = np.array([2,33,44,66,76])
y = np.array([3,5,43,54,67])
eswar.plot(x,y,"o-",mec="r")
eswar.show()

#we can set the inner dot color using  "mfc"
x = np.array([2,33,44,66,76])
y = np.array([3,5,43,54,67])
eswar.plot(x,y,"o-",mfc="m")
eswar.show()
#we can give the hexadecimal values to display the color
x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,43,54,64])
eswar.plot(x,y, "o-", mec="#04AA6D")
eswar.show()

