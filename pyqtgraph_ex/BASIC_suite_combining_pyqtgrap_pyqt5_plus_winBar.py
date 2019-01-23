from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
import pyqtgraph as pg
import numpy as np
import sys


class ScrollingPlot(QWidget):
    def __init__(self):
        super(ScrollingPlot, self).__init__()

        self.init_ui()

        self.data1 = np.random.normal(size=300)
        self.curve1 = self.plot_obj.plot(self.data1)

    def init_ui(self):
        lcheck = QtGui.QPushButton('plot local')
        layout = pg.LayoutWidget()
        # Build the layout
        layout.addWidget(lcheck)
        layout.resize(1000, 800)
        layout.show()
        timer = QtCore.QTimer()
        my_plots = []

        for i in range(8):
            self.plot_obj = pg.PlotWidget()
            layout.addWidget(self.plot_obj, row=i + 1, col=0, rowspan=1)

            my_plots.append(ScrollingPlot(self.plot_obj, i))
            self.timer.timeout.connect(my_plots[i].update)

    def update(self):
        self.data1[:-1] = self.data1[1:]
        self.data1[-1] = np.random.normal()
        self.curve1.setData(self.data1)

    def start_timer(self):
        self.timer.start(0)


# class Writer(QMainWindow):
#     def __init__(self, plot_obj):
#         super().__init__()
#
#         self.scrolling_plot = ScrollingPlot(plot_obj)
#         self.setCentralWidget(self.scrolling_plot)
#
#         self.init_ui()
#
#     def init_ui(self):
#         bar = self.menuBar()
#         file = bar.addMenu('File')


def main():
    # app = pg.mkQApp()
    app = QApplication(sys.argv)

    ScrollingPlot()

    QtGui.QApplication.instance().exec_()

if __name__ == '__main__':
    main()
