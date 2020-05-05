from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QGroupBox, QHBoxLayout, \
    QFileDialog, QCheckBox, QScrollArea, QDesktopWidget

from Services import CommandExecuter
from Utils.Tools import Tools
from UI import Crunch, Dirb, Dmitry, Dnsenum, GppDecrypt, HashIdentifier, Hashcat, Hping3, JohnTheRipper, Maskprocessor, \
    Netdiscover, Nikto, Nmap, Searchploit, TheHarvester, Home, AboutUs


class TheHarvester:
    __command=[]
    def __init__(self):

        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(320)
        self.win.setWindowTitle("The Harvester")
        self.center()
        self.form()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        wid.setLayout(self.vBox)
        self.createMenu()


    def center(self):
        frameGm = self.win.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.win.move(frameGm.topLeft())


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

        self.vBox.addWidget(QLabel("Start Result Number (Default:0)"))
        self.start = QLineEdit()
        self.vBox.addWidget(self.start)


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
        self.startButton.clicked.connect(lambda : self.buttonHandler())

        self.vBox.addWidget(self.startButton)

    def sourceScrollArea(self):
        self.sourceScrollArea = QScrollArea()
        self.sourceScrollArea.setVisible(False)
        self.sourceScrollArea.setMinimumWidth(300)
        self.sourceScrollArea.setFixedHeight(100)
        sourceGBox = QGroupBox()
        vBox = QVBoxLayout()


        self.baidu= QCheckBox("Badiu")
        self.bing= QCheckBox("Bing")
        self.bingapi= QCheckBox("Bing API")
        self.certspotter= QCheckBox("Certspotter")
        self.crtsh= QCheckBox("Crtsh")
        self.dnsdumpster= QCheckBox("Dnsdumpster")
        self.dogpile= QCheckBox("Dogpile")
        self.duckduckgo= QCheckBox("Duckduckgo")
        self.github_code= QCheckBox("Github Code")
        self.google= QCheckBox("Google")
        self.hunter= QCheckBox("Hunter")
        self.intelx= QCheckBox("IntelX")
        self.linkedin= QCheckBox("Linked In")
        self.linkedin_links= QCheckBox("Linked In Links")
        self.netcraft= QCheckBox("Netcraft")
        self.otx= QCheckBox("Otx")
        self.securityTrails= QCheckBox("Securiyt Trails")
        self.threatcrowd= QCheckBox("Threat Crowd")
        self.trello= QCheckBox("Trello")
        self.twitter= QCheckBox("Twitter")
        self.vhost= QCheckBox("Vhost")
        self.virustotal= QCheckBox("Virustotal")
        self.yahoo= QCheckBox("Yahoo")
        self.all= QCheckBox("All")

        vBox.addWidget(self.baidu)
        vBox.addWidget(self.bing)
        vBox.addWidget(self.bingapi)
        vBox.addWidget(self.certspotter)
        vBox.addWidget(self.crtsh)
        vBox.addWidget(self.dnsdumpster)
        vBox.addWidget(self.dogpile)
        vBox.addWidget(self.duckduckgo)
        vBox.addWidget(self.github_code)
        vBox.addWidget(self.google)
        vBox.addWidget(self.hunter)
        vBox.addWidget(self.intelx)
        vBox.addWidget(self.linkedin)
        vBox.addWidget(self.linkedin_links)
        vBox.addWidget(self.netcraft)
        vBox.addWidget(self.otx)
        vBox.addWidget(self.securityTrails)
        vBox.addWidget(self.threatcrowd)
        vBox.addWidget(self.trello)
        vBox.addWidget(self.twitter)
        vBox.addWidget(self.vhost)
        vBox.addWidget(self.virustotal)
        vBox.addWidget(self.yahoo)
        vBox.addWidget(self.all)

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

        report = bar.addMenu("Reporting")

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
            self.ui = Home.Home()
        elif (text == "About Us"):
            self.ui = AboutUs.AboutUs()
        self.ui.createWindow()
        self.ui.showWindow()
        self.win.close()


    def buttonHandler(self):
        if(self.domain.text()!=""):
            self.__command.append("-d")
            self.__command.append(self.domain.text())

        if(self.limit.text()==""):
            self.__command.append("-l")
            self.__command.append("500")
        else:
            self.__command.append("-l")
            self.__command.append(self.limit.text())
        if (self.start.text() != ""):
            self.__command.append("-S")
            self.__command.append(self.start.text())

        if(self.outputFileedit.text()==""):
            self.__command.append("-f")
            self.__command.append("harvesterResult.xml")
        else:
            self.__command.append("-f")
            self.__command.append(self.outputFileedit.text())

        if(self.useShodan.isChecked()):
            self.__command.append("-s")

        if(self.source.isChecked()):
            self.__command.append("-b")
            if(self.baidu.isChecked()):
                self.__command.append("baidu")
            if(self.bing.isChecked()):
                self.__command.append("bing")
            if(self.bingapi.isChecked()):
                self.__command.append("bingapi")
            if(self.certspotter.isChecked()):
                self.__command.append("certspotter")
            if(self.crtsh.isChecked()):
                self.__command.append("crtsh")
            if(self.dnsdumpster.isChecked()):
                self.__command.append("dnsdumpster")
            if(self.dogpile.isChecked()):
                self.__command.append("dogpile")
            if(self.duckduckgo.isChecked()):
                self.__command.append("duckduckgo")
            if(self.github_code.isChecked()):
                self.__command.append("github-code")
            if(self.google.isChecked()):
                self.__command.append("google")
            if(self.hunter.isChecked()):
                self.__command.append("hunter")
            if(self.intelx.isChecked()):
                self.__command.append("intelx")
            if(self.linkedin.isChecked()):
                self.__command.append("linkedin")
            if(self.linkedin_links.isChecked()):
                self.__command.append("linkedin_links")
            if(self.netcraft.isChecked()):
                self.__command.append("netcraft")
            if(self.otx.isChecked()):
                self.__command.append("otx")
            if(self.securityTrails.isChecked()):
                self.__command.append("securityTrails")
            if(self.threatcrowd.isChecked()):
                self.__command.append("threatcrowd")
            if(self.trello.isChecked()):
                self.__command.append("trello")
            if(self.twitter.isChecked()):
                self.__command.append("twitter")
            if(self.vhost.isChecked()):
                self.__command.append("vhost")
            if(self.virustotal.isChecked()):
                self.__command.append("virustotal")
            if(self.yahoo.isChecked()):
                self.__command.append("yahoo")
            if(self.all.isChecked()):
                self.__command.append("all")

        print(self.__command)
        cexec = CommandExecuter("theHarvester", self.__command)
        cexec.run()
        res = cexec.getResult()
        print(res.stdout.decode("utf-8"))
        print("************************")
        print(res.stderr.decode("utf-8"))
        self.__command.clear()
        cexec.clear()

    def __del__(self):
        self.win.close()