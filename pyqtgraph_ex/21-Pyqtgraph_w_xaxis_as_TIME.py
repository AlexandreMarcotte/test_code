import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import numpy as np
from collections import deque
from time import time

init_t = time()
win = pg.GraphicsWindow()
p1 = win.addPlot()
N_DATA = 100
data_queue = deque(np.zeros(N_DATA), maxlen=N_DATA)
time_queue = deque(np.zeros(N_DATA), maxlen=N_DATA)
curve1 = p1.plot(time_queue, data_queue)

def update():
    global data1, curve1, ptr1, init_t
    data_queue.append(np.random.normal())
    time_queue.append(time() - init_t)
    curve1.setData(time_queue, data_queue)

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
