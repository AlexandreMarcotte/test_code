from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 20
w.show()
w.setWindowTitle('pyqtgraph example: GLScatterPlotItem')

g = gl.GLGridItem()
w.addItem(g)


pos = np.array([[1, 0, 0], [2, 0, 0]]).reshape(2, 3)
size = np.array([0.8, 0.5])
color = np.array([[0.0, 1.0, 0.0, 0.9], [0.0, 1.0, 0.0, 0.9]]).reshape(2, 4)


sp1 = gl.GLScatterPlotItem(pos=pos, size=size, color=color, pxMode=False)
# sp1.translate(5,5,0)
w.addItem(sp1)


if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()