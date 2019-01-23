from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys
import time


class Visualizer:
    def __init__(self):
        self.traces = {}
        self.app = QtGui.QApplication(sys.argv)
        self.w = gl.GLViewWidget()
        self.w.opts['distance'] = 40
        self.w.setGeometry(0, 110, 1920, 1080)
        self.w.show()

        self.phase = 0
        self.lines = 100
        self.points = 100
        self.y = np.linspace(-10, 10, self.lines)
        self.x = np.linspace(-10, 10, self.points)

        for i, line in enumerate(self.y):
            self.traces[i] = gl.GLLinePlotItem()
            self.w.addItem(self.traces[i])

    def set_plotdata(self, name, points, color, width):
        self.traces[name].setData(pos=points, color=color, width=width)

    def update(self):
        for i, line in enumerate(self.y):
            y = np.array([line] * self.points)

            amp = 10 / (i + 1)
            phase = self.phase * (i + 1) - 10
            freq = self.x * (i + 1) / 10

            sine = amp * np.sin(freq - phase)
            pts = np.vstack([self.x, y, sine]).transpose()

            print('i', i, 'self.lines', self.lines)
            print(pg.glColor((i, self.lines*4)))
            self.set_plotdata(
                name=i, points=pts,
                color=pg.glColor((i, self.lines * 4)),
                width=1)
            self.phase -= .0002

    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(10)
        QtGui.QApplication.instance().exec_()


if __name__ == '__main__':
    v = Visualizer()
    v.animation()