from turtle import left
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 380, 280, 290, 300, 310, 320, 330])

plt.title("data graph")
plt.xlabel("x data")
plt.ylabel("y data")

plt.plot(x,y, "o-.", color="red", )
plt.show()

#we can tell the font of the text label
a = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
b = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(a,b)

font1={"family":"serif", "color":"red", "size":"20"}
font2={"family":"monospace", "color":"blue", "size":"15"}
font3 = {"family":"cursive","color":"black", "size":"15"}
font4 = {"family":"fantasy","color":"m", "size":"15"}

plt.title("Font check",fontdict=font1, loc="left")#we can also tell the location of the text (alignment)
plt.xlabel("Font-1", fontdict=font2)
plt.ylabel("Font-2", fontdict=font4)
plt.show()


