import sys
from PyQt5.QtWidgets import *

# class Window(QWidget):
#     def __init__(self, parent=None):
#         super(Window, self).__init__(parent)
#
#         # tool box
#         tool_box = QToolBox()
#
#         # items
#         tool_box.addItem(QPlainTextEdit('Text 1'),
#                          'Page 1')
#         tool_box.addItem(QPlainTextEdit('Text 2'),
#                          'Page 2')
#
#         # vertical box layout
#         vlayout = QVBoxLayout()
#         vlayout.addWidget(tool_box)
#         self.setLayout(vlayout)
#
#
# application = QApplication(sys.argv)
#
# # window
# window = Window()
# window.setWindowTitle('Tool Box')
# window.resize(280, 300)
# window.show()
#
# sys.exit(application.exec_())

#%%import os

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot


class SignalsWindow(QWidget, object):
    def __init__(self, parent=None):
        super(SignalsWindow, self).__init__(parent)

        # plain text edit
        self.output_text = QPlainTextEdit()
        self.output_text.setReadOnly(True)  # read-only
        self.output_text.setStyleSheet('QPlainTextEdit { background-color: #f4eed7; color: black; }')

        # instructions label
        self.instructions_label = QLabel()
        self.instructions_label.setTextFormat(Qt.PlainText)
        self.instructions_label.setWordWrap(True)
        self.instructions_label.setText('* Play with the widget to see when the signals are emitted.')
        self.instructions_label.setEnabled(False)

        # icons
        # clean_icon = QIcon(os.path.join('images', 'clean_icon.png'))

        # clean button
        clean_button = QToolButton()
        # clean_button.setIcon(clean_icon)
        clean_button.setToolTip('Clean all')
        clean_button.clicked.connect(self.clean_button_clicked)  # clicked signal

        # horizontal box layout
        hlayout = QHBoxLayout()
        hlayout.addStretch()
        hlayout.addWidget(clean_button)

        # vertical box layout
        self.vlayout = QVBoxLayout()
        self.vlayout.setDirection(QBoxLayout.BottomToTop)
        self.vlayout.addWidget(self.instructions_label)
        self.vlayout.addLayout(hlayout)
        self.vlayout.addWidget(self.output_text)
        self.setLayout(self.vlayout)

    def scroll_to_end(self):
        self.output_text.moveCursor(QtGui.QTextCursor.End)

    # *** SLOTS ***
    # clicked slot
    @pyqtSlot()
    def clean_button_clicked(self):
        self.output_text.clear()
#
#
# if __name__ == '__main__':
#     application = QApplication(sys.argv)
#
#     # window
#     window = SignalsWindow()
#     window.setWindowTitle('Signals window')
#     window.resize(240, 300)
#     window.show()
#
#     sys.exit(application.exec_())

#
## %%
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot

# from signals_window import SignalsWindow  # The SignalsWindow class is required


class Window(SignalsWindow):
    def __init__(self, parent=None):
        super().__init__()

        # tool box
        tool_box = QToolBox()
        self.vlayout.addWidget(tool_box)

        # items
        for index in range(3):
            tool_box.addItem(QPlainTextEdit('Text {}'.format(index + 1)),
                             'Page {}'.format(index + 1))

        tool_box.setMaximumHeight(300)

        # *** Tool Box signals ***
        # currentChanged signal
        # tool_box.currentChanged.connect(self.current_changed)

        # instructions label
        self.instructions_label.setText('* Play with the Tool Box to see when the signals are emitted.')

    # *** Tool Box slots ***
    # current_changed slot
    @pyqtSlot(int)
    def current_changed(self, index):
        self.output_text.appendPlainText('currentChanged (index: {})'.format(index))
        self.scroll_to_end()


application = QApplication(sys.argv)

# window
window = Window()
window.setWindowTitle('Tool Box signals')
window.resize(300, 420)
window.show()

sys.exit(application.exec_())
