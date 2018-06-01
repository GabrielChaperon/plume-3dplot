from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# data
z = np.linspace(0, 1, 20)
theta = np.linspace(0, 2 * np.pi, 20)
z, theta = np.meshgrid(z,theta)
x = np.cos(theta) + z
y = np.sin(theta)

ax.plot_surface(x, z, y, color='b')
ax.set_xlim([-2,2])
ax.set_ylim([-2,2])
ax.set_zlim([-2,2])
plt.show()