import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


class Home:

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setGeometry(50, 50, 680, 557)
        self.win.setWindowTitle("Home")

    def showWindow(self):
        self.win.show()
