import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

pg.setConfigOptions(imageAxisOrder='row-major')

## Create image to display
arr = np.ones((100, 100), dtype=float)
arr[45:55, 45:55] = 0
arr[25, :] = 5
arr[:, 25] = 5
arr[75, :] = 5
arr[:, 75] = 5
arr[50, :] = 10
arr[:, 50] = 10
arr += np.sin(np.linspace(0, 20, 100)).reshape(1, 100)
arr += np.random.normal(size=(100,100))

# add an arrow for asymmetry
arr[10, :50] = 10
arr[9:12, 44:48] = 10
arr[8:13, 44:46] = 10


## create GUI
app = QtGui.QApplication([])
w = pg.GraphicsWindow(size=(1000,800), border=True)
w.setWindowTitle('pyqtgraph example: ROI Examples')

text = """Data Selection From Image.<br>\n
Drag an ROI or its handles to update the selected image.<br>
Hold CTRL while dragging to snap to pixel boundaries<br>
and 15-degree rotation angles.
"""

text = """Transforming objects with ROI"""
w4 = w.addLayout(row=0, col=0)
label4 = w4.addLabel(text, row=0, col=0)
v4 = w4.addViewBox(row=1, col=0, lockAspect=True)
# grid
g = pg.GridItem()
v4.addItem(g)
# text
txt = pg.TextItem('this is text')
txt.setPos(10, 0)
txt.rotateAxis(90)
v4.addItem(txt)
# vertical lines
for i in range(3):
    l = pg.InfiniteLine(10*i)
    v4.addItem(l)





# line item
# pen = pg.mkPen(width=0.1)
# font
font=QtGui.QFont()
font.setPixelSize(10)

axis = pg.AxisItem(orientation='right')
axis.setLabel(labelStyle = {'color': '#F06', 'font-size': '6pt'})
# axis.getAxis("left").tickFont = font
v4.addItem(axis)

r4 = pg.ROI([0,0], [100,100], removable=True)
r4.addRotateHandle([1,0], [0.5, 0.5])
r4.addRotateHandle([0,1], [0.5, 0.5])
img4 = pg.ImageItem(arr)
v4.addItem(r4)
img4.setParentItem(r4)

v4.disableAutoRange('xy')
v4.autoRange()

if __name__ == '__main__':
        QtGui.QApplication.instance().exec_()
