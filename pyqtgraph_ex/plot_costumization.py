# -*- coding: utf-8 -*-
"""
This example demonstrates the creation of a plot with a customized
AxisItem and ViewBox.
"""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import time

class DateAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        strns = []
        rng = max(values)-min(values)
        if rng < 3600*24:
            string = '%H:%M:%S'
            label1 = '%b %d -'
            label2 = ' %b %d, %Y'
        elif rng >= 3600*24 and rng < 3600*24*30:
            string = '%d'
            label1 = '%b - '
            label2 = '%b, %Y'
        elif rng >= 3600*24*30 and rng < 3600*24*30*24:
            string = '%b'
            label1 = '%Y -'
            label2 = ' %Y'
        elif rng >=3600*24*30*24:
            string = '%Y'
            label1 = ''
            label2 = ''
        for x in values:
            try:
                strns.append(time.strftime(string, time.localtime(x)))

                # strns = ['10:00:00', '20:00:00']
            except ValueError:  ## Windows can't handle dates before 1970
                print('value error')
                strns.append('')
        try:
            label = time.strftime(
                    label1,
                    time.localtime(min(values)))\
                    + time.strftime(label2, time.localtime(max(values)))
        except ValueError:
            label = ''
        return strns

class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.setMouseMode(self.RectMode)

    ## reimplement right-click to zoom out
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.autoRange()

    def mouseDragEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            ev.ignore()
        else:
            pg.ViewBox.mouseDragEvent(self, ev)


app = pg.mkQApp()

axis = DateAxis(orientation='bottom')
vb = CustomViewBox()

pw = pg.PlotWidget(
        viewBox=vb, axisItems={'bottom': axis}, enableMenu=False,
        title="Costumized plot")
dates = np.arange(2) * (3600*24*356)
pw.show()
pw.plot(x=dates, y=[0,0], symbol='o')
pw.setWindowTitle('pyqtgraph example: customPlot')

# r = pg.PolyLineROI([(0,0), (10, 10)])
# pw.addItem(r)

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
