from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np

app = QtGui.QApplication([])
view = pg.GraphicsView()
l = pg.GraphicsLayout(border=(100,100,100))
view.setCentralItem(l)
view.show()

l.addLabel('txt', col=1, colspan=4)
l.nextRow()

## Put vertical label on left side
l.addLabel('Long Vertical Label', angle=-90, rowspan=2)

## Add 3 plots into the first row (automatic position)
p1 = l.addPlot(title="Plot 1")
vb = l.addViewBox(lockAspect=True)
img = pg.ImageItem(np.random.normal(size=(100,100)))
vb.addItem(img)
vb.autoRange()


## Add a sub-layout into the second row (automatic position)
## The added item should avoid the first column, which is already filled
l.nextRow()
l2 = l.addLayout(colspan=3, border=(50,0,0))
l2.setContentsMargins(10, 10, 10, 10)
l2.addLabel("shared axes and axis labels", colspan=3)
l2.nextRow()
l2.addLabel('Vertical Axis Label', angle=-90, rowspan=2)
p21 = l2.addPlot()
p22 = l2.addPlot()
l2.nextRow()
l2.addLabel("Horizontal Axis Label", col=1, colspan=2)

p1.plot([1,3,2,4,3,5])


if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
