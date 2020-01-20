from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QGroupBox, QHBoxLayout, \
    QFileDialog, QCheckBox, QScrollArea

from Utils.Tools import Tools
from UI import Crunch, Dirb, Dmitry, Dnsenum, GppDecrypt, HashIdentifier, Hashcat, Hping3, JohnTheRipper, Maskprocessor, \
    Netdiscover, Nikto, Nmap, Searchploit, TheHarvester,Home

class TheHarvester:
    def __init__(self):

        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(320)
        self.win.setWindowTitle("The Harvester")
        self.form()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        wid.setLayout(self.vBox)
        self.createMenu()

    def showWindow(self):
        self.win.show()

    def form(self):
        self.vBox=QVBoxLayout()
        self.vBox.addWidget(QLabel("Company Name/Domain"))
        self.domain = QLineEdit()
        self.vBox.addWidget(self.domain)

        self.vBox.addWidget(QLabel("Limit Of Result (Default:500"))
        self.limit = QLineEdit()
        self.vBox.addWidget(self.limit)

        self.vBox.addWidget(QLabel("Start Result Number (Default:0"))
        self.limit = QLineEdit()
        self.vBox.addWidget(self.limit)


        self.vBox.addWidget(QLabel("Output File Name"))
        self.outputFileedit = QLineEdit()
        self.vBox.addWidget(self.outputFileedit)
        self.useShodan=QCheckBox("Use Shodan")
        self.vBox.addWidget(self.useShodan)

        self.sourceScrollArea()
        self.source=QCheckBox("Source")
        self.vBox.addWidget(self.source)

        self.source.toggled.connect(lambda: self.checkboxHandler(self.source, self.sourceScrollArea))
        self.vBox.addWidget(self.sourceScrollArea)
        self.startButton=QPushButton("Run")
        self.vBox.addWidget(self.startButton)

    def sourceScrollArea(self):
        self.sourceScrollArea = QScrollArea()
        self.sourceScrollArea.setVisible(False)
        self.sourceScrollArea.setMinimumWidth(300)
        self.sourceScrollArea.setFixedHeight(100)
        sourceGBox = QGroupBox()
        vBox = QVBoxLayout()
        self.file_upload = QCheckBox("File Upload")
        self.interesting_file = QCheckBox("Interesting File / Seen in logs")
        self.misconfiguration = QCheckBox("Misconfiguration / Default File")
        self.disclosure = QCheckBox("Information Disclosure ")
        self.injection = QCheckBox("Injection (XSS/Script/HTML)")
        self.rfRetrieval_in_web_root = QCheckBox("Remote File Retrieval - Inside Web Root")
        self.rfRetrieval_in_web_root.setMinimumWidth(300)
        self.dos = QCheckBox("Denial of Service")
        self.rfRetrieval_server_wide = QCheckBox("Remote File Retrieval - Server Wide")
        self.remote_shell = QCheckBox("Command Execution / Remote Shell")
        self.sqlInjection = QCheckBox("SQL Injection")
        self.authBypass = QCheckBox("Authentication Bypass")
        self.swIdentification = QCheckBox("Software Identification ")
        self.rsInclusion = QCheckBox("Remote Source Inclusion")
        self.adminConsole = QCheckBox("Administrative Console")

        vBox.addWidget(self.file_upload)
        vBox.addWidget(self.interesting_file)
        vBox.addWidget(self.misconfiguration)
        vBox.addWidget(self.disclosure)
        vBox.addWidget(self.injection)
        vBox.addWidget(self.rfRetrieval_in_web_root)
        vBox.addWidget(self.dos)
        vBox.addWidget(self.rfRetrieval_server_wide)
        vBox.addWidget(self.remote_shell)
        vBox.addWidget(self.sqlInjection)
        vBox.addWidget(self.authBypass)
        vBox.addWidget(self.swIdentification)
        vBox.addWidget(self.rsInclusion)
        vBox.addWidget(self.adminConsole)

        sourceGBox.setLayout(vBox)
        self.sourceScrollArea.setWidget(sourceGBox)

    def checkboxHandler(self, checbox, groupBox):
        if (checbox.isChecked()):
            groupBox.setVisible(True)
        else:
            groupBox.setVisible(False)

    def createMenu(self):
        bar = self.win.menuBar()

        self.actionHome = bar.addAction("Home")
        self.actionHome.triggered.connect(lambda: self.buttonClickHandler(self.actionHome.text()))

        tools = bar.addMenu("Tools")

        self.actionCrunch = tools.addAction(Tools.CRUNCH.name)
        self.actionCrunch.triggered.connect(lambda: self.buttonClickHandler(self.actionCrunch.text()))

        self.actionDirb = tools.addAction(Tools.DIRB.name)
        self.actionDirb.triggered.connect(lambda: self.buttonClickHandler(self.actionDirb.text()))

        self.actionDmitry = tools.addAction(Tools.DMITRY.name)
        self.actionDmitry.triggered.connect(lambda: self.buttonClickHandler(self.actionDmitry.text()))

        self.actionDnsenum = tools.addAction(Tools.DNSENUM.name)
        self.actionDnsenum.triggered.connect(lambda: self.buttonClickHandler(self.actionDnsenum.text()))

        self.actionGppDecrypt = tools.addAction(Tools.GPP_DECRYPT.name.replace("_", "-"))
        self.actionGppDecrypt.triggered.connect(lambda: self.buttonClickHandler(self.actionGppDecrypt.text()))

        self.actionHashIdentifier = tools.addAction(Tools.HASH_IDENTIFIER.name.replace("_", "-"))
        self.actionHashIdentifier.triggered.connect(lambda: self.buttonClickHandler(self.actionHashIdentifier.text()))

        self.actionHashcat = tools.addAction(Tools.HASHCAT.name)
        self.actionHashcat.triggered.connect(lambda: self.buttonClickHandler(self.actionHashcat.text()))

        self.actionHping = tools.addAction(Tools.HPING3.name)
        self.actionHping.triggered.connect(lambda: self.buttonClickHandler(self.actionHping.text()))

        self.actionJohnTheRipper = tools.addAction(Tools.JOHN_THE_RIPPER.name.replace("_", " "))
        self.actionJohnTheRipper.triggered.connect(lambda: self.buttonClickHandler(self.actionJohnTheRipper.text()))

        self.actionMaskprocessor = tools.addAction(Tools.MASKPROCESSOR.name)
        self.actionMaskprocessor.triggered.connect(lambda: self.buttonClickHandler(self.actionMaskprocessor.text()))

        self.actionNetdiscover = tools.addAction(Tools.NETDISCOVER.name)
        self.actionNetdiscover.triggered.connect(lambda: self.buttonClickHandler(self.actionNetdiscover.text()))

        self.actionNikto = tools.addAction(Tools.NIKTO.name)
        self.actionNikto.triggered.connect(lambda: self.buttonClickHandler(self.actionNikto.text()))

        self.actionNmap = tools.addAction(Tools.NMAP.name)
        self.actionNmap.triggered.connect(lambda: self.buttonClickHandler(self.actionNmap.text()))

        self.actionSearchploit = tools.addAction(Tools.SEARCHPLOIT.name)
        self.actionSearchploit.triggered.connect(lambda: self.buttonClickHandler(self.actionSearchploit.text()))

        self.actionTheHarvester = tools.addAction(Tools.THE_HARVESTER.name.replace("_", " "))
        self.actionTheHarvester.triggered.connect(lambda: self.buttonClickHandler(self.actionTheHarvester.text()))

        report = bar.addMenu("Report")

        report.addAction("Create")
        report.addAction("Show")
        report.addAction("Delete")
        bar.addAction("About Us")

    def buttonClickHandler(self, text):
        self.window = QWidget()
        self.ui = None;
        if (text == Tools.CRUNCH.name):
            self.ui = Crunch.Crunch()
        elif (text == Tools.DIRB.name):
            self.ui = Dirb.Dirb()
        elif (text == Tools.DMITRY.name):
            self.ui = Dmitry.Dmitry()
        elif (text == Tools.DNSENUM.name):
            self.ui = Dnsenum.Dnsenum()
        elif (text == Tools.GPP_DECRYPT.name.replace("_", "-")):
            self.ui = GppDecrypt.GppDecrypt()
        elif (text == Tools.HASH_IDENTIFIER.name.replace("_", "-")):
            self.ui = HashIdentifier.HashIdentifier()
        elif (text == Tools.HASHCAT.name):
            self.ui = Hashcat.Hashcat()
        elif (text == Tools.HPING3.name):
            self.ui = Hping3.Hping3()
        elif (text == Tools.JOHN_THE_RIPPER.name.replace("_", " ")):
            self.ui = JohnTheRipper.JohnTheRipper()
        elif (text == Tools.MASKPROCESSOR.name):
            self.ui = Maskprocessor.Maskprocessor()
        elif (text == Tools.NETDISCOVER.name):
            self.ui = Netdiscover.Netdiscover()
        elif (text == Tools.NIKTO.name):
            self.ui = Nikto.Nikto()
        elif (text == Tools.NMAP.name):
            self.ui = Nmap.Nmap()
        elif (text == Tools.SEARCHPLOIT.name):
            self.ui = Searchploit.Searchploit()
        elif (text == Tools.THE_HARVESTER.name.replace("_", " ")):
            self.ui = TheHarvester()
        elif (text == "Home"):
            self.win.close()
            self.ui = Home.Home()
        self.ui.createWindow()
        self.ui.showWindow()
        self.win.close()

    def __del__(self):
        self.win.close()