from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from functools import partial
from numpy import sin, pi

app = QtGui.QApplication([])

vb = pg.ViewBox()
vb.setAspectLocked()
img = pg.ImageItem()
vb.addItem(img)
# vb.setRange(QtCore.QRectF(100, 0, 500, 500))

win = pg.plot()
win.show()
win.setCentralWidget(vb)

def mkData():
    width = 125
    height = 50
    dt = np.uint8
    loc = 0
    scale = 640

    # t = np.linspace(0, 2 * pi, height)
    # m = 1000
    # s = m * sin(20 * t)
    data = np.random.normal(size=(100, width, height, 3),
                            loc=loc, scale=scale)
    # data = []
    # for i in range(width):
    #     data.append(s)
    # data = np.array(data)

    data = data.astype(dt)
    return data

data = mkData()
ptr = 0
def update(data):
    global ptr, img
    img.setImage(data[ptr%data.shape[0]],
                 autoLevels=False, levels=None,
                 lut=None, autoDownsample=False)
    ptr += 1
    # app.processEvents()  ## force complete redraw for every plot

timer = QtCore.QTimer()
timer.timeout.connect(partial(update, data))
timer.start(100)

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
