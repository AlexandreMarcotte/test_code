#!/usr/bin/env python

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
import sys

class RotatedButton(QPushButton):
    def __init__(self, text, parent, orientation="west"):
        super(RotatedButton,self).__init__(text, parent)
        self.orientation = orientation

    def paintEvent(self, event):
        painter = QStylePainter(self)
        painter.rotate(90)
        # x = self.width()
        x = 20
        painter.translate(0, -1*x)
        painter.drawControl(QStyle.CE_PushButton, self.getSyleOptions())

    # def minimumSizeHint(self):
    #     size = QtCore.QSize(20, 80)
    #     return size
    #
    # def maximumSizeHint(self):
    #     size = QtCore.QSize(20, 80)
    #     return size

    def sizeHint(self):
        size = super(RotatedButton, self).sizeHint()
        size.transpose()
        # size = QtCore.QSize(80, 20)
        return size

    def getSyleOptions(self):
        options = QStyleOptionButton()
        options.initFrom(self)
        # size = options.rect.size()
        size = QtCore.QSize(80, 20)
        # size.transpose()
        options.rect.setSize(size)
        # options.features = QStyleOptionButton.None_
        # if self.isFlat():
        #     options.features |= QStyleOptionButton.Flat
        # if self.menu():
        #     options.features |= QStyleOptionButton.HasMenu
        # if self.autoDefault() or self.isDefault():
        #     options.features |= QStyleOptionButton.AutoDefaultButton
        # if self.isDefault():
        #     options.features |= QStyleOptionButton.DefaultButton
        # if self.isDown() or (self.menu() and self.menu().isVisible()):
        #     options.state |= QStyle.State_Sunken
        # if self.isChecked():
        #     options.state |= QStyle.State_On
        # if not self.isFlat() and not self.isDown():
        #     options.state |= QStyle.State_Raised
        options.text = self.text()
        # options.icon = self.icon()
        # options.iconSize = self.iconSize()
        return options


class Main(QFrame):
    def __init__(self):
        QFrame.__init__(self)

        self.application = QtCore.QCoreApplication.instance()
        self.layout = QHBoxLayout()
        self.button = RotatedButton("Button", self, orientation="west")
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

if __name__ == '__main__':

    application = QApplication(sys.argv)
    application.main = Main()
    application.main.show()
    sys.exit(application.exec_())