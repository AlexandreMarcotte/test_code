from PyQt5.QtWidgets import *
import pyqtgraph as pg
from collections import deque
import numpy as np
import sys


class MainWin(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.plot_widget = PlotWidget()
        self.setCentralWidget(self.plot_widget)
        self.show()


class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)

        q = deque(np.random.random(100), maxlen=100)
        q2 = deque(np.ones(100), maxlen=100)


        p = pg.plot(q)
        c = p.plot(q2)
        b = QPushButton('allo')
        self.layout.addWidget(b)
        # p_w = pg.PlotWidget()
        # self.curve = p_w.plot(q2)
        # c = self.curve.setData(q2)

        self.layout.addWidget(p)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWin()
    sys.exit(app.exec_())
