from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# data
xo = np.linspace(0, 1, 10)
theta = np.linspace(0, 2 * np.pi, 20)
xx = np.zeros([20,10])
yy = np.zeros([20,10])
zz = np.zeros([20,10])
for j in xrange(len(xo)):
 	for i in xrange(len(theta)):
 	 	xx[i][j] = xo[j]
 	 	yy[i][j] = np.cos(theta[i])
 	 	zz[i][j] = np.sin(theta[i])

ax.plot_surface(xx, yy, zz, color='b')

plt.show()