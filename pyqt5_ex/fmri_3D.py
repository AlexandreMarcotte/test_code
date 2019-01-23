"""Test GL volume tool with MRI data.
   from: ofgulban
   on github: https://gist.github.com/ofgulban/a5c23bbcb843d690fa07038e5b7a4801"""

from pyqtgraph.Qt import QtGui
import pyqtgraph.opengl as gl
import numpy as np
from nibabel import load

# get MRI data
nii = load('inplane001.nii')
data = nii.get_data()
data = np.repeat(data, repeats=4, axis=2)
# create qtgui
app = QtGui.QApplication([])

w = gl.GLViewWidget()
w.setCameraPosition(0, 0, 90)
w.opts['distance'] = 500
w.show()
w.setWindowTitle('pyqtgraph example: GLVolumeItem')

# create color image channels
d2 = np.empty(data.shape + (4,), dtype=np.ubyte)
d2[..., 0] = data * (255./(data.max()/1))
d2[..., 1] = d2[..., 0]
d2[..., 2] = d2[..., 0]
d2[..., 3] = d2[..., 0]
d2[..., 3] = (d2[..., 3].astype(float) / 255.)**2 * 255

# RGB orientation lines (optional)
d2[:, 0, 0] = [255, 0, 0, 255]
d2[0, :, 0] = [0, 255, 0, 255]
d2[0, 0, :] = [0, 0, 255, 255]

v = gl.GLVolumeItem(d2, sliceDensity=1, smooth=False)
v.translate(-d2.shape[0]/2, -d2.shape[1]/2, -150)
w.addItem(v)

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()












#
#
#
#
# from pyqtgraph.Qt import QtCore, QtGui
# import pyqtgraph.opengl as gl
# import numpy as np
#
# app = QtGui.QApplication([])
# w = gl.GLViewWidget()
# w.opts['distance'] = 20
# w.show()
# w.setWindowTitle('pyqtgraph example: GLScatterPlotItem')
#
# g = gl.GLGridItem()
# w.addItem(g)
#
# pos = np.empty((53, 3))
# size = np.empty((53))
# color = np.empty((53, 4))
# pos[0] = (1, 0, 0)
# size[0] = 0.5
# color[0] = (1.0, 0.0, 0.0, 0.5)
#
# sp1 = gl.GLScatterPlotItem(pos=pos, size=size, color=color, pxMode=False)
# w.addItem(sp1)
#
# ##
# ##  Second example shows a volume of points with rapidly updating color
# ##  and pxMode=True
# ##
#
# pos = np.random.random(size=(100000, 3))
# pos *= [10, -10, 10]
# pos[0] = (0, 0, 0)
# color = np.ones((pos.shape[0], 4))
# d2 = (pos ** 2).sum(axis=1) ** 0.5
# size = np.random.random(size=pos.shape[0]) * 10
# sp2 = gl.GLScatterPlotItem(pos=pos, color=(1, 1, 1, 1), size=size)
# phase = 0.
#
# w.addItem(sp2)
#
# ##
# ##  Third example shows a grid of points with rapidly updating position
# ##  and pxMode = False
# ##
#
# pos3 = np.zeros((100, 100, 3))
# pos3[:, :, :2] = np.mgrid[:100, :100].transpose(1, 2, 0) * [-0.1, 0.1]
# pos3 = pos3.reshape(10000, 3)
# d3 = (pos3 ** 2).sum(axis=1) ** 0.5
#
# sp3 = gl.GLScatterPlotItem(pos=pos3, color=(1, 1, 1, .3), size=0.1, pxMode=False)
#
# w.addItem(sp3)
#
#
# def update():
#     ## update volume colors
#     global phase, sp2, d2
#     s = -np.cos(d2 * 2 + phase)
#     color = np.empty((len(d2), 4), dtype=np.float32)
#     color[:, 3] = np.clip(s * 0.1, 0, 1)
#     color[:, 0] = np.clip(s * 3.0, 0, 1)
#     color[:, 1] = np.clip(s * 1.0, 0, 1)
#     color[:, 2] = np.clip(s ** 3, 0, 1)
#     sp2.setData(color=color)
#     phase -= 0.1
#
#     ## update surface positions and colors
#     global sp3, d3, pos3
#     z = -np.cos(d3 * 2 + phase)
#     pos3[:, 2] = z
#     color = np.empty((len(d3), 4), dtype=np.float32)
#     color[:, 3] = 0.3
#     color[:, 0] = np.clip(z * 3.0, 0, 1)
#     color[:, 1] = np.clip(z * 1.0, 0, 1)
#     color[:, 2] = np.clip(z ** 3, 0, 1)
#     sp3.setData(pos=pos3, color=color)
#
#
# t = QtCore.QTimer()
# t.timeout.connect(update)
# t.start(50)
#
# if __name__ == '__main__':
#     QtGui.QApplication.instance().exec_()
