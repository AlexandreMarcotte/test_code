import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import numpy as np


class dockdemo(QMainWindow):
    def __init__(self, parent=None):
        super(dockdemo, self).__init__(parent)
        self.setWindowTitle('Modelisation Tool')
        self.init_UI()

    def init_UI(self):
        self.create_menu_bar()
        self.create_dock()

    def create_menu_bar(self):
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")

    def create_dock(self):
        d = QDockWidget("d1")
        self.addDockWidget(Qt.BottomDockWidgetArea, d)
        self.plot_widget = PlotWidget()
        d.setWidget(self.plot_widget)


class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout(self)
        q = np.zeros(100)
        plot = pg.PlotWidget()
        layout.addWidget(plot)
        plot.plot(q, pen='w')


def main():
    app = QApplication(sys.argv)
    ex = dockdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
