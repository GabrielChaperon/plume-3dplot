import numpy as np
import matplotlib.pyplot as plt

# data
a = 2
b = 1
theta = np.linspace(0, 2*np.pi, 20)

x, y = a*np.cos(theta), b*np.sin(theta)
plt.axis('equal')
plt.plot(x,y)
plt.show()