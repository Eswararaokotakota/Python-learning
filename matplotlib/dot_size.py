from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt

#we can set the size ofthe dot by using (ms) keyword
x = np.array([1,2,3,33,53,64])
y = np.array([1,23,3,44,52,63])
plt.plot(x,y,"o-.", ms=20)
plt.show()
