from PyQt5.QtWidgets import QMainWindow, QGridLayout, QPushButton, QVBoxLayout, QGroupBox, QWidget
from Utils.Tools import Tools


class Home:

    def __init__(self):

        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setGeometry(50, 50, 680, 557)
        self.win.setWindowTitle("Home")
        self.buttonGroups()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        self.createMenu()
        hbox=QVBoxLayout()
        hbox.addWidget(self.gridBox)
        wid.setLayout(hbox)

    def showWindow(self):
        self.win.show()

    def buttonGroups(self):
        self.gridBox=QGroupBox()
        grid=QGridLayout()
        grid.addWidget(QPushButton(Tools.CRUNCH.name),0,0)
        grid.addWidget(QPushButton(Tools.DIRB.name),0,1)
        grid.addWidget(QPushButton(Tools.DMITRY.name),0,2)
        grid.addWidget(QPushButton(Tools.DNSENUM.name),1,0)
        grid.addWidget(QPushButton(Tools.GPP_DECRYPT.name.replace("_","-")),1,1)
        grid.addWidget(QPushButton(Tools.HASH_IDENTIFIER.name.replace("_","-")),1,2)
        grid.addWidget(QPushButton(Tools.HASHCAT.name),2,0)
        grid.addWidget(QPushButton(Tools.HPING3.name),2,1)
        grid.addWidget(QPushButton(Tools.JOHN_THE_RIPPER.name.replace("_"," ")),2,2)
        grid.addWidget(QPushButton(Tools.MASKPROCESSOR.name),3,0)
        grid.addWidget(QPushButton(Tools.NETDISCOVER.name),3,1)
        grid.addWidget(QPushButton(Tools.NIKTO.name),3,2)
        grid.addWidget(QPushButton(Tools.NMAP.name),4,0)
        grid.addWidget(QPushButton(Tools.SEARCHPLOIT.name),4,1)
        grid.addWidget(QPushButton(Tools.THE_HARVESTER.name.replace("_"," ")),4,2)
        self.gridBox.setLayout(grid)

    def createMenu(self):
        bar=self.win.menuBar()

        bar.addAction("Home")

        tools=bar.addMenu("Tools")

        tools.addAction(Tools.CRUNCH.name)
        tools.addAction(Tools.DIRB.name)
        tools.addAction(Tools.DMITRY.name)
        tools.addAction(Tools.DNSENUM.name)
        tools.addAction(Tools.GPP_DECRYPT.name.replace("_","-"))
        tools.addAction(Tools.HASH_IDENTIFIER.name.replace("_","-"))
        tools.addAction(Tools.HASHCAT.name)
        tools.addAction(Tools.HPING3.name)
        tools.addAction(Tools.JOHN_THE_RIPPER.name.replace("_"," "))
        tools.addAction(Tools.MASKPROCESSOR.name)
        tools.addAction(Tools.NETDISCOVER.name)
        tools.addAction(Tools.NIKTO.name)
        tools.addAction(Tools.NMAP.name)
        tools.addAction(Tools.SEARCHPLOIT.name)
        tools.addAction(Tools.THE_HARVESTER.name.replace("_"," "))

        report=bar.addMenu("Report")

        report.addAction("Create")
        report.addAction("Show")
        report.addAction("Delete")
        bar.addAction("About Us")

    def __del__(self):
        self.win.close()
        print("asas")