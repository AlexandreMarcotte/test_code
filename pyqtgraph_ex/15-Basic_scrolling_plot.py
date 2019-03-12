import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import numpy as np
from collections import deque
from random import random


class BasicScroll:
    def __init__(self, win):
        p = win.addPlot()
        self.d = deque(np.zeros(100), maxlen=100)
        self.c = p.plot()

    def update(self):
        self.d.append(random())
        self.c.setData(self.d)


def start_timer(scroll_plot):
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(scroll_plot.update)
    timer.start(10)
    return timer


if __name__ == '__main__':

    win = pg.GraphicsWindow()
    basic_scroll = BasicScroll(win)
    timer = start_timer(basic_scroll)

    QtGui.QApplication.instance().exec_()

