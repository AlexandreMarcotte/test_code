import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 200)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()

        self.tab1 = Tab()
        self.tab2 = Tab(num_tabs=6)
        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class Tab(QWidget):
    def __init__(self, num_tabs=3):
        super().__init__()
        self.num_tabs = num_tabs

        self.initUI()

    def initUI(self):
        layout = QGridLayout(self)
        self.add_docks()

    def add_docks(self):
        self.d1 = QDockWidget('d1')
        self.d2 = QDockWidget('d2')
        self.layout.addDock(self.d1)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())