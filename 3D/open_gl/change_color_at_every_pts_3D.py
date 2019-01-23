from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np
from collections import deque

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
w.setCameraPosition(distance=200)

a = 10
cols = 20
rows = 1000

x = np.linspace(-8, 8, cols).reshape(cols,1)
y = np.linspace(-8, 8, rows).reshape(1,rows)

p = gl.GLSurfacePlotItem(x=x[:,0], y=y[0,:], shader='heightColor', computeNormals=False, smooth=False)
p.shader()['colorMap'] = np.array([-1, -1, -1, 0, 0, 0, 1, 1, 1])
w.addItem(p)

def update():
    global p
    # p.setData(z=a * (np.random.random((cols, rows)) - 0.5))
    p.setData(z=a * np.array(deque(deque(np.random.random(rows) for _ in range(cols)))))

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(100)

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
