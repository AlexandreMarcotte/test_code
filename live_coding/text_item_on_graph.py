import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

x = np.linspace(-20, 20, 1000)
y = np.sin(x) / x
plot = pg.plot()  ## create an empty plot widget
plot.setYRange(-1, 2)
plot.setWindowTitle('pyqtgraph example: text')
curve = plot.plot(x, y)  ## add a single curve

## Set up an animated arrow and text that track the curve
curvePoint = pg.CurvePoint(curve)
plot.addItem(curvePoint)
text2 = pg.TextItem("test", anchor=(0.5, -1.0))
text2.setParentItem(curvePoint)
arrow2 = pg.ArrowItem(angle=90)
arrow2.setParentItem(curvePoint)

## update position every 10ms
index = 0

def update():
    global curvePoint, index
    # index = (index + 1) % len(x)
    index = 100
    curvePoint.setPos(float(index) / (len(x) - 1))
    text2.setText('Event type 1')

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
