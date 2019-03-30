import pyqtgraph as pg
import sys
from PyQt5.QtWidgets import *
from collections import deque
import numpy as np
from pyqtgraph.Qt import QtGui
from collections import deque
from random import random


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1000, 900)
        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)
        self.show()


class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()

        self.game_tab = GameTab()
        self.stat_tab = StatTab()
        # Add tabs
        self.tabs.addTab(self.game_tab, 'Game Tab')
        self.tabs.addTab(self.stat_tab, 'Stat Tab')
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class GameTab(QTabWidget):
    def __init__(self):
        super().__init__()
        # self.basic_scrolls = []
        self.init_ui()

    def init_ui(self):
        self.parent_layout = QGridLayout(self)
        self.add_sub_layout(0)
        self.add_sub_layout(1) # Add a second layout on the side

    def add_sub_layout(self, pos):
        layout = QGridLayout()
        # Add a plot
        self.basic_scroll = BasicScroll()
        layout.addWidget(self.basic_scroll.plot)
        # self.basic_scrolls.append(basic_scroll)
        gr = QGroupBox(f'Player {pos + 1}')
        gr.setLayout(layout)
        self.parent_layout.addWidget(gr, 0, pos)
        return layout


class StatTab(QTabWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.parent_layout = QGridLayout(self)

    # def add_sub_layout(self):
    #     layout = QGridLayout()
    #     self.parent_layout.addWidget(layout)
    #     return layout


class BasicScroll:
    def __init__(self):
        self.plot = pg.PlotWidget()
        self.deque = deque(np.zeros(100), maxlen=100)
        self.curve = self.plot.plot()
        self.timer = self.start_timer()

    def update(self):
        self.deque.append(random())
        self.curve.setData(self.deque)

    def start_timer(self):
        timer = pg.QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(10)
        return timer


if __name__ == '__main__':
    Qapp = QApplication(sys.argv)
    application = App()
    sys.exit(Qapp.exec_())
