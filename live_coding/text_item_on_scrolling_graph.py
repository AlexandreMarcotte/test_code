import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import numpy as np

win = pg.GraphicsWindow()
plot = win.addPlot()
x = np.random.normal(size=300)
curve = plot.plot(x)

# -- arrow text:
curvePoint = pg.CurvePoint(curve)
plot.addItem(curvePoint)
txt = pg.TextItem("test", anchor=(0.5, -1.0))
txt.setParentItem(curvePoint)
arrow = pg.ArrowItem(angle=90)
arrow.setParentItem(curvePoint)

i = len(x)
def update_graph():
    global x, curve
    x[:-1] = x[1:]
    x[-1] = np.random.normal()
    curve.setData(x)

    global curvePoint, i, plot
    i -= 1
    index = float(i) / (len(x) - 1)
    curvePoint.setPos(index)
    txt.setText('Type 1')

# i = 0
# def update_txt():
#     global curvePoint, i
#     i += 1
#     index = float(i) / (len(x) - 1)
#     curvePoint.setPos(index)
#     txt.setText('Type 1')
# -------

timer_graph = pg.QtCore.QTimer()
timer_graph.timeout.connect(update_graph)
timer_graph.start(50)

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()


#%%
import numpy as np
from copy import deepcopy

x = np.zeros(10)
x[4] = 10
x[6] = 43
print(np.nonzero(x)[0])