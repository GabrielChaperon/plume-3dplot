from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import sys

def R_y(alphay):
	return np.array([[np.cos(alphay), 0, np.sin(alphay)],
					 [0, 1, 0],
					 [-np.sin(alphay), 0, np.cos(alphay)]])


data_name = sys.argv[1];

data = xc, yc, zc, S, C, B= np.loadtxt(data_name, skiprows=9).T
m, n = len(xc), 20
print n,m
t2 = np.linspace(0, 2*np.pi, n)
xx = np.zeros([n, m])
yy = np.zeros([n, m])
zz = np.zeros([n, m])
print xx.shape
points = np.vstack([np.zeros(n),
					np.cos(t2),
					np.sin(t2)]).T
print points.shape
xx[:,0] = np.copy(points[:,0])
yy[:,0] = np.copy(points[:,1])
zz[:,0] = np.copy(points[:,2])

alphays = np.zeros(m)
alphays[0] = 0
for i in xrange(1, m):
	alphays[i] = np.arctan2(zc[i] - zc[i-1], xc[i] - xc[i-1])

for i in xrange(m):
	A = np.dot(points, R_y(alphays[i]))
	xx[:,i],yy[:,i],zz[:,i] = (B[i]*A[:,0]+xc[i],
							   B[i]*A[:,1]+yc[i],
							   B[i]*A[:,2]+zc[i])

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xc[:10], yc[:10], zc[:10], 'r--')
ax.plot_surface(xx[:,:10],yy[:,:10],zz[:,:10])
lim = [-1.5,1.5]
# ax.set_xlim(lim)
# ax.set_ylim(lim)
# ax.set_zlim(lim)
plt.show()