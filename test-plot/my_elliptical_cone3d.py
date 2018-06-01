from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# data
a = 2
b = 1
z = np.linspace(0, 1, 20)
theta = np.linspace(0, 2 * np.pi, 20)
z, theta = np.meshgrid(z,theta)
x = a * 0.5 * z * np.ones(z.shape) * np.cos(theta)
y = b * 0.5 * z * np.ones(z.shape) * np.sin(theta)

ax.autoscale(enable=False)
ax.autoscale_view()
ax.plot_surface(x, z, y, color='b')
plt.show()