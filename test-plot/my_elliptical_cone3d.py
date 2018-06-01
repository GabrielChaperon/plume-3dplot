from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# data
a = 2
b = 1
z = np.linspace(0, 1, 10)
theta = np.linspace(0, 2 * np.pi, 20)
z, theta = np.meshgrid(z,theta)
n, m = z.shape
x = z * np.ones(z.shape) * np.cos(theta)
x[:,:m/2] *= a
x[:,m/2:] *= b

y = z * np.ones(z.shape) * np.sin(theta)
y[:,:m/2] *= b
y[:,m/2:] *= a
print n,m
print x.shape
print y.shape
print z.shape
# ax.autoscale(enable=False)
# ax.autoscale_view()
ax.plot_surface(x, z, y, color='b')
plt.show()