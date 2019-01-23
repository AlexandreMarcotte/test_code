import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import pyqtgraph as pg


class dockdemo(QMainWindow):
    def __init__(self, parent=None):
        super(dockdemo, self).__init__(parent)

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Dock demo")
        self.setGeometry(100, 100, 400, 400)

        self.create_menu_bar()
        self.create_d1()
        self.d2 = self.create_d2()

    def create_menu_bar(self):
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")

    def create_d1(self):
        d1 = QDockWidget('')

        l = pg.LayoutWidget()
        d1.setWidget(l)

        txt = QTextEdit()
        l.addWidget(txt, 1, 1, 1, 2)

        b = QPushButton('1')
        b.setMaximumWidth(14)
        b.setCheckable(True)
        b.clicked.connect(self.open_d2)
        l.addWidget(b, 0, 0)

        self.addDockWidget(Qt.RightDockWidgetArea, d1)

    @QtCore.pyqtSlot(bool)
    def open_d2(self, checked):
        if checked:
            self.d2.show()
        else:
            self.d2.hide()

    def create_d2(self):
        d2 = QDockWidget('')
        d2.toggleViewAction()
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
