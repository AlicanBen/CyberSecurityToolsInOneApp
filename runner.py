import sys

from PyQt5.QtWidgets import QApplication

from  UI import Home
from UI.Crunch import Crunch

#windows=Crunch()
windows=Crunch()
def window():
    app = QApplication(sys.argv)
    windows.createWindow()
    windows.showWindow()
    sys.exit(app.exec_())

window()


