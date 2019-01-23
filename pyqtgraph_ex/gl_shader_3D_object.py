# -*- coding: utf-8 -*-
"""
Demonstration of some of the shader programs included with pyqtgraph that can be
used to affect the appearance of a surface.
"""

## Add path to library (just for examples; you do not need this)

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl

# pg.mkBrush()

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GL Shaders')
w.setCameraPosition(distance=15, azimuth=-90)

g = gl.GLGridItem()
g.scale(2, 2, 1)
w.addItem(g)

import numpy as np

md = gl.MeshData.sphere(rows=10, cols=20)
x = np.linspace(-8, 8, 6)

m1 = gl.GLMeshItem(meshdata=md, smooth=True, color=(1, 0, 0, 0.2),
                   shader='balloon', glOptions='additive')
m1.translate(x[0], 0, 0)
m1.scale(1, 1, 2)
w.addItem(m1)

m2 = gl.GLMeshItem(meshdata=md, smooth=True, shader='normalColor', glOptions='opaque')
m2.translate(x[1], 0, 0)
m2.scale(1, 1, 2)
w.addItem(m2)

m3 = gl.GLMeshItem(meshdata=md, smooth=True, shader='viewNormalColor', glOptions='opaque')
m3.translate(x[2], 0, 0)
m3.scale(1, 1, 2)
w.addItem(m3)

m4 = gl.GLMeshItem(meshdata=md, smooth=True, shader='shaded', glOptions='opaque')
m4.translate(x[3], 0, 0)
m4.scale(1, 1, 2)
w.addItem(m4)

m5 = gl.GLMeshItem(meshdata=md, smooth=True, color=(1, 0, 0, 1), shader='edgeHilight', glOptions='opaque')
m5.translate(x[4], 0, 0)
m5.scale(1, 1, 2)
w.addItem(m5)

m6 = gl.GLMeshItem(meshdata=md, smooth=True, color=(1, 0, 0, 1), shader='heightColor', glOptions='opaque')
m6.translate(x[5], 0, 0)
m6.scale(1, 1, 2)
w.addItem(m6)

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
