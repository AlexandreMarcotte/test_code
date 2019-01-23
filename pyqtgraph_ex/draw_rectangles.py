# https://groups.google.com/forum/#!msg/pyqtgraph/O-d2L6qfPoo/i1zedC2Oda4J
# from Nicholas Tan Jerome

from PyQt5 import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import ctypes, sys
from ctypes.util import find_library
import sip

if sys.platform == 'win32':
    qtlib = ctypes.windll.qtgui4
    drawPoints = getattr(qtlib, '?drawPoints@QPainter@@QEAAXPEBVQPointF@@H@Z')
else:
    """
    pwd: /usr/lib/i386-linux-gnu
    list: nm -D ./libQtGui.so.4 > ~./list.txt
    """
    qtlib = ctypes.cdll.LoadLibrary(find_library("QtGui"))
    drawPoints = getattr(qtlib, '_ZN8QPainter10drawPointsEPK7QPointFi')
    drawRects = getattr(qtlib, '_ZN8QPainter9drawRectsEPK6QRectFi')


class SquareItem(QtGui.QGraphicsItem):
    def __init__(self, x=None, y=None, w=None, h=None):
        QtGui.QGraphicsItem.__init__(self)
        self.setData(x, y, w, h)

    def setData(self, x, y, w, h):
        if x is None:
            x = np.array([])
            y = np.array([])
        self.data = np.empty((len(x), 4), dtype=np.float)
        self.data[:, 0] = x
        self.data[:, 1] = y
        self.data[:, 2] = w
        self.data[:, 3] = h
        xmin = x.min()
        xmax = x.max()
        ymin = y.min()
        ymax = y.max()
        self.bounds = QtCore.QRectF(xmin, ymin, xmax - xmin, ymax - ymin)
        self.prepareGeometryChange()

    def boundingRect(self):
        return self.bounds

    def paint(self, p, *args):
        p.setPen(pg.mkPen((255, 255, 255, 80)))
        p.setBrush(pg.mkBrush((0, 255, 0, 255)))
        ptr = ctypes.c_void_p(sip.unwrapinstance(p))
        drawRects(ptr, self.data.ctypes, self.data.shape[0])


if __name__ == '__main__':
    app = QtGui.QApplication([])
    w1 = pg.PlotWidget()
    x = np.linspace(0, 100, 100)
    y = np.zeros(100)
    w = 0.1 * np.ones(100)
    h = np.ones(100)
    p = SquareItem(x, y, w, h)
    w1.addItem(p)
    w1.show()
    app.exec_()


#%%
import random
print(random.randrange(10))