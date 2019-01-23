import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QWidget,
                              QAction, QTabWidget, QVBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui, QtCore
import pyqtgraph as pg
import numpy as np


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200

        main_menu = self.menuBar()
        main_menu.addMenu('File')

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__()
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")

        # Create first tab with a button
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab with a button
        # self.tab2.layout = QVBoxLayout(self)
        # self.pushButton1 = QPushButton("dickoosss")
        # self.tab2.layout.addWidget(self.pushButton1)
        # self.tab2.setLayout(self.tab2.layout)

        # Create second tab with a plot
        self.tab2.layout = QVBoxLayout(self)
        self.timer = QtCore.QTimer()
        self.plot = pg.PlotWidget()
        self.tab2.layout.addWidget(self.plot)
        self.my_plot = ScrollingPlot(self.plot)
        self.timer.timeout.connect(self.my_plot.update)
        self.timer.start(0)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @QtCore.pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


class ScrollingPlot(object):
    def __init__(self, plot_obj):
        self.data1 = np.random.normal(size=300)
        self.curve1 = plot_obj.plot(self.data1)

    def update(self):
        self.data1[:-1] = self.data1[1:]
        self.data1[-1] = np.random.normal()
        self.curve1.setData(self.data1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())