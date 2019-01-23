#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
                             QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        # top = QFrame(self)
        # top.setFrameShape(QFrame.StyledPanel)
        # bottom = QFrame(self)
        # bottom.setFrameShape(QFrame.StyledPanel)

        top = QHBoxLayout(self)
        bottom = QHBoxLayout(self)

        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addLayout(top)
        splitter1.addLayout(bottom)

        hbox.addWidget(splitter1)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())