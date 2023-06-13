import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(4,4))

xs = np.random.random(100)

ys = np.random.random(100)

zs = np.random.random(100)


ax = fig.add_subplot(111, projection='3d')
ax.set_title("Eswar")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.set_zlabel("Z-Axis")

ax.scatter(xs,ys,zs)

plt.show()