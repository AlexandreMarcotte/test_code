import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.UI()

    def UI(self):
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        page1 = FirstWidget(self)
        page1.visualize_btn.clicked.connect(self.P_2)
        self.central_widget.addWidget(page1)
        self.showMaximized()

    def P_2(self):
        page2 = VisualizeWidget(self)
        self.central_widget.addWidget(page2)
        self.central_widget.setCurrentWidget(page2)


class FirstWidget(QWidget):

    def __init__(self, parent=None):
        super(FirstWidget, self).__init__(parent)
        self.buttons()

    def buttons(self):
        self.btn2 = QPushButton("Visualize")
        self.buttonsLayout = QVBoxLayout()
        self.buttonsLayout.addWidget(self.btn2)
        self.visualize_btn = self.btn2
        self.setLayout(self.buttonsLayout)


class VisualizeWidget(QWidget):

    def __init__(self, parent=None):
        super(VisualizeWidget, self).__init__(parent)

        #Creation of the left layout
        self.dirmodel = QFileSystemModel()
        self.dirmodel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)    # Don't show files, just folders

        self.folder_view = QTreeView(parent=self)
        self.folder_view.setModel(self.dirmodel)
        self.folder_view.clicked[QModelIndex].connect(self.clicked)

        self.selectionModel = self.folder_view.selectionModel()

        self.now_layout = QVBoxLayout()
        self.now_layout.addWidget(self.folder_view)

        self.left_widget = QWidget()
        self.left_widget.setLayout(self.now_layout)

        #Creation of the right layout
        #self.right_widget = QTextEdit();

        self.btn1 = QPushButton('btn1')

        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(self.btn1)

        self.right_widget = QWidget()
        self.right_widget.setLayout(self.right_layout)

        splitter_filebrowser = QSplitter(Qt.Horizontal)
        splitter_filebrowser.addWidget(self.left_widget)
        splitter_filebrowser.addWidget(self.right_widget)
        splitter_filebrowser.setStretchFactor(1, 1)

        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter_filebrowser)

        self.setLayout(hbox)

    def set_path(self):
        self.dirmodel.setRootPath("")

    def clicked(self, index):
        index = self.selectionModel.currentIndex()
        dir_path = self.dirmodel.filePath(index)

        self.filemodel.setRootPath(dir_path)
        self.file_view.setRootIndex(self.filemodel.index(dir_path))

def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main())