from pyqtgraph.Qt import QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys

#%%
class Visualizer:
    def __init__(self):
        self.w = self.create_win()
        self.w.show()

    def create_win(self):
        self.app = QtGui.QApplication(sys.argv)
        w = gl.GLViewWidget()
        w.opts['distance'] = 40
        return w

    def add_data(self, z, translate=(0, 0, 0)):
        self.N_PTS = len(z)
        x = np.linspace(0, self.N_PTS, self.N_PTS)
        y = np.ones(self.N_PTS)
        pts = np.vstack([x, y, z]).transpose()

        self.line_item = gl.GLLinePlotItem()
        self.line_item.translate(*translate)
        self.w.addItem(self.line_item)
        self.line_item.setData(pos=pts, color=pg.glColor((1, 20)), width=1)


if __name__ == '__main__':
    v = Visualizer()
    for i in range(20):
        z = np.random.random(i + 1) * 10
        v.add_data(z, (0, i, 0))
    QtGui.QApplication.instance().exec_()
