from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 20)
v = np.linspace(0, np.pi, 10)
uu, vv = np.meshgrid(u, v)
x = np.sin(vv) * np.cos(uu)
y = np.sin(vv) * np.sin(uu)
z = np.cos(vv)

ax.plot_trisurf(x.flatten(), y.flatten(), z.flatten(), color='b')

plt.show()
