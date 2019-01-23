import sys
from PyQt5.QtWidgets import *
# import qdarkstyle


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
        for ch in range(self.num_tabs):
            self.add_sub_layout(layout, ch)

    def add_sub_layout(self, parent_layout, pos):
        layout = QGridLayout()
        b = QPushButton(f'button {pos}')
        layout.addWidget(b)
        gr = QGroupBox(f'ch {pos}')
        gr.setLayout(layout)
        parent_layout.addWidget(gr, pos, 0)
        return layout


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ex = App()
    sys.exit(app.exec_())