# from PyQt5 import QtCore, QtGui, QtWidgets
# import pyqtgraph as pg
# import numpy as np
#
# #
# # painter = QtGui.QPainter(mw)
# # painter.setPen(QtGui.QPen(QtCore.Qt.red, 10, QtCore.Qt.SolidLine))
# # painter.drawRect(100, 15, 100, 200)
#
#
#
# import sys
# from PyQt5.QtWidgets import *
# import qdarkstyle
#
#
# class MainWin(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         graph = Graph()
#         self.setCentralWidget(graph)
#         self.show()
#
#
#
# class Graph(QWidget):
#     def __init__(self, num_tabs=3):
#         super().__init__()
#         self.num_tabs = num_tabs
#
#         self.initUI()
#
#     def initUI(self):
#         layout = QGridLayout(self)
#         b = QPushButton('Test')
#         layout.addWidget(b)
#
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
#     main_window = MainWin()
#     sys.exit(app.exec_())


# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example draws nine rectangles in different
brush styles.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())