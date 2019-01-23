import sys
from PyQt5.QtWidgets import *
# import qdarkstyle


class MainWin(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        # self.create_menu_bar()
        # self.add_toolbar()
        #
        # self.statusBar().showMessage('bonjour')
        self.show()

    def create_tabs(self):                                                    # TODO: KNOW why this part fucks the ability to draw lines on the widget (It is the dark style that is fucked and doesnt want to draw the lines it seems)
        tab_w = QTabWidget()
        for name, tab in self.tabs.items():
            tab_w.addTab(name, tab)
        return tab_w

    def add_toolbar(self):
        exitAct = QAction('Exit', self)
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

    def create_menu_bar(self):
        main_menu = self.menuBar()
        self.files = QMenu('&Files')
        one = QAction('1')
        self.files.addAction(one)
        main_menu.addMenu(self.files)


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
    main_window = MainWin()
    sys.exit(app.exec_())