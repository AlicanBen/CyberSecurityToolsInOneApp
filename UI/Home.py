from PyQt5.QtWidgets import QMainWindow, QGridLayout, QPushButton, QVBoxLayout, QGroupBox, QWidget, QDesktopWidget

from Reporting import Report
from UI import Crunch, Dirb, Dmitry, Dnsenum, GppDecrypt, HashIdentifier, Hashcat, Hping3, JohnTheRipper, Maskprocessor, \
    Netdiscover, Nikto, Nmap, Searchploit, TheHarvester, Home, AboutUs
from Utils.Tools import Tools


class Home:

    def __init__(self):

        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(500)
        self.win.setMinimumHeight(400)
        self.win.setWindowTitle("Home")
        self.center()
        self.buttonGroups()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        self.createMenu()
        hbox=QVBoxLayout()
        hbox.addWidget(self.gridBox)
        wid.setLayout(hbox)

    def center(self):
        frameGm = self.win.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.win.move(frameGm.topLeft())


    def showWindow(self):
        self.win.show()

    def buttonGroups(self):
        self.gridBox=QGroupBox()
        grid=QGridLayout()
        self.btnCrunc=QPushButton(Tools.CRUNCH.name)
        self.btnDirb=QPushButton(Tools.DIRB.name)
        self.btnDMitry=QPushButton(Tools.DMITRY.name)
        self.btnDnsenum=QPushButton(Tools.DNSENUM.name)
        self.btnGppDecrypt=QPushButton(Tools.GPP_DECRYPT.name.replace("_","-"))
        self.btnHashIdentifier=QPushButton(Tools.HASH_IDENTIFIER.name.replace("_","-"))
        self.btnHashcat=QPushButton(Tools.HASHCAT.name)
        self.btnHping=QPushButton(Tools.HPING3.name)
        self.btnJohnTheRipper=QPushButton(Tools.JOHN_THE_RIPPER.name.replace("_"," "))
        self.btnMaskprocessor=QPushButton(Tools.MASKPROCESSOR.name)
        self.btnNetdiscover=QPushButton(Tools.NETDISCOVER.name)
        self.btnNikto=QPushButton(Tools.NIKTO.name)
        self.btnNmap = QPushButton(Tools.NMAP.name)
        self.btnSearchploit = QPushButton(Tools.SEARCHPLOIT.name)
        self.btnTheHarvester = QPushButton(Tools.THE_HARVESTER.name.replace("_"," "))

        self.btnCrunc.clicked.connect(lambda:self.buttonClickHandler(self.btnCrunc.text()))
        self.btnDirb.clicked.connect(lambda:self.buttonClickHandler(self.btnDirb.text()))
        self.btnDMitry.clicked.connect(lambda:self.buttonClickHandler(self.btnDMitry.text()))
        self.btnDnsenum.clicked.connect(lambda:self.buttonClickHandler(self.btnDnsenum.text()))
        self.btnGppDecrypt.clicked.connect(lambda:self.buttonClickHandler(self.btnGppDecrypt.text()))
        self.btnHashIdentifier.clicked.connect(lambda:self.buttonClickHandler(self.btnHashIdentifier.text()))
        self.btnHashcat.clicked.connect(lambda:self.buttonClickHandler(self.btnHashcat.text()))
        self.btnHping.clicked.connect(lambda:self.buttonClickHandler(self.btnHping.text()))
        self.btnJohnTheRipper.clicked.connect(lambda:self.buttonClickHandler(self.btnJohnTheRipper.text()))
        self.btnMaskprocessor.clicked.connect(lambda:self.buttonClickHandler(self.btnMaskprocessor.text()))
        self.btnNetdiscover.clicked.connect(lambda:self.buttonClickHandler(self.btnNetdiscover.text()))
        self.btnNikto.clicked.connect(lambda:self.buttonClickHandler(self.btnNikto.text()))
        self.btnNmap.clicked.connect(lambda:self.buttonClickHandler(self.btnNmap.text()))
        self.btnSearchploit.clicked.connect(lambda:self.buttonClickHandler(self.btnSearchploit.text()))
        self.btnTheHarvester.clicked.connect(lambda:self.buttonClickHandler(self.btnTheHarvester.text()))

        grid.addWidget(self.btnCrunc,0,0)
        grid.addWidget(self.btnDirb,0,1)
        grid.addWidget(self.btnDMitry,0,2)
        grid.addWidget(self.btnDnsenum,1,0)
        grid.addWidget(self.btnGppDecrypt,1,1)
        grid.addWidget(self.btnHashIdentifier,1,2)
        grid.addWidget(self.btnHashcat,2,0)
        grid.addWidget(self.btnHping,2,1)
        grid.addWidget(self.btnJohnTheRipper,2,2)
        grid.addWidget(self.btnMaskprocessor,3,0)
        grid.addWidget(self.btnNetdiscover,3,1)
        grid.addWidget(self.btnNikto,3,2)
        grid.addWidget(self.btnNmap,4,0)
        grid.addWidget(self.btnSearchploit,4,1)
        grid.addWidget(self.btnTheHarvester,4,2)
        self.gridBox.setLayout(grid)

    def createMenu(self):
        bar = self.win.menuBar()

        self.actionHome=bar.addAction("Home")
        self.actionHome.triggered.connect(lambda: self.buttonClickHandler(self.actionHome.text()))

        tools = bar.addMenu("Tools")

        self.actionCrunch=tools.addAction(Tools.CRUNCH.name)
        self.actionCrunch.triggered.connect(lambda: self.buttonClickHandler(self.actionCrunch.text()))

        self.actionDirb=tools.addAction(Tools.DIRB.name)
        self.actionDirb.triggered.connect(lambda: self.buttonClickHandler(self.actionDirb.text()))

        self.actionDmitry= tools.addAction(Tools.DMITRY.name)
        self.actionDmitry.triggered.connect(lambda: self.buttonClickHandler(self.actionDmitry.text()))

        self.actionDnsenum= tools.addAction(Tools.DNSENUM.name)
        self.actionDnsenum.triggered.connect(lambda: self.buttonClickHandler(self.actionDnsenum.text()))

        self.actionGppDecrypt= tools.addAction(Tools.GPP_DECRYPT.name.replace("_", "-"))
        self.actionGppDecrypt.triggered.connect(lambda: self.buttonClickHandler(self.actionGppDecrypt.text()))

        self.actionHashIdentifier= tools.addAction(Tools.HASH_IDENTIFIER.name.replace("_", "-"))
        self.actionHashIdentifier.triggered.connect(lambda: self.buttonClickHandler(self.actionHashIdentifier.text()))

        self.actionHashcat= tools.addAction(Tools.HASHCAT.name)
        self.actionHashcat.triggered.connect(lambda: self.buttonClickHandler(self.actionHashcat.text()))

        self.actionHping= tools.addAction(Tools.HPING3.name)
        self.actionHping.triggered.connect(lambda: self.buttonClickHandler(self.actionHping.text()))

        self.actionJohnTheRipper= tools.addAction(Tools.JOHN_THE_RIPPER.name.replace("_", " "))
        self.actionJohnTheRipper.triggered.connect(lambda: self.buttonClickHandler(self.actionJohnTheRipper.text()))

        self.actionMaskprocessor= tools.addAction(Tools.MASKPROCESSOR.name)
        self.actionMaskprocessor.triggered.connect(lambda: self.buttonClickHandler(self.actionMaskprocessor.text()))

        self.actionNetdiscover= tools.addAction(Tools.NETDISCOVER.name)
        self.actionNetdiscover.triggered.connect(lambda: self.buttonClickHandler(self.actionNetdiscover.text()))

        self.actionNikto= tools.addAction(Tools.NIKTO.name)
        self.actionNikto.triggered.connect(lambda: self.buttonClickHandler(self.actionNikto.text()))

        self.actionNmap= tools.addAction(Tools.NMAP.name)
        self.actionNmap.triggered.connect(lambda: self.buttonClickHandler(self.actionNmap.text()))

        self.actionSearchploit= tools.addAction(Tools.SEARCHPLOIT.name)
        self.actionSearchploit.triggered.connect(lambda: self.buttonClickHandler(self.actionSearchploit.text()))

        self.actionTheHarvester= tools.addAction(Tools.THE_HARVESTER.name.replace("_", " "))
        self.actionTheHarvester.triggered.connect(lambda: self.buttonClickHandler(self.actionTheHarvester.text()))

        report = bar.addMenu("Reporting")

        self.createReport=report.addAction("Create")
        self.createReport.triggered.connect(lambda: self.creatingReport())

        self.actionAboutUs = bar.addAction("About Us")
        self.actionAboutUs.triggered.connect(lambda: self.buttonClickHandler(self.actionAboutUs.text()))

    def creatingReport(self):
        r=Report()
        r.generateReport()

    def buttonClickHandler(self,text):
        self.window=QWidget()
        self.ui=None;
        if(text==Tools.CRUNCH.name):
            self.ui = Crunch.Crunch()
        elif(text==Tools.DIRB.name):
            self.ui = Dirb.Dirb()
        elif(text==Tools.DMITRY.name):
            self.ui = Dmitry.Dmitry()
        elif(text==Tools.DNSENUM.name):
            self.ui = Dnsenum.Dnsenum()
        elif(text==Tools.GPP_DECRYPT.name.replace("_", "-")):
            self.ui = GppDecrypt.GppDecrypt()
        elif(text==Tools.HASH_IDENTIFIER.name.replace("_", "-")):
            self.ui = HashIdentifier.HashIdentifier()
        elif(text==Tools.HASHCAT.name):
            self.ui = Hashcat.Hashcat()
        elif(text==Tools.HPING3.name):
            self.ui = Hping3.Hping3()
        elif(text==Tools.JOHN_THE_RIPPER.name.replace("_", " ")):
            self.ui = JohnTheRipper.JohnTheRipper()
        elif(text==Tools.MASKPROCESSOR.name):
            self.ui = Maskprocessor.Maskprocessor()
        elif(text==Tools.NETDISCOVER.name):
            self.ui = Netdiscover.Netdiscover()
        elif(text==Tools.NIKTO.name):
            self.ui = Nikto.Nikto()
        elif(text==Tools.NMAP.name):
            self.ui = Nmap.Nmap()
        elif(text==Tools.SEARCHPLOIT.name):
            self.ui = Searchploit.Searchploit()
        elif(text==Tools.THE_HARVESTER.name.replace("_", " ")):
            self.ui = TheHarvester.TheHarvester()
        elif(text=="Home"):
            self.ui = Home.Home()
        elif (text == "About Us"):
            self.ui = AboutUs.AboutUs()
        self.ui.createWindow()
        self.ui.showWindow()
        self.win.close()


    def show(self):
        self.win.showMaximized()
    def __del__(self):
        self.win.close()
