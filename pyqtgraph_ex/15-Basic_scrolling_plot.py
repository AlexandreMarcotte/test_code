import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import numpy as np
from collections import deque
from random import random


class BasicScroll:
    def __init__(self, win):
        plot = win.addPlot()
        self.deque = deque(np.zeros(100), maxlen=100)
        self.curve = plot.plot()

    def start_timer(self):
        timer = pg.QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(10)
        return timer

    def update(self):
        self.deque.append(random())
        self.curve.setData(self.deque)


if __name__ == '__main__':

    win = pg.GraphicsWindow()
    basic_scroll = BasicScroll(win)
    timer = basic_scroll.start_timer()

    QtGui.QApplication.instance().exec_()

