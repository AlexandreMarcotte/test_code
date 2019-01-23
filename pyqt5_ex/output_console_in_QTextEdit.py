# !/usr/bin/env python
# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui


# class Stream(QtCore.QObject):
#     newText = QtCore.pyqtSignal(str)
#
#     def write(self, text):
#         self.newText.emit(str(text))
#
# class Window(QtGui.QMainWindow):
#     def __init__(self):
#         super(Window, self).__init__()
#         self.home()
#         sys.stdout = Stream(newText=self.onUpdateText)
#
#     def onUpdateText(self, text):
#         cursor = self.process.textCursor()
#         cursor.movePosition(QtGui.QTextCursor.End)
#         cursor.insertText(text)
#         self.process.setTextCursor(cursor)
#         self.process.ensureCursorVisible()
#
#     def __del__(self):
#         sys.stdout = sys.__stdout__


class MyStream(QtCore.QObject):
    message = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def write(self, message):
        self.message.emit(str(message))



class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.pushButtonPrint = QPushButton("Click Me!")
        self.pushButtonPrint.clicked.connect(self.on_pushButtonPrint_clicked)

        self.textEdit = QTextEdit()

        self.layoutVertical = QVBoxLayout(self)
        self.layoutVertical.addWidget(self.pushButtonPrint)
        self.layoutVertical.addWidget(self.textEdit)

    @QtCore.pyqtSlot()
    def on_pushButtonPrint_clicked(self):
        print("Button Clicked!")

    @QtCore.pyqtSlot(str)
    def on_myStream_message(self, message):
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.textEdit.insertPlainText(message)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()

    myStream = MyStream()
    myStream.message.connect(main.on_myStream_message)

    sys.stdout = myStream  # Important part if removed not working
    sys.exit(app.exec_())