# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
#
# """
# ZetCode PyQt5 tutorial
#
# This program creates a checkable menu.
#
# Author: Jan Bodnar
# Website: zetcode.com
# Last edited: August 2017
# """
#
# import sys
# from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
#
#
# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.statusbar = self.statusBar()
#         self.statusbar.showMessage('Ready')
#
#         menubar = self.menuBar()
#         viewMenu = menubar.addMenu('View')
#
#         viewStatAct = QAction('View statusbar', self, checkable=True)
#         viewStatAct.setStatusTip('View statusbar')
#         viewStatAct.setChecked(True)
#         viewStatAct.triggered.connect(self.toggleMenu)
#
#         viewMenu.addAction(viewStatAct)
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Check menu')
#         self.show()
#
#     def toggleMenu(self, state):
#
#         if state:
#             self.statusbar.show()
#         else:
#             self.statusbar.hide()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())



# Create the menu from outside the main class where the general menu is created
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a checkable menu.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from PyQt5.QtWidgets import QMenu


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()

        one_menu = OneMenu(menubar, self, self.print_shizzle)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def print_shizzle(self):
        print(self.one_menu.name)




class OneMenu:
    def __init__(self, menubar, mainwindow, func):
        self.name = 'EEG'
        self.mainwindow = mainwindow
        self.menubar = menubar
        self.func = func

        self.add_menu()

    def add_menu(self):
        viewMenu = self.menubar.addMenu('View')
        viewStatAct = QAction('View statusbar', self.mainwindow, checkable=True)
        # viewStatAct.setStatusTip('View statusbar')
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)

    def toggleMenu(self):
        """An object of the present class needs to be instantiated inside the
        mainmenu class for this method to be called by the connect because the
        trigger event is only perceptible inside the mainwindow class
        THE OBJECT INSTANTIATED NEEDS TO BE PART OF THE MAINWINDOW CLASS
        IE. IT NEEDS TO BE SELF.objectname"""
        print('toggle menu')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())