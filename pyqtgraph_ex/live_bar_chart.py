import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import numpy as np

win = pg.GraphicsWindow()
p1 = win.addPlot()




x = np.arange(10)
y = np.sin(x)
bg1 = pg.BarGraphItem(x=x, height=y, width=1, brush='b')
wave_plot.addItem(bg1)

curve1 = p1.plot(bg1)

def update():
    # global data1, curve1
    # data1[:-1] = data1[1:]
    # data1[-1] = np.random.normal()
    # curve1.setData(data1)
    pass







timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
