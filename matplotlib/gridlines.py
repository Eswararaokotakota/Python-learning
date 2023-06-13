
import numpy as np
import matplotlib.pyplot as plt

x = np.array([10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 
              10.227500000000001, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.22765625, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.227500000000001, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.227500000000001, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.227500000000001, 10.227500000000001, 10.22765625, 10.22765625, 10.227500000000001, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.227500000000001, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.22765625, 10.227500000000001, 10.22765625, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227343750000001, 10.2265625, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.225, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.22515625, 10.2253125, 10.2253125, 10.2253125, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225468750000001, 10.225625, 10.225625, 10.22578125, 10.22578125, 10.225625, 10.225625, 10.225625, 10.22578125, 10.22578125, 10.225625, 10.225625, 10.22578125, 10.22578125, 10.22578125, 10.22578125, 10.225625, 10.22578125, 10.225625, 10.225625, 10.225625, 10.22578125, 10.225625, 10.22578125, 10.22578125, 10.22578125, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.2259375, 10.22609375,
              10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.22640625, 10.2265625, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.22703125, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.227343750000001, 10.227343750000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.2278125, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.22765625, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227500000000001, 10.227500000000001, 10.227500000000001, 10.227343750000001, 10.227343750000001, 10.227500000000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227500000000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.2271875, 10.2271875, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.227343750000001, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.227343750000001, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.2271875, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.2271875, 10.2271875, 10.2271875, 10.22703125, 10.22703125, 10.2271875, 10.2271875, 10.22703125, 10.2271875, 10.2271875, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125,
              10.22703125, 10.22703125, 10.22703125, 10.2271875, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 
              10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.226875, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.226875, 10.22703125, 10.22703125, 10.22703125, 10.226875, 10.22703125, 10.22703125, 10.22703125, 10.226875, 10.226875, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.22703125, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.22671875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.226875, 10.22671875, 10.22671875, 10.22671875, 10.226875, 10.226875, 10.226875, 10.22671875, 10.226875, 10.226875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875, 10.22671875])
y1=[]
for i in range(len(x)):
    y1.append(i)
y=np.array(y1)
print(len(x),len(y1))



# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(y,x)
plt.grid()
plt.show()  #prints the plotline with grid line


plt.plot(x,y)
plt.grid(axis = "x")
plt.show()


plt.plot(x,y)
plt.grid(axis = "y")
plt.show()

#we can set the color and style and even the size of the grid also
plt.plot(x,y)
plt.grid(color = "red", linestyle="-.", linewidth= 0.5)
plt.show()