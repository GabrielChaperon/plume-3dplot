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


xl = [0, 1]
yl = [0, 0]
zl = [0, 1]

t = np.linspace(-0.5*np.pi,0.5*np.pi,20)
x0 = np.cos(t)
y0 = np.zeros(t.shape)
z0 = np.sin(t)
# points = np.vstack((x0,y0,z0)).T
# # A = points
# alpha = np.arctan((zl[1]-zl[0])/(xl[1]-xl[0]))
# A = np.dot(points, R_y(alpha))
# x,y,z = A[0]+xl[1],A[1]+yl[1],A[2]+zl[1]
# print A
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x0,y0,z0,color='b')
# ax.plot(A[:,0]+xl[1],A[:,1]+yl[1],A[:,2]+zl[1], color='b')
# ax.plot(xl,yl,zl,'r')
lim = [-1.5,1.5]
ax.set_xlim(lim)
ax.set_ylim(lim)
ax.set_zlim(lim)
plt.show()
