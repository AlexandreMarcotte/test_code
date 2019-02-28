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
        self.layout = QGridLayout(self)

        # p = self.create_plot()
        b1 = QPushButton('yoo')
        b2 = QPushButton('allo')

        q = deque(np.random.random(100), maxlen=100)
        q2 = deque(np.ones(100), maxlen=100)
        # p = pg.plot()
        p = pg.PlotWidget()
        self.layout.addWidget(p)
        # p2 = pg.plot(q2)
        c = p.plot(q2)

        self.layout.addWidget(b2)
        self.layout.addWidget(b1)
        # p_w = pg.PlotWidget()
        # self.curve = p_w.plot(q2)
        # c = self.curve.setData(q2)

        # self.setLayout(self.layout)
    # def create_plot(self):
    #     q = deque(np.random.random(100), maxlen=100)
    #     q2 = deque(np.ones(100), maxlen=100)
    #     p = pg.plot()
    #     p2 = pg.plot(q2)
        # c = p.plot(q2)
        # return p



if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWin()
    sys.exit(app.exec_())
