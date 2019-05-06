from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QWidget,
                             QAction, QTabWidget, QVBoxLayout, QGridLayout)
import PyQt5
import pyqtgraph as pg
import numpy as np
import sys


class ScrollingPlot:
    def __init__(self, plot_obj):
        self.data1 = np.random.normal(size=300)
        self.curve1 = plot_obj.plot(self.data1)

    def update(self):
        self.data1[:-1] = self.data1[1:]
        self.data1[-1] = np.random.normal()
        self.curve1.setData(self.data1)


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('basic graph')
        # Add a menu bar
        main_menu = self.menuBar()
        main_menu.addMenu('File')
        # message at the bottom
        self.statusBar().showMessage('Message in statusbar.')

        self.simple_graph = SimpleGraph()
        self.setCentralWidget(self.simple_graph)
        self.simple_graph.start_timer()

        self.show()

class SimpleGraph(QTabWidget):
    def __init__(self):
        super(SimpleGraph, self).__init__()
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        # Add tabs
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")

        # Compose tabs
        self.create_tab1()
        self.create_tab2()

    def create_tab1(self):
        # Create first tab with a button
        self.tab1.layout = QGridLayout(self)
        # self.pushButton1 = QPushButton("PyQt5 button")
        # self.tab1.layout.addWidget(self.pushButton1)
        self.le = QtGui.QLineEdit('here')
        self.le.textChanged.connect(self.do_something)
        self.tab1.layout.addWidget(self.le)
        self.tab1.setLayout(self.tab1.layout)

    def do_something(self):
        print('do something')

    def create_tab2(self):
        # self.layout = QVBoxLayout(self)                                         # This line allowed me to set this object as the central widget (adding the word self to the function made it work)
        self.tab2.layout = QGridLayout(self)
        self.timer = QtCore.QTimer()
        self.plot = pg.PlotWidget()
        self.tab2.layout.addWidget(self.plot, 0, 0, 3, 2)
        # self.pb2 = QPushButton("pb2")
        # self.pb3 = QPushButton("pb3")
        # self.pb4 = QPushButton("pb4")
        # self.tab2.layout.addWidget(self.pb2, 3, 0, 1, 1)
        # self.tab2.layout.addWidget(self.pb3, 4, 0, 1, 1)
        # self.tab2.layout.addWidget(self.pb4, 5, 0, 1, 1)
        self.my_plot = ScrollingPlot(self.plot)
        self.timer.timeout.connect(self.my_plot.update)
        self.tab2.setLayout(self.tab2.layout)

    def start_timer(self):
        self.timer.start(0)


if __name__ == '__main__':
    app = pg.mkQApp()
    simple_graph = App()
    sys.exit(app.exec_())
