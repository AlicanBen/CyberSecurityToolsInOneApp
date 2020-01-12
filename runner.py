import sys

from PyQt5.QtWidgets import QApplication

from UI import *

#windows=Home()
windows=Netdiscover()
def window():
    app = QApplication(sys.argv)
    windows.createWindow()
    windows.showWindow()
    sys.exit(app.exec_())

window()


