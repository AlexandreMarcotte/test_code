from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import time
import sys


class GuiThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.status = True
        self.app = QtGui.QApplication(sys.argv)
        self.app.aboutToQuit.connect(self.stop)
        self.win = pg.GraphicsWindow(title="Example")
        self.win.resize(500, 400)
        pg.setConfigOptions(antialias=True)
        self.px = self.win.addPlot(title="X plot")
        self.ckx = self.px.plot(pen='y')
        self.cdx = self.px.plot(pen='r')
        self.range = 100
        self.px.setXRange(0, self.range)
        self.px.setYRange(-180, 180)
        self.px.showGrid(x=True, y=True)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateplot)
        self.timer.start(0.001)
        self.kx = np.zeros(self.range)
        self.dx = np.zeros(self.range)

    def updateplot(self):
        self.ckx.setData(self.kx)
        self.cdx.setData(self.dx)

    def append(self, sin):
        self.kx = np.roll(self.kx, -1)
        self.kx[-1] = sin[0]
        self.dx = np.roll(self.dx, -1)
        self.dx[-1] = int(sin[1])

    def stop(self):
        print("Exit")  # exit when window closed
        self.status = False
        sys.exit()

    def run(self):
        print("run")  # Qthread run
        while self.status:
            sin = np.random.randint(-180, 180, 2)
            self.append(sin)  # append random number for plot
            time.sleep(0.01)


import time
import my_threading


class TimeThread (my_threading.Thread):
    def __init__(self, name):
        my_threading.Thread.__init__(self)
        self.name = name
        self.t = time.time()
        self.elapsed = 0

    def run(self):
        print("thread start")
        while 1:
            self.elapsed = time.time()-self.t
            time.sleep(1)
            print(self.name, self.elapsed)


if __name__ == '__main__':
    t1 = GuiThread()
    t1.start()
    t2 = TimeThread("t1")
    t2.start()