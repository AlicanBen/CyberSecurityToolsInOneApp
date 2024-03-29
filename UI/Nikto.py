import os
import pathlib

from PyQt5.QtWidgets import QPushButton, QLineEdit, QHBoxLayout, QGroupBox, QVBoxLayout, QWidget, QMainWindow, \
    QCheckBox, QLabel, QRadioButton, QScrollArea, QDesktopWidget

from Reporting import Report
from Services import CommandExecuter
from UI import Crunch, Dirb, Dmitry, Dnsenum, GppDecrypt, HashIdentifier, Hashcat, Hping3, JohnTheRipper, Maskprocessor, \
    Netdiscover, Nikto, Nmap, Searchploit, TheHarvester, Home, AboutUs
from Utils import ReportPositions
from Utils.Tools import Tools


class Nikto:
    __command=[]
    def __init__(self):
        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(500)
        self.win.setWindowTitle("Nikto")
        self.center()
        self.form()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        wid.setLayout(self.hBox)
        self.createMenu()


    def center(self):
        frameGm = self.win.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.win.move(frameGm.topLeft())


    def showWindow(self):
        self.win.show()

    def form(self):
        self.hBox = QHBoxLayout()
        self.leftSide()
        self.rightSide()
        self.hBox.addWidget(self.leftBox)
        self.hBox.addWidget(self.rightBox)

    def leftSide(self):
        self.leftBox=QGroupBox()
        self.leftBox.setMinimumWidth(250)

        self.leftBox.setStyleSheet("QGroupBox { border-style: none;}")
        vLayout=QVBoxLayout()

        self.outputDisplay()

        self.host=QLineEdit()
        self.port=QLineEdit()
        self.dbCheck=QCheckBox("Check Database")
        self.displayOutput=QCheckBox("Display Output")
        self.displayOutput.toggled.connect(lambda : self.checkboxHandler(self.displayOutput,self.displayScrollArea))

        vLayout.addWidget(QLabel("Target Host"))
        vLayout.addWidget(self.host)
        vLayout.addWidget(QLabel("Target Port (Default: 80"))
        vLayout.addWidget(self.port)
        vLayout.addWidget(self.dbCheck)
        vLayout.addWidget(self.displayOutput)
        vLayout.addWidget(self.displayScrollArea)

        self.leftBox.setLayout(vLayout)

    def rightSide(self):
        self.rightBox = QGroupBox()
        self.rightBox.setMinimumWidth(250)
        self.rightBox.setStyleSheet("QGroupBox { border-style: none;}")
        vLayout = QVBoxLayout()
        self.tuningScrollBox()
        self.tuningCheck = QCheckBox("Scan Tuning")
        self.tuningCheck.toggled.connect(lambda: self.checkboxHandler(self.tuningCheck, self.tuningScrollArea))
        self.runButton= QPushButton("Run")
        self.runButton.clicked.connect(lambda : self.buttonHandler())

        vLayout.addWidget(self.tuningCheck)
        vLayout.addWidget(self.tuningScrollArea)
        vLayout.addWidget(self.runButton)

        self.rightBox.setLayout(vLayout)

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

        self.createReport=report.addAction("Create")
        self.createReport.triggered.connect(lambda: self.creatingReport())

        self.actionAboutUs = bar.addAction("About Us")
        self.actionAboutUs.triggered.connect(lambda: self.buttonClickHandler(self.actionAboutUs.text()))

    def creatingReport(self):
        r=Report()
        r.generateReport()


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
            self.ui = Nikto()
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


    def outputDisplay(self):
        self.displayScrollArea = QScrollArea()
        self.displayScrollArea.setVisible(False)
        self.displayScrollArea.setFixedHeight(100)
        formatGBox = QGroupBox()
        vBox = QVBoxLayout()
        self.redirect = QCheckBox("Show redirects")
        self.receivedCookies = QCheckBox("Show cookies received")
        self.OKResponse = QCheckBox("Show all 200/OK responses")
        self.requreAuthUrl = QCheckBox("Show URLs which require authentication")
        self.debugOutput = QCheckBox("Debug Output")
        self.verbose = QCheckBox("Verbose Output")

        vBox.addWidget(self.redirect)
        vBox.addWidget(self.receivedCookies)
        vBox.addWidget(self.OKResponse)
        vBox.addWidget(self.requreAuthUrl)
        vBox.addWidget(self.debugOutput)
        vBox.addWidget(self.verbose)

        formatGBox.setLayout(vBox)
        self.displayScrollArea.setWidget(formatGBox)

    def tuningScrollBox(self):
        self.tuningScrollArea = QScrollArea()
        self.tuningScrollArea.setVisible(False)
        self.tuningScrollArea.setFixedHeight(100)
        tuningGBox = QGroupBox()
        vBox = QVBoxLayout()
        self.file_upload = QCheckBox("File Upload")
        self.interesting_file = QCheckBox("Interesting File / Seen in logs")
        self.misconfiguration = QCheckBox("Misconfiguration / Default File")
        self.disclosure = QCheckBox("Information Disclosure ")
        self.injection = QCheckBox("Injection (XSS/Script/HTML)")
        self.rfRetrieval_in_web_root = QCheckBox("Remote File Retrieval - Inside Web Root")
        self.dos = QCheckBox("Denial of Service")
        self.rfRetrieval_server_wide = QCheckBox("Remote File Retrieval - Server Wide")
        self.remote_shell = QCheckBox("Command Execution / Remote Shell")
        self.sqlInjection = QCheckBox("SQL Injection")
        self.authBypass = QCheckBox("Authentication Bypass")
        self.swIdentification = QCheckBox("Software Identification ")
        self.rsInclusion = QCheckBox("Remote Source Inclusion")
        self.webService = QCheckBox("WebService")
        self.adminConsole = QCheckBox("Administrative Console")
        self.reverseTO = QCheckBox("Reverse Tuning Options (i.e., include all except specified)")

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
        vBox.addWidget(self.webService)
        vBox.addWidget(self.adminConsole)
        vBox.addWidget(self.reverseTO)

        tuningGBox.setLayout(vBox)
        self.tuningScrollArea.setWidget(tuningGBox)

    def checkboxHandler(self,checbox,groupBox):
        if(checbox.isChecked()):
            groupBox.setVisible(True)
        else:
            groupBox.setVisible(False)

    def buttonHandler(self):


        if (self.displayOutput.isChecked()):
            self.__command.append("-Display")
            displaystr = "P"
            if(self.redirect.isChecked()):
                displaystr+="1"
            if(self.receivedCookies.isChecked()):
                displaystr+="2"
            if(self.OKResponse.isChecked()):
                displaystr+="3"
            if(self.requreAuthUrl.isChecked()):
                displaystr+="4"
            if(self.debugOutput.isChecked()):
                displaystr+="D"
            if(self.verbose.isChecked()):
                displaystr+="V"
            self.__command.append(displaystr)

        if(pathlib.Path("./results/htmls/" + ReportPositions.NIKTO.name + ".html").exists()==True):
            os.remove("./results/htmls/" + ReportPositions.NIKTO.name + ".html")
        self.__command.append("-o")
        self.__command.append("./results/htmls/" + ReportPositions.NIKTO.name + ".html")
        self.__command.append("-Format")
        self.__command.append("htm")

        if(self.dbCheck.isChecked()):
            self.__command.append("-dbcheck")

        if(self.tuningCheck.isChecked()):
            tuningstr=""
            self.__command.append("-Tuning")
            if (self.file_upload.isChecked()):
                tuningstr+="0"
            if (self.interesting_file.isChecked()):
                tuningstr+="1"
            if (self.misconfiguration.isChecked()):
                tuningstr+="2"
            if (self.disclosure.isChecked()):
                tuningstr+="3"
            if (self.injection.isChecked()):
                tuningstr+="4"
            if (self.rfRetrieval_in_web_root.isChecked()):
                tuningstr+="5"
            if (self.dos.isChecked()):
                tuningstr+="6"
            if (self.rfRetrieval_server_wide.isChecked()):
                tuningstr+="7"
            if (self.remote_shell.isChecked()):
                tuningstr+="8"
            if (self.sqlInjection.isChecked()):
                tuningstr+="9"
            if (self.authBypass.isChecked()):
                tuningstr+="a"
            if (self.swIdentification.isChecked()):
                tuningstr+="b"
            if (self.rsInclusion.isChecked()):
                tuningstr+="c"
            if (self.webService.isChecked()):
                tuningstr+="d"
            if (self.adminConsole.isChecked()):
                tuningstr+="e"
            if (self.reverseTO.isChecked()):
                tuningstr+="x"
            self.__command.append(tuningstr)
        self.__command.append("-host")
        self.__command.append(self.host.text())

        if(self.port.text()!=""):
            self.__command.append("-port")
            self.__command.append(self.port.text())
        print(self.__command)
        cexec = CommandExecuter("nikto", self.__command)
        cexec.Popen()
        res = cexec.getResult()
        r=Report()
        r.setFileName(ReportPositions.NIKTO.name)
        print(res.communicate())
        self.__command.clear()
        cexec.clear()



    def __del__(self):
        self.win.close()