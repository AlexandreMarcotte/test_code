import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


class dockdemo(QMainWindow):
    def __init__(self, parent=None):
        super(dockdemo, self).__init__(parent)
        self.setWindowTitle('Modelisation Tool')
        # self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.init_UI()

    def init_UI(self):
        self.create_menu_bar()
        self.create_dock()

    def create_menu_bar(self):
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")

    def create_dock(self):
        d = QDockWidget()
        self.addDockWidget(Qt.BottomDockWidgetArea, d)
        self.plot_widget = PlotWidget()
        d.setWidget(self.plot_widget)


class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout(self)

        self.num_val = QTextEdit()
        self.denom_val = QTextEdit()
        self.p1 = self.create_plot_item()
        self.p2 = self.create_plot_item()

        layout.addWidget(QLabel('Numerator: '))
        layout.addWidget(self.num_val)
        layout.addWidget(QLabel('Denominator: '))
        layout.addWidget(self.denom_val)
        layout.addWidget(self.p1)
        layout.addWidget(self.p2)

        self.create_bode_plot()

    def create_plot_item(self):
        plot = pg.PlotWidget()
        plot.plotItem.setLogMode(x=True)
        return plot

    def create_bode_plot(self):
        # K / (s + 1)
        s1 = signal.lti([-20, 200], [1, 16, 100])
        w, mag, phase = signal.bode(s1)

        self.p1.plot(w, mag)
        self.p2.plot(w, phase)
        # plt.semilogx(w, mag)    # Bode magnitude plot
        # plt.figure()
        # plt.semilogx(w, phase)  # Bode phase plot
        # plt.show()




def main():
    app = QApplication(sys.argv)
    ex = dockdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
