# 'calculate' function is an inside-class thread and main thread use calculated self.y array
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import my_threading
# from Queue import Queue
import time
from random import randint

class MyApp(my_threading.Thread):
    def __init__(self):
        super(MyApp, self).__init__()
        self.qapp = pg.mkQApp()
        self.win = pg.GraphicsWindow()
        plot1 = self.win.addPlot()
        curve = plot1.plot()
        self.i = 0
        self.n_steps = 100

        while self.win.isVisible():
            curve.setData(x, y)
            self.qapp.processEvents()


class CreateData(my_threading.Thread):
    def __init__(self):
        super(CreateData, self).__init__()

    def run(self):
        while 1:
            time.sleep(0.1)
            y[randint(0, 100-1)] = randint(-1, 1)
# class PlotData(my_threading.Thread):
#     """
#     Ploting data with pyqtgraph under a class format
#     """
#     def __init__(self):
#         super(PlotData, self).__init__()
#         # Set pyqtgraph elements
#         self._win = pg.GraphicsWindow()
#         self._p = self._win.addPlot()
#         self._p.setXRange(-10, 0)
#
#         # self.dataQueue = dataQueue
#         self._startTime = pg.ptime.time()
#         self._chunkSize = 100  # size of _data
#         self._maxChunks = 10  # number of chunk of data to plot
#         self._curves = []
#         self._data = np.empty((self._chunkSize + 1, 2))  # 2D => first: time / second: data
#         self._ptr = 0  # keep track of total number of iterations
#
#     def update(self):
#         now = pg.ptime.time()
#         # There is up to _maxChunks _curves that can be in _curves list
#         for c in self._curves:
#             c.setPos(-(now - self._startTime), 0)
#
#         i = self._ptr % self._chunkSize
#         # One time every self._chunksize steps
#         if i == 0:
#             curve = self._p.plot(pen='g')  # create a new curve object
#             self._curves.append(curve)  # append this new curve to _curves list
#             last = self._data[-1]
#             self._data[0] = last  # move the last data value to the first place
#             while len(self._curves) > self._maxChunks:
#                 c = self._curves.pop(0)  # remove the excess curve
#                 self._p.removeItem(c)
#         # The vast majority of the time (all except one)
#         else:
#             curve = self._curves[-1]
#
#         self._data[i + 1, 0] = now - self._startTime  # time elapse since beginning
#         self._data[i + 1, 1] = np.random.normal()     # create random data
#
#         curve.setData(x=self._data[:i + 2, 0], y=self._data[:i + 2, 1])
#         self._ptr += 1
#
#
#     def run(self):
#         timer = pg.QtCore.QTimer()
#         timer.timeout.connect(self.update)
#         timer.start(0)
#
#         QtGui.QApplication.instance().exec_()
#
#
# class PrintShit(my_threading.Thread):
#     def __init__(self):
#         super(PrintShit, self).__init__()
#
#     def run(self):
#         while 1:
#             print('cool les dudesssss')
#             time.sleep(0.1)


if __name__ == '__main__':

    n_steps = 100
    # starting value in the graph
    x = np.linspace(0, n_steps, n_steps)
    y = np.zeros(n_steps)

    play = CreateData()
    play.start()

    m = MyApp()
    m.start()
    # p = PlotData()
    # p.run()








