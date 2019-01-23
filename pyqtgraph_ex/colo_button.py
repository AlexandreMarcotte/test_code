
# -*- coding: utf-8 -*-
"""
Simple example demonstrating a button which displays a colored rectangle
and allows the user to select a new color by clicking on the button.
"""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

app = QtGui.QApplication([])
win = QtGui.QMainWindow()
btn = pg.ColorButton()
win.setCentralWidget(btn)
win.show()
win.setWindowTitle('pyqtgraph example: ColorButton')

def change(btn):
    print("change", btn.color())
def done(btn):
    x = QtGui.QColor(10)
    print(x)
    print("done", repr(btn.color()))

btn.sigColorChanging.connect(change)
btn.sigColorChanged.connect(done)

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
