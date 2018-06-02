from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def R_x(alphax):
	return np.array([[1, 0, 0],
					 [0, np.cos(alphax), -np.sin(alphax)],
					 [0, np.sin(alphax), np.cos(alphax)]])


def R_y(alphay):
	return np.array([[np.cos(alphay), 0, np.sin(alphay)],
					 [0, 1, 0],
					 [-np.sin(alphay), 0, np.cos(alphay)]])


def R_z(alphaz):
	return np.array([[np.cos(alphaz), -np.sin(alphaz), 0],
					 [np.sin(alphaz), np.cos(alphaz), 0],
					 [0, 0, 1]])




t1 = np.linspace(-0.5*np.pi,0.5*np.pi,20)
xc = np.cos(t1)
yc = np.zeros(t1.shape)
zc = np.sin(t1)
t2 = np.linspace(0, 2*np.pi, 30)
xx = np.zeros([len(t2), len(t1)])
yy = np.zeros([len(t2), len(t1)])
zz = np.zeros([len(t2), len(t1)])


points = np.vstack([np.zeros(t2.shape),
					0.5 * np.cos(t2),
					0.5 * np.sin(t2)]).T

xx[:,0] = np.copy(points[:,0])
yy[:,0] = np.copy(points[:,1])
zz[:,0] = np.copy(points[:,2])



alphays = np.zeros(len(t1))
alphays[0] = 0
for i in xrange(1, len(t1)):
	alphays[i] = np.arctan2(zc[i] - zc[i-1], xc[i] - xc[i-1])

for i in xrange(len(zc)):
	A = np.dot(points, R_y(alphays[i]))
	xx[:,i],yy[:,i],zz[:,i] = A[:,0]+xc[i],A[:,1]+yc[i],A[:,2]+zc[i]


		


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xc, yc, zc, 'r--')
ax.plot_surface(xx,yy,zz)
lim = [-1.5,1.5]
ax.set_xlim(lim)
ax.set_ylim(lim)
ax.set_zlim(lim)
plt.show()
plt.show()