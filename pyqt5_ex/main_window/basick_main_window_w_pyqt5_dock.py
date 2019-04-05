import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class dockdemo(QMainWindow):
    def __init__(self, parent=None):
        super(dockdemo, self).__init__(parent)

        layout = QVBoxLayout()
        self.setCentralWidget(QTextEdit())
        self.setLayout(layout)
        self.setWindowTitle("Dock demo")

        self.create_menu_bar()
        self.create_d2()
        self.create_d1()

    def create_menu_bar(self):
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("save")
        file.addAction("quit")

    def create_d2(self):
        d2 = QDockWidget('d2')
        d2.toggleViewAction()
        self.addDockWidget(Qt.TopDockWidgetArea, d2)

    def create_d1(self):
        d1 = QDockWidget("d1")

        listWidget = QListWidget()
        listWidget.addItem("item1")
        listWidget.addItem("item2")

        d1.setWidget(listWidget)
        d1.setFloating(False)
        self.addDockWidget(Qt.BottomDockWidgetArea, d1)


def main():
    app = QApplication(sys.argv)
    ex = dockdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()