# -*- coding: utf-8 -*-
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import pyqtgraph.console
import numpy as np
from pyqtgraph.dockarea import *

app = QtGui.QApplication([])
win = QtGui.QMainWindow()
area = DockArea()
win.setCentralWidget(area)
win.resize(1000, 500)

d1 = Dock("Dock1 - Plot", size=(500,200))
d2 = Dock("Dock2 - Plot", size=(500,200))
area.addDock(d1)
area.addDock(d2, 'above', d1)

w1 = pg.PlotWidget(title="Dock 4 plot")
w1.plot(np.random.normal(size=100))
d1.addWidget(w1)

w2 = pg.PlotWidget(title="Dock 4 plot")
w2.plot(np.random.normal(size=100))
d2.addWidget(w2)

win.show()

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
