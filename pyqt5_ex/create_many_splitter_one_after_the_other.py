from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QWidget,
                              QAction, QTabWidget, QVBoxLayout)


def create_gr(margin=False):
    gr = QGroupBox()
    l = QGridLayout()
    if not margin:
        l.setContentsMargins(0, 0, 0, 0)
    gr.setLayout(l)
    return gr, l

def create_splitter(first_gr, second_gr):
    s = QSplitter(Qt.Vertical)
    s.addWidget(first_gr)
    s.addWidget(second_gr)
    return s

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs - pythonspot.com'

        main_menu = self.menuBar()
        main_menu.addMenu('File')

        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, 300, 200)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__()
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tabs.resize(300, 200)
        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")

        # Create first tab with a button
        self.tab1.layout = QVBoxLayout(self)

        gr1, l1 = create_gr()
        gr2, l2 = create_gr()
        gr3, l3 = create_gr()

        s1 = create_splitter(gr1, gr2)
        s2 = create_splitter(s1, gr3)
        b1 = QPushButton('b1')
        b2 = QPushButton('b2')
        b3 = QPushButton('b3')

        l1.addWidget(b1)
        l2.addWidget(b2)
        l3.addWidget(b3)

        # self.tab1.layout.addWidget(s1)
        self.tab1.layout.addWidget(s2)

        self.tab1.setLayout(self.tab1.layout)


        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

