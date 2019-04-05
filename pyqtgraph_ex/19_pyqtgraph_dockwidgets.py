
from pyqtgraph.dockarea.Dock import DockLabel

def updateStylePatched(self):
    r = '3px'
    if self.dim:
        fg = '#b0b0b0'
        bg = '#94f5bb'
        border = '#94f5bb'
        # border = '#7cf3ac'
    else:
        fg = '#fff'
        bg = '#10b151'
        border = '#10b151'

    if self.orientation == 'vertical':
        self.vStyle = """DockLabel {
            background-color : %s;
            color : %s;
            border-top-right-radius: 0px;
            border-top-left-radius: %s;
            border-bottom-right-radius: 0px;
            border-bottom-left-radius: %s;
            border-width: 0px;
            border-right: 2px solid %s;
            padding-top: 3px;
            padding-bottom: 3px;
            font-size: 18px;
        }""" % (bg, fg, r, r, border)
        self.setStyleSheet(self.vStyle)
    else:
        self.hStyle = """DockLabel {
            background-color : %s;
            color : %s;
            border-top-right-radius: %s;
            border-top-left-radius: %s;
            border-bottom-right-radius: 0px;
            border-bottom-left-radius: 0px;
            border-width: 0px;
            border-bottom: 2px solid %s;
            padding-left: 13px;
            padding-right: 13px;
            font-size: 18px
        }""" % (bg, fg, r, r, border)
        self.setStyleSheet(self.hStyle)


DockLabel.updateStyle = updateStylePatched
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
