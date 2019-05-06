import pyqtgraph as pg
import sys
from PyQt5.QtWidgets import *
from collections import deque
import numpy as np


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 200)
        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)
        self.show()


class MyTabWidget(QTabWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tab1 = Tab(1)
        self.tab2 = Tab(2)
        # Add tabs
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")


class Tab(QWidget):
    def __init__(self, number=1):
        super().__init__()
        self.number = number

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout(self)
        self.add_sub_layout(layout)

    def add_sub_layout(self, parent_layout):
        layout = QGridLayout()

        b = QPushButton(f'button {self.number}')
        layout.addWidget(b)
        # Add a plot
        self.q = deque(np.random.random(10), maxlen=10)
        plot = pg.PlotWidget()
        layout.addWidget(plot)
        self.curve = plot.plot(self.q)

        gr = QGroupBox(f'ch {self.number}')
        gr.setLayout(layout)
        parent_layout.addWidget(gr, self.number, 0)
        return layout


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())