# from PyQt4 import QtCore, QtGui
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Dock Widgets')
        self.button = QPushButton('Raise Next Tab', self)
        self.button.clicked.connect(self.handleButton)
        self.setCentralWidget(self.button)
        self.dockList = []
        approvedAdded = False
        for dockName in 'Red Green Yellow Blue'.split():
            dock = QDockWidget(dockName)
            dock.setWidget(QListWidget())
            dock.setAllowedAreas(QtCore.Qt.TopDockWidgetArea)
            dock.setFeatures(QDockWidget.DockWidgetMovable |
                             QDockWidget.DockWidgetFloatable)
            self.addDockWidget(QtCore.Qt.TopDockWidgetArea, dock)
            insertIndex = len(self.dockList) - 1
            if dockName == 'Green':
                insertIndex = 0
                approvedAdded = True
            elif dockName == 'Yellow':
                if not approvedAdded:
                    insertIndex = 0
                else:
                    insertIndex = 1
            self.dockList.insert(insertIndex, dock)
        if len(self.dockList) > 1:
            for index in range(0, len(self.dockList) - 1):
                self.tabifyDockWidget(self.dockList[index],
                                      self.dockList[index + 1])
        self.dockList[0].raise_()
        self.nextindex = 1

    def handleButton(self):
        self.dockList[self.nextindex].raise_()
        self.nextindex += 1
        if self.nextindex > len(self.dockList) - 1:
            self.nextindex = 0

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


#  # __author__ = 'Caroline Beyne'
#
# # from PyQt4 import  QtCore
# from  PyQt5.QtWidgets import *
# from PyQt5 import QtCore
# from PyQt5.QtWidgets import QStylePainter, QColo
#
# class FrameLayout(QWidget):
#     def __init__(self, parent=None, title=None):
#         QFrame.__init__(self, parent=parent)
#
#         self._is_collasped = True
#         self._title_frame = None
#         self._content, self._content_layout = (None, None)
#
#         self._main_v_layout = QVBoxLayout(self)
#         self._main_v_layout.addWidget(self.initTitleFrame(title, self._is_collasped))
#         self._main_v_layout.addWidget(self.initContent(self._is_collasped))
#
#         self.initCollapsable()
#
#     def initTitleFrame(self, title, collapsed):
#         self._title_frame = self.TitleFrame(title=title, collapsed=collapsed)
#
#         return self._title_frame
#
#     def initContent(self, collapsed):
#         self._content = QWidget()
#         self._content_layout = QVBoxLayout()
#
#         self._content.setLayout(self._content_layout)
#         self._content.setVisible(not collapsed)
#
#         return self._content
#
#     def addWidget(self, widget):
#         self._content_layout.addWidget(widget)
#
#     def initCollapsable(self):
#         # QtCore.QObject.connect(self._title_frame, QtCore.SIGNAL('clicked()'), self.toggleCollapsed)
#         pass
#
#     def toggleCollapsed(self):
#         self._content.setVisible(self._is_collasped)
#         self._is_collasped = not self._is_collasped
#         self._title_frame._arrow.setArrow(int(self._is_collasped))
#
#     ############################
#     #           TITLE          #
#     ############################
#     class TitleFrame(QFrame):
#         def __init__(self, parent=None, title="", collapsed=False):
#             QFrame.__init__(self, parent=parent)
#
#             self.setMinimumHeight(24)
#             self.move(QtCore.QPoint(24, 0))
#             self.setStyleSheet("border:1px solid rgb(41, 41, 41); ")
#
#             self._hlayout = QHBoxLayout(self)
#             self._hlayout.setContentsMargins(0, 0, 0, 0)
#             self._hlayout.setSpacing(0)
#
#             self._arrow = None
#             self._title = None
#
#             self._hlayout.addWidget(self.initArrow(collapsed))
#             self._hlayout.addWidget(self.initTitle(title))
#
#         def initArrow(self, collapsed):
#             self._arrow = FrameLayout.Arrow(collapsed=collapsed)
#             self._arrow.setStyleSheet("border:0px")
#
#             return self._arrow
#
#         def initTitle(self, title=None):
#             self._title = QLabel(title)
#             self._title.setMinimumHeight(24)
#             self._title.move(QtCore.QPoint(24, 0))
#             self._title.setStyleSheet("border:0px")
#
#             return self._title
#
#         def mousePressEvent(self, event):
#             self.emit(QtCore.SIGNAL('clicked()'))
#
#             return super(FrameLayout.TitleFrame, self).mousePressEvent(event)
#
#
#     #############################
#     #           ARROW           #
#     #############################
#     class Arrow(QFrame):
#         def __init__(self, parent=None, collapsed=False):
#             QFrame.__init__(self, parent=parent)
#
#             self.setMaximumSize(24, 24)
#
#             # horizontal == 0
#             self._arrow_horizontal = (
#                     QtCore.QPointF(7.0, 8.0), QtCore.QPointF(17.0, 8.0),
#                     QtCore.QPointF(12.0, 13.0))
#             # vertical == 1
#             self._arrow_vertical = (
#                     QtCore.QPointF(8.0, 7.0), QtCore.QPointF(13.0, 12.0),
#                     QtCore.QPointF(8.0, 17.0))
#             # arrow
#             self._arrow = None
#             self.setArrow(int(collapsed))
#
#         def setArrow(self, arrow_dir):
#             if arrow_dir:
#                 self._arrow = self._arrow_vertical
#             else:
#                 self._arrow = self._arrow_horizontal
#
#         def paintEvent(self, event):
#             painter = QStylePainter()
#             painter.begin(self)
#             painter.setBrush(QtCore.QColor(192, 192, 192))
#             painter.setPen(QtCore.QColor(64, 64, 64))
#             painter.drawPolygon(*self._arrow)
#             painter.end()
#
#
#
# import sys
# # from FrameLayout import FrameLayout
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#
#     win = QMainWindow()
#     w = QWidget()
#     w.setMinimumWidth(350)
#     win.setCentralWidget(w)
#     l = QVBoxLayout()
#     l.setSpacing(0)
#     l.setAlignment(QtCore.Qt.AlignTop)
#     w.setLayout(l)
#
#     t = FrameLayout(title="Buttons")
#     t.addWidget(QPushButton('a'))
#     t.addWidget(QPushButton('b'))
#     t.addWidget(QPushButton('c'))
#
#     f = FrameLayout(title="TableWidget")
#     rows, cols = (6, 3)
#     data = {'col1': ['1', '2', '3', '4', '5', '6'],
#             'col2': ['7', '8', '9', '10', '11', '12'],
#             'col3': ['13', '14', '15', '16', '17', '18']}
#     table = QTableWidget(rows, cols)
#     headers = []
#     for n, key in enumerate(sorted(data.keys())):
#         headers.append(key)
#         for m, item in enumerate(data[key]):
#             newitem = QTableWidgetItem(item)
#             table.setItem(m, n, newitem)
#     table.setHorizontalHeaderLabels(headers)
#     f.addWidget(table)
#
#     l.addWidget(t)
#     l.addWidget(f)
#
#     win.show()
#     win.raise_()
#     # print "Finish"
# sys.exit(app.exec_())




