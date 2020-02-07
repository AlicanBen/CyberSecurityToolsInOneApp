from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QGroupBox, QWidget, QLabel, QLineEdit, QCheckBox, \
    QDesktopWidget

from Services import CommandExecuter
from Utils.Tools import Tools
from UI import Crunch, Dirb, Dmitry, Dnsenum, GppDecrypt, HashIdentifier, Hashcat, Hping3, JohnTheRipper, Maskprocessor, \
    Netdiscover, Nikto, Nmap, Searchploit, TheHarvester, Home, AboutUs


class Dmitry:
    __command=[]

    def __init__(self):

        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(250)
        self.win.setMinimumHeight(200)
        self.win.setWindowTitle("Dmitry")
        self.center()
        self.form()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        wid.setLayout(self.vBox)
        self.createMenu()

    def showWindow(self):
        self.win.show()

    def form(self):
        self.vBox=QVBoxLayout()
        self.vBox.addWidget(QLabel("URL/IP"))
        self.urlEdit=QLineEdit()
        self.vBox.addWidget(self.urlEdit)

        self.vBox.addWidget(QLabel("Output File Name"))
        self.outputFileedit = QLineEdit()
        self.vBox.addWidget(self.outputFileedit)
        self.options()
        self.optionsGBox.setVisible(False)
        self.optionUse = QCheckBox()
        self.optionUse.setText("Use Options")
        self.vBox.addWidget(self.optionUse)
        self.optionUse.toggled.connect(lambda : self.optionsController(self.optionUse))
        self.vBox.addWidget(self.optionsGBox)

        self.startButton=QPushButton("Start")
        self.startButton.clicked.connect(lambda :self.buttonHandler())
        self.vBox.addWidget(self.startButton)

    def options(self):
        self.optionsGBox=QGroupBox("Options");
        vBox=QVBoxLayout()

        self.whois_IP = QCheckBox()
        self.whois_Domain = QCheckBox()
        self.netCraft_info = QCheckBox()
        self.possible_subDomains = QCheckBox()
        self.possible_eMails = QCheckBox()
        self.tcp_port_scan = QCheckBox()

        self.whois_IP.setText("Whois lookup on the IP address of a host")
        self.whois_Domain.setText("Whois lookup on the domain name of a host ")
        self.netCraft_info.setText("Netcraft.com information on a host")
        self.possible_subDomains.setText("Search for possible subdomains")
        self.possible_eMails.setText("Search for possible email addresses")
        self.tcp_port_scan.setText("TCP port scan on a host")

        vBox.addWidget(self.whois_IP)
        vBox.addWidget(self.whois_Domain)
        vBox.addWidget(self.netCraft_info)
        vBox.addWidget(self.possible_subDomains)
        vBox.addWidget(self.possible_eMails)
        vBox.addWidget(self.tcp_port_scan)
        self.optionsGBox.setLayout(vBox)

    def optionsController(self, checkBox):
        if (checkBox.isChecked()):
            self.optionsGBox.setVisible(True)
            self.win.setMinimumHeight(400)


        else:
            self.optionsGBox.setVisible(False)
            self.win.setFixedHeight(200)

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
        self.actionAboutUs = bar.addAction("About Us")
        self.actionAboutUs.triggered.connect(lambda: self.buttonClickHandler(self.actionAboutUs.text()))

    def buttonClickHandler(self, text):
        self.window = QWidget()
        self.ui = None;
        if (text == Tools.CRUNCH.name):
            self.ui = Crunch.Crunch()
        elif (text == Tools.DIRB.name):
            self.ui = Dirb.Dirb()
        elif (text == Tools.DMITRY.name):
            self.ui = Dmitry()
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
            self.ui = TheHarvester.TheHarvester()
        elif (text == "Home"):
            self.ui = Home.Home()
        elif (text == "About Us"):
            self.ui = AboutUs.AboutUs()
        self.ui.createWindow()
        self.ui.showWindow()
        self.win.close()

    def center(self):
        frameGm = self.win.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.win.move(frameGm.topLeft())
    def buttonHandler(self):
        str=""
        if(self.optionUse.isChecked()):
            if(self.whois_IP.isChecked()):
                str+="i"
            if(self.whois_Domain.isChecked()):
                str += "w"
            if(self.netCraft_info.isChecked()):
                str += "n"
            if(self.possible_subDomains .isChecked()):
                str+="s"
            if(self.possible_eMails .isChecked()):
                str+="e"
            if(self.tcp_port_scan .isChecked()):
                str+="p"
            self.__command.append("-"+str)
        str=""

        if (self.outputFileedit.text() != ""):
            self.__command.append("-o")
            self.__command.append(self.outputFileedit.text())
        self.__command.append(self.urlEdit.text())

        print(self.__command)
        cexec = CommandExecuter("dmitry", self.__command)
        cexec.run()
        result = cexec.getResult()
        print(result.stderr.decode("utf-8"))
        print(result.stdout.decode("utf-8"))
        self.__command.clear()

    def __del__(self):
        self.win.close()