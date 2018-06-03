from mayavi import mlab
import numpy as np

a = np.random.random((4, 4))
mlab.surf(a)
mlab.show()