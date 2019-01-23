from pyqtgraph.Qt import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow
import pyqtgraph as pg
import numpy as np


class Constructor3D:
    def __init__(self):
        self.init_win()

    def init_win(self):
        app = QtGui.QApplication([])
        mw = QtGui.QMainWindow()
        mw.resize(800,800)
        view = pg.GraphicsLayoutWidget()
        mw.setCentralWidget(view)
        mw.show()
        w = view.addPlot()
        n = 300
        s = pg.ScatterPlotItem(
            size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))
        pos = np.random.normal(size=(2,n), scale=1)
        spots = [{'pos': pos[:,i]} for i in range(n)]
        s.addPoints(spots)
        w.addItem(s)

        self.lastClicked = []

        s.sigClicked.connect(self.clicked)

        QtGui.QApplication.instance().exec_()

    def clicked(self, plot, points):
        for p in self.lastClicked:
            p.resetPen()
        for p in points:
            p.setPen('b', width=2)
            print('pos: ', p.pos())
        self.lastClicked = points


if __name__ == '__main__':
    constructor_3D = Constructor3D()




#
# from pyqtgraph.Qt import QtGui, QtCore
# import pyqtgraph as pg
# import numpy as np
#
# class Constructor3D:
#     def __init__(self):
#         self.w = self.initUI()
#
#         self.lastClicked = []
#         self.create_pts()
#         self.start_application()
#
#     def initUI(self):
#         self.app = QtGui.QApplication([])
#         mw = QtGui.QMainWindow()
#         mw.resize(800, 800)
#         view = pg.GraphicsLayoutWidget()
#         mw.setCentralWidget(view)
#         mw.show()
#         w = view.addPlot()
#         return w
#
#     def create_pts(self):
#         n = 300
#         s = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None),
#                                brush=pg.mkBrush(255, 255, 255, 120))
#         pos = np.random.normal(size=(2,n), scale=1)
#         spots = [{'pos': pos[:,i]} for i in range(n)]
#         s.addPoints(spots)
#         self.w.addItem(s)
#         s.sigClicked.connect(self.clicked)
#
#     def clicked(plot, points):
#         global lastClicked
#         for p in lastClicked:
#             p.resetPen()
#         for p in points:
#             p.setPen('b', width=2)
#             print('pos: ', p.pos())
#         lastClicked = points
#
#     def start_application(self):
#         QtGui.QApplication.instance().exec_()
#
#
# if __name__ == '__main__':
#     constructor_3d = Constructor3D()
#
#
#
#
#
# app = QtGui.QApplication([])
# mw = QtGui.QMainWindow()
# mw.resize(800,800)
# view = pg.GraphicsLayoutWidget()
# mw.setCentralWidget(view)
# mw.show()
#
# w = view.addPlot()
# n = 300
# s = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None),
#                        brush=pg.mkBrush(255, 255, 255, 120))
# pos = np.random.normal(size=(2,n), scale=1)
# spots = [{'pos': pos[:,i]} for i in range(n)]
# s.addPoints(spots)
# w.addItem(s)
#
# lastClicked = []
# def clicked(plot, points):
#     global lastClicked
#     for p in lastClicked:
#         p.resetPen()
#     for p in points:
#         p.setPen('b', width=2)
#         print('pos: ', p.pos())
#     lastClicked = points
#
# s.sigClicked.connect(clicked)
#
#
# if __name__ == '__main__':
#     QtGui.QApplication.instance().exec_()