# from PyQt5 import QtCore, QtGui
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# import sys
#
#
# class MainWin(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.table_widget = Spoiler(self)
#         self.setCentralWidget(self.table_widget)
#         self.show()
#
#
# class Spoiler(QWidget):
#     def __init__(self, parent=None, title='', animationDuration=300):
#         """
#         References:
#             # Adapted from c++ version
#             http://stackoverflow.com/questions/32476006/how-to-make-an-expandable-collapsable-section-widget-in-qt
#         """
#         super(Spoiler, self).__init__(parent=parent)
#
#         self.animationDuration = 300
#         self.toggleAnimation = QtCore.QParallelAnimationGroup()
#         self.contentArea = QScrollArea()
#         self.headerLine = QFrame()
#         self.toggleButton = QToolButton()
#         self.mainLayout = QGridLayout()
#
#         toggleButton = self.toggleButton
#         toggleButton.setStyleSheet("QToolButton { border: none; }")
#         toggleButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
#         toggleButton.setArrowType(QtCore.Qt.RightArrow)
#         toggleButton.setText(str(title))
#         toggleButton.setCheckable(True)
#         toggleButton.setChecked(False)
#
#         headerLine = self.headerLine
#         headerLine.setFrameShape(QFrame.HLine)
#         headerLine.setFrameShadow(QFrame.Sunken)
#         headerLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
#
#         self.contentArea.setStyleSheet("QScrollArea { background-color: white; border: none; }")
#         self.contentArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         # start out collapsed
#         self.contentArea.setMaximumHeight(0)
#         self.contentArea.setMinimumHeight(0)
#         # let the entire widget grow and shrink with its content
#         toggleAnimation = self.toggleAnimation
#         toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self, "minimumHeight"))
#         toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self, "maximumHeight"))
#         toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self.contentArea, "maximumHeight"))
#         # don't waste space
#         mainLayout = self.mainLayout
#         mainLayout.setVerticalSpacing(0)
#         mainLayout.setContentsMargins(0, 0, 0, 0)
#         row = 0
#         mainLayout.addWidget(self.toggleButton, row, 0, 1, 1, Qt.AlignLeft)
#         mainLayout.addWidget(self.headerLine, row, 2, 1, 1)
#         row += 1
#         mainLayout.addWidget(self.contentArea, row, 0, 1, 3)
#         self.setLayout(self.mainLayout)
#
#         def start_animation(checked):
#             arrow_type = QtCore.Qt.DownArrow if checked else QtCore.Qt.RightArrow
#             direction = QtCore.QAbstractAnimation.Forward if checked else QtCore.QAbstractAnimation.Backward
#             toggleButton.setArrowType(arrow_type)
#             self.toggleAnimation.setDirection(direction)
#             self.toggleAnimation.start()
#
#         self.toggleButton.clicked.connect(start_animation)
#
#     def setContentLayout(self, contentLayout):
#         # Not sure if this is equivalent to self.contentArea.destroy()
#         self.contentArea.destroy()
#         self.contentArea.setLayout(contentLayout)
#         collapsedHeight = self.sizeHint().height() - self.contentArea.maximumHeight()
#         contentHeight = contentLayout.sizeHint().height()
#         for i in range(self.toggleAnimation.animationCount()-1):
#             spoilerAnimation = self.toggleAnimation.animationAt(i)
#             spoilerAnimation.setDuration(self.animationDuration)
#             spoilerAnimation.setStartValue(collapsedHeight)
#             spoilerAnimation.setEndValue(collapsedHeight + contentHeight)
#         contentAnimation = self.toggleAnimation.animationAt(self.toggleAnimation.animationCount() - 1)
#         contentAnimation.setDuration(self.animationDuration)
#         contentAnimation.setStartValue(0)
#         contentAnimation.setEndValue(contentHeight)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_window = MainWin()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import (QPushButton, QDialog, QTreeWidget,
#                              QTreeWidgetItem, QVBoxLayout,
#                              QHBoxLayout, QFrame, QLabel,
#                              QApplication)
# import sys
#
# class SectionExpandButton(QPushButton):
#     """a QPushbutton that can expand or collapse its section
#     """
#     def __init__(self, item, text = "", parent = None):
#         super().__init__(text, parent)
#         self.section = item
#         self.clicked.connect(self.on_clicked)
#
#     def on_clicked(self):
#         """toggle expand/collapse of section by clicking
#         """
#         if self.section.isExpanded():
#             self.section.setExpanded(False)
#         else:
#             self.section.setExpanded(True)
#
#
# class CollapsibleDialog(QDialog):
#     """a dialog to which collapsible sections can be added;
#     subclass and reimplement define_sections() to define sections and
#         add them as (title, widget) tuples to self.sections
#     """
#     def __init__(self):
#         super().__init__()
#         self.tree = QTreeWidget()
#         self.tree.setHeaderHidden(True)
#         layout = QVBoxLayout()
#         layout.addWidget(self.tree)
#
#         l1 = QLabel('main_layout')
#         layout.addWidget(l1)
#
#         self.setLayout(layout)
#         self.tree.setIndentation(0)
#
#         self.sections = []
#         self.define_sections()
#         self.add_sections()
#
#     def add_sections(self):
#         """adds a collapsible sections for every
#         (title, widget) tuple in self.sections
#         """
#         for (title, widget) in self.sections:
#             button1 = self.add_button(title)
#             section1 = self.add_widget(button1, widget)
#             button1.addChild(section1)
#
#     def define_sections(self):
#         """reimplement this to define all your sections
#         and add them as (title, widget) tuples to self.sections
#         """
#         widget = QFrame(self.tree)
#         layout = QHBoxLayout(widget)
#         layout.addWidget(QLabel("text1"))
#         layout.addWidget(QLabel("text2"))
#         title = "Section 1"
#         self.sections.append((title, widget))
#
#     def add_button(self, title):
#         """creates a QTreeWidgetItem containing a button
#         to expand or collapse its section
#         """
#         item = QTreeWidgetItem()
#         self.tree.addTopLevelItem(item)
#         self.tree.setItemWidget(item, 0, SectionExpandButton(item, text = title))
#         return item
#
#     def add_widget(self, button, widget):
#         """creates a QWidgetItem containing the widget,
#         as child of the button-QWidgetItem
#         """
#         section = QTreeWidgetItem(button)
#         section.setDisabled(True)
#         self.tree.setItemWidget(section, 0, widget)
#         return section
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = CollapsibleDialog()
#     window.show()
#     sys.exit(app.exec_())
