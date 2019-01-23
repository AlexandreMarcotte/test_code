import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from pyqt5_ex.rotate_QPushButton import RotatedButton


class dockdemo(QMainWindow):
    def __init__(self, parent=None):
        super(dockdemo, self).__init__(parent)

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Dock demo")
        # self.setGeometry(100, 100, 400, 400)

        self.create_menu_bar()
        self.create_d1()
        self.d2 = self.create_d2()

    def create_menu_bar(self):
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")

    def create_d1(self):
        d1 = QDockWidget('Text dock')
        # d_in_1 = QDockWidget('d_in_1')
        # d_in_2 = QDockWidget('d_in_2')

        l = pg.LayoutWidget()
        # l = QGridLayout()
        d1.setWidget(l)
        # l.addWidget(d_in_1, 1, 0)
        # l.addWidget(d_in_2, 1, 1)

        txt = QTextEdit()
        l.addWidget(txt, 0, 1, 1, 2)


        # b2 = QPushButton('1')
        # b.setMaximumWidth(14)
        # b.setCheckable(True)
        b = RotatedButton("toolbox", self, orientation="west")
        b.setCheckable(True)
        b.setMaximumWidth(20)
        b.clicked.connect(self.open_d2)
        l.addWidget(b, 0, 0)
        # l.setColumnStretch(0, 1)
        self.addDockWidget(Qt.RightDockWidgetArea, d1)

    @QtCore.pyqtSlot(bool)
    def open_d2(self, checked):
        if checked:
            self.d2.show()
        else:
            self.d2.hide()

    def create_d2(self):
        d2 = QDockWidget('')
        l = pg.LayoutWidget()
        d2.setWidget(l)
        # d2.toggleViewAction()
        tb = QToolBox()
        for i in range(3):
            tb.addItem(QPlainTextEdit(f'Text {i}'), f'Page {i}')
        l.addWidget(tb)
        self.addDockWidget(Qt.LeftDockWidgetArea, d2)
        d2.hide()
        return d2


def main():
    app = QApplication(sys.argv)
    ex = dockdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()