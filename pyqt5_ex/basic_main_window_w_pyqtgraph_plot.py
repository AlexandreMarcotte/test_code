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
        self.table_widget = PlotWidget()
        self.setCentralWidget(self.table_widget)
        self.show()


class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        # b = QPushButton('button')
        # self.layout.addWidget(b)
        q = deque(np.random.random(100), maxlen=100)
        p = pg.plot(q)
        # p_w = pg.PlotWidget()
        # self.curve = p_w.plot(q)
        # self.curve.setData(q)
        self.layout.addWidget(p)
        # self.l.addWidget(self.plot)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWin()
    sys.exit(app.exec_())
