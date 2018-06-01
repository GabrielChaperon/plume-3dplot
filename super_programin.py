from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys

data_name = sys.argv[1];

data = np.loadtxt(data_name, skiprows=1)
print data.shape
