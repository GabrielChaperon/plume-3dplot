from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import sys

def R_y(alphay):
	return np.array([[np.cos(alphay), 0, np.sin(alphay)],
					 [0, 1, 0],
					 [-np.sin(alphay), 0, np.cos(alphay)]])


def R_z(alphaz):
	return np.array([[np.cos(alphaz), -np.sin(alphaz), 0],
					 [np.sin(alphaz), np.cos(alphaz), 0],
					 [0, 0, 1]])


data_name = sys.argv[1];

data = xc, yc, zc, S, C, B = np.loadtxt(data_name, skiprows=9).T
m, n = len(xc), 20
t2 = np.linspace(0, 2*np.pi, n)
xx = np.zeros([n, m])
yy = np.zeros([n, m])
zz = np.zeros([n, m])
points = np.vstack([np.zeros(n),
					np.cos(t2),
					np.sin(t2)]).T
xx[:,0] = np.copy(points[:,0])
yy[:,0] = np.copy(points[:,1])
zz[:,0] = np.copy(points[:,2])

alphays = np.zeros(m)
alphazs = np.zeros(m)
alphays[0] = 0
alphazs[0] = 0
for i in range(1, m):
	alphays[i] = np.arctan2(zc[i] - zc[i-1], xc[i] - xc[i-1])
	alphazs[i] = np.arctan2(yc[i] - yc[i-1], xc[i] - xc[i-1])

for i in range(m):
	A = np.dot(np.dot(points, R_y(alphays[i])), R_z(alphazs[i]))

	xx[:,i], yy[:,i], zz[:,i] = (B[i] * A[:,0] + xc[i],
							     B[i] * A[:,1] + yc[i],
							     B[i] * A[:,2] + zc[i])

concentration = np.ones([n, m])
for i in range(m):
	concentration[:,i] *= C[i] * 0.37
concentration = np.log10(concentration)
concentration -= np.min(concentration)
concentration /= np.max(concentration)
my_col = cm.jet(concentration)


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xc, yc, zc, 'r--')
surf = ax.plot_surface(xx, yy, zz, facecolors=my_col)
# plt.colorbar(surf) # por alguna razon se cae con esto

max_range = np.array([xx.max()-xx.min(), yy.max()-yy.min(), zz.max()-zz.min()]).max() / 2.0

mid_x = (xx.max() + xx.min()) * 0.5
mid_y = (yy.max() + yy.min()) * 0.5
mid_z = (zz.max() + zz.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)
ax.grid(False)
plt.show()