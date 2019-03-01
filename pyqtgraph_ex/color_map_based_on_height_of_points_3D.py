from pyqtgraph.Qt import QtGui
import pyqtgraph.opengl as gl
import matplotlib.pyplot as plt
import numpy as np

# Create the view
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 400
w.show()

# Create the signal 3D
y = np.linspace(0, 100, 10)
x = np.linspace(0, 100, 10)
temp_z = np.random.rand(len(x),len(y)) * 80


cmap = plt.get_cmap('jet')
min_z = np.min(temp_z)
max_z = np.max(temp_z)
rgba_img = cmap((temp_z - min_z)/(max_z - min_z))

surf = gl.GLSurfacePlotItem(x=x, y=y, z=temp_z, colors=rgba_img )
w.addItem(surf)
# surf.setData(x=x, y=y, z=np.random.rand(len(x),len(y)) * 80)

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()