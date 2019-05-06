from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (
        QMainWindow, QPushButton, QWidget, QTabWidget, QVBoxLayout,
        QGridLayout)
import pyqtgraph as pg
import sys
import datetime as dt
import os


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Computer Control GUI")
        self.setGeometry(700, 300, 600, 200)
        # message at the bottom
        self.statusBar().showMessage("Take control over your computer")

        self.simple_graph = TabWidget()
        self.setCentralWidget(self.simple_graph)

        self.show()


class TabWidget(QTabWidget):
    def __init__(self):
        super(TabWidget, self).__init__()
        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.internet_control_tab = TabInternetControl()
        self.website_control_tab = TabWebsiteControl()
        # Add tabs
        self.addTab(self.internet_control_tab, "Internet control")
        self.addTab(self.website_control_tab, "Block websites")


class TabInternetControl(QWidget):
    def __init__(self):
        self.ACTIVATE_N_MINUTES = 15
        super().__init__()

        self.init_ui()

    def init_ui(self):
        """ Create first tab with a button """
        self.layout = QGridLayout(self)
        # WHY label
        self.why_txt = QtGui.QLabel(
                "What do you want to activate internet for?")
        self.why_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.why_txt)
        # Line edit
        self.reason_le = QtGui.QLineEdit('')
        self.layout.addWidget(self.reason_le)
        # Button to save and add time
        self.save_and_activate_btn = QPushButton(
                f"Activate Internet for {self.ACTIVATE_N_MINUTES} minutes")
        self.save_and_activate_btn.clicked.connect(
                self.add_interval_of_activation_time_to_file)
        self.layout.addWidget(self.save_and_activate_btn)

    def add_interval_of_activation_time_to_file(self):
        # curr_path = os.path.dirname(__file__)
        curr_path = "/home/alex/Documents/improve_myself/internet_usage/"
        print('saving interval into file')
        start = dt.datetime.now()
        stop = start + dt.timedelta(minutes=self.ACTIVATE_N_MINUTES)
        print(start, stop)
        with open(os.path.join(
                curr_path, "activation_time_list.txt"), 'a') as f:
            f.writelines(f"{start.hour}:{start.minute},"
                         f"{stop.hour}:{stop.minute},"
                         f"{self.reason_le.text()},"
                         f"{start}\n")
        # restart internet
        os.system("rfkill unblock 1")
        # Set message telling that the activation was done properly
        self.activation_message_label = QtGui.QLabel("Activation completed")
        self.activation_message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.activation_message_label)


class TabWebsiteControl(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        """ Create first tab with a button """
        self.layout = QGridLayout(self)


if __name__ == '__main__':
    app = pg.mkQApp()
    simple_graph = App()
    sys.exit(app.exec_())