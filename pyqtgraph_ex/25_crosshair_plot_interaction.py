# self.crosshair_plot = pg.PlotWidget()
#
# data1 = np.random.random(size=1000)
# self.crosshair_plot.plot(data1, pen="w")
#
# row = 0;
# col = 1;
# rowspan = 1;
# colspan = 1
# self.tab3.layout.addWidget(self.crosshair_plot, row,
#                            col, rowspan, colspan)




import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

#generate layout
app = QtGui.QApplication([])
win = pg.GraphicsWindow()
win.setWindowTitle('pyqtgraph example: crosshair')

# Add the label to show the 'y' position on the plot at the 'x' value of the cross hair
label = pg.LabelItem(justify='right')
win.addItem(label)

# Instanciate the plot containing the crosshair
crosshair_plot = win.addPlot(row=0, col=0)
# Instanciate the plot containing all the data
all_data_plot = win.addPlot(row=0, col=1)

# Region of selection in the 'all_data_plot'
region = pg.LinearRegionItem()

# Tell the ViewBox to exclude this item when doing auto-range calculations.
all_data_plot.addItem(region, ignoreBounds=True)
crosshair_plot.setAutoVisible(y=True)

# Create data
data1 = np.random.random(size=1000)
all_data_plot.plot(data1, pen="w")

data2 = np.random.random(size=1000)
crosshair_plot.plot(data2, pen="g")

def update_cross_hair_plot_range():
    """ Update the cross_hair_plot range based on the region position """
    minX, maxX = region.getRegion()
    crosshair_plot.setXRange(minX, maxX, padding=0)

region.sigRegionChanged.connect(update_cross_hair_plot_range)

def update_region(window, viewRange):
    """ Update the range of the region"""
    rgn = viewRange[0]
    region.setRegion(rgn)

crosshair_plot.sigRangeChanged.connect(update_region)

# Set the starting position of the region
region.setRegion([0, 200])

#Create the cross hair and add it to the window
vLine = pg.InfiniteLine(angle=90, movable=False)
hLine = pg.InfiniteLine(angle=0, movable=False)
crosshair_plot.addItem(vLine, ignoreBounds=True)
crosshair_plot.addItem(hLine, ignoreBounds=True)

def mouseMoved(evt):
    pos = evt[0]  # select the x position of the mouse
    # if the mouse is inside the cross_hair_plot delimited region
    if crosshair_plot.sceneBoundingRect().contains(pos):
        mousePoint = crosshair_plot.vb.mapSceneToView(pos)
        index = int(mousePoint.x())
        if index > 0 and index < len(data1):
            label.setText("""<span style='font-size: 12pt'>x=%0.1f,
                             <span style='color: green'>y2=%0.1f</span>"""\
                             % (mousePoint.x(), data2[index]))
        # Set the crosshair where on the mouse position
        vLine.setPos(mousePoint.x())
        hLine.setPos(mousePoint.y())

proxy = pg.SignalProxy(crosshair_plot.scene().sigMouseMoved,
                       rateLimit=60, slot=mouseMoved)


if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()

