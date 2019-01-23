# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot
#
#
# class App(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 menu - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 640
#         self.height = 400
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         mainMenu = self.menuBar()
#         fileMenu = mainMenu.addMenu('EEG')
#         editMenu = mainMenu.addMenu('BCI')
#         viewMenu = mainMenu.addMenu('View')
#         searchMenu = mainMenu.addMenu('Search')
#         toolsMenu = mainMenu.addMenu('Tools')
#         helpMenu = mainMenu.addMenu('Help')
#
#         exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
#         exitButton.setShortcut('Ctrl+Q')
#         exitButton.setStatusTip('Exit application')
#         exitButton.triggered.connect(self.close)
#         fileMenu.addAction(exitButton)
#
#         self.show()


import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

        self.pushButton.clicked.connect(self.btn_clk)

        MainWindow.show()
    def btn_clk(self):
        L = [1,2,3,4,5]
        pg.plot(L)#this line plots in a new window
        self.graphicsView.plot(L)#this line doesn't work

import sys

def main():
    app = QtGui.QApplication(sys.argv)
    ui_win = Ui_MainWindow()
    app.exec_()


if __name__ == '__main__':
    main()


