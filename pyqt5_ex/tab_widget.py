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


class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()

        self.tab1 = Tab()
        self.tab2 = Tab()
        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class Tab(QTabWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout(self)
        self.add_sub_layout(layout, 0)

    def add_sub_layout(self, parent_layout, pos):
        layout = QGridLayout()

        b = QPushButton(f'button {pos}')
        layout.addWidget(b)
        # Add a plot
        self.q = deque(np.zeros(10), maxlen=10)
        plot = pg.PlotWidget()
        layout.addWidget(plot)
        # self.curve = plot.plot(self.q)

        gr = QGroupBox(f'ch {pos}')
        gr.setLayout(layout)
        parent_layout.addWidget(gr, pos, 0)
        return layout


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())