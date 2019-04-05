import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class dockdemo(QMainWindow):
    def __init__(self, parent=None):
        super(dockdemo, self).__init__(parent)
        self.setWindowTitle('Modelisation Tool')
        self.create_menu_bar()
        self.create_d1()

    def create_menu_bar(self):
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")

    def create_d1(self):
        d1 = QDockWidget("d1")
        self.addDockWidget(Qt.BottomDockWidgetArea, d1)


def main():
    app = QApplication(sys.argv)
    ex = dockdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
