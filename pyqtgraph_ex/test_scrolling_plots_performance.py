# -*- coding: utf-8 -*-
"""
Various methods of drawing scrolling plots.
"""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from random import random
from collections import deque

win = pg.GraphicsWindow()
win.setWindowTitle('pyqtgraph example: Scrolling Plots')

# # 1) Simplest approach -- update data in the array such that plot appears to scroll
# #    In these examples, the array size is fixed.
# p1 = win.addPlot()
# p2 = win.addPlot()
# data1 = np.random.normal(size=300)
# curve1 = p1.plot(data1)
# curve2 = p2.plot(data1)
# ptr1 = 0
#
#
# def update1():
#     global data1, curve1, ptr1
#     data1[:-1] = data1[1:]  # shift data in the array one sample left
#     # (see also: np.roll)
#     data1[-1] = np.random.normal()
#     curve1.setData(data1)
#
#     ptr1 += 1
#     curve2.setData(data1)
#     curve2.setPos(ptr1, 0)
#
#
# # 2) Allow data to accumulate. In these examples, the array doubles in length
# #    whenever it is full.
# win.nextRow()
# p3 = win.addPlot()
# p4 = win.addPlot()
# # Use automatic downsampling and clipping to reduce the drawing load
# p3.setDownsampling(mode='peak')
# p4.setDownsampling(mode='peak')
# p3.setClipToView(True)
# p4.setClipToView(True)
# p3.setRange(xRange=[-100, 0])
# p3.setLimits(xMax=0)
# curve3 = p3.plot()
# curve4 = p4.plot()
#
# data3 = np.empty(100)
# ptr3 = 0
#
#
# def update2():
#     global data3, ptr3
#     data3[ptr3] = np.random.normal()
#     ptr3 += 1
#     if ptr3 >= data3.shape[0]:
#         tmp = data3
#         data3 = np.empty(data3.shape[0] * 2)
#         data3[:tmp.shape[0]] = tmp
#     curve3.setData(data3[:ptr3])
#     curve3.setPos(-ptr3, 0)
#     curve4.setData(data3[:ptr3])


# 3) Plot in chunks, adding one new plot curve for every 100 samples


class BasicScroll:
    def __init__(self, win):
        win.nextRow()
        p = win.addPlot(colspan=2)
        self.d1 = deque(np.zeros(1000), maxlen=1000)
        self.c1 = p.plot(self.d1)

    def update(self):
        self.d1.append(random())
        self.c1.setData(self.d1)

class ChunkPlot:
    def __init__(self, win):
        self.chunkSize = 100
        # Remove chunks after we have 10
        self.maxChunks = 10
        self.startTime = pg.ptime.time()
        win.nextRow()
        self.p5 = win.addPlot(colspan=2)
        self.p5.setLabel('bottom', 'Time', 's')
        self.p5.setXRange(-10, 0)
        self.curves = []
        self.data5 = np.empty((self.chunkSize + 1, 2))
        self.ptr5 = 0

    def update(self):
        now = pg.ptime.time()
        for c in self.curves:
            c.setPos(-(now - self.startTime), 0)

        i = self.ptr5 % self.chunkSize
        if i == 0:
            curve = self.p5.plot()
            self.curves.append(curve)
            last = self.data5[-1]
            self.data5 = np.empty((self.chunkSize + 1, 2))
            self.data5[0] = last
            while len(self.curves) > self.maxChunks:
                c = self.curves.pop(0)
                self.p5.removeItem(c)
        else:
            curve = self.curves[-1]
        self.data5[i + 1, 0] = now - self.startTime
        self.data5[i + 1, 1] = np.random.normal()
        curve.setData(x=self.data5[:i + 2, 0], y=self.data5[:i + 2, 1])
        self.ptr5 += 1

chunk_plots = []
for _ in range(8):
    # chunk_plots.append(ChunkPlot(win))
    chunk_plots.append(BasicScroll(win))

# update all plots
def update():
    # update1()
    # update2()
    for chunk_plot in chunk_plots:
        chunk_plot.update()



timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
