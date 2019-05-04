# -*- coding: utf-8 -*-
"""
Demonstrates use of GLScatterPlotItem with rapidly-updating plots.

"""


from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
from collections import deque


app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 20
w.show()
w.setWindowTitle('ScatterPlot')

g = gl.GLGridItem()
w.addItem(g)


sps = deque(np.array([]))
n_added = 0
def update():
    print('here')
    global sp3, pos, phase, color, sps, n_added, n
    n_added += 1
    # print(n_added)

    sp_item = SpItem()
    sps.append(sp_item)
    for sp in sps:
        sp.item.translate(0, 0.1, 0)

    w.addItem(sps[-1].item)
    if len(sps) > 50:
        w.removeItem(sps.popleft().item)


class SpItem:
    def __init__(self):
        self.n = 1000
        self.z_max = 10
        self.ratio = self.n / self.z_max
        self.zs = 0

        self.pos = self.init_pos()

        self.item = gl.GLScatterPlotItem(
                pos=self.pos, color=(1, 1, 1, .3), size=3, pxMode=True)
        self.color = self.init_color()

    def init_pos(self):
        xs = np.linspace(-5, 5, self.n)
        ys = np.ones(self.n) * -10
        self.zs = np.linspace(-100, self.z_max, self.n) + np.random.normal(1)
        # self.zs_max = max(self.zs)
        pos = np.stack((xs, ys, self.zs), axis=1)
        return pos

    def init_color(self):
        color = np.empty((self.n, 4))
        for i, z in enumerate(self.zs):
            # print('i', i, 'z', z, 'self.zs_max', self.z_max)
            # print('COLOR', pg.glColor((int(z), )))
            # print(int(z*self.ratio), int(self.z_max*self.ratio))
            color[i] = pg.glColor((int(z*self.ratio), int(self.z_max*self.ratio)*4))
            # print(color[i])
        self.item.setData(pos=self.pos, color=color)


if __name__ == '__main__':
    t = QtCore.QTimer()
    t.timeout.connect(update)
    t.start(100)
    QtGui.QApplication.instance().exec_()


