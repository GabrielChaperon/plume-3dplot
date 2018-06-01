from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys

data_name = sys.argv[1];

data = xc, yc, zc, _, _, b, a, _, _ = np.loadtxt(data_name, skiprows=1).transpose()
b /= 2

theta = np.linspace(0, 2*np.pi, 20)
xx, tt = np.meshgrid(xc, theta)
nrows, ncols = xx.shape
yy = np.cos(tt)
zz = np.sin(tt)
print b
print a
for i in xrange(ncols):
	yy[:,i] *= a[i]
	zz[:,i] *= b[i]
yy += yc * np.ones(xx.shape)
zz += zc * np.ones(xx.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx, yy, zz)
plt.show()

	


