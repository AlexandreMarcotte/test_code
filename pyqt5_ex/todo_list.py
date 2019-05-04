import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.console
import numpy as np

from pyqtgraph.dockarea import *


class dockdemo(QMainWindow):
    def __init__(self, parent=None):
        super(dockdemo, self).__init__(parent)
        self.setWindowTitle('Todo list')
        # self.dock_area = DockArea()
        # self.setCentralWidget(self.dock_area)
        self.create_menu_bar()
        for i in range(5):
            self.create_dock(i)

    def create_menu_bar(self):
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")

    def create_dock(self, i):
        # Pyqt5
        dock = QDockWidget('dock')
        dock.setWidget(QTextEdit(f'this is a new task {i}'))
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        # Pyqtgraph
        # dock = Dock('Dock',)
        # dock.addWidget(QLineEdit(f'this is some text'))
        # self.dock_area.addDock(dock, 'bottom')


def main():
    app = QApplication(sys.argv)
    ex = dockdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
