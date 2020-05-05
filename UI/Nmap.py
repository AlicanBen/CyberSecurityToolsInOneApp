from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QLineEdit, QMainWindow, QLabel, \
    QCheckBox, QScrollArea, QRadioButton, QComboBox, QPushButton, QDesktopWidget

from Services import CommandExecuter
from Utils.Tools import Tools
from UI import Crunch, Dirb, Dmitry, Dnsenum, GppDecrypt, HashIdentifier, Hashcat, Hping3, JohnTheRipper, Maskprocessor, \
    Netdiscover, Nikto, Nmap, Searchploit, TheHarvester, Home, AboutUs


class Nmap:
    __command=[]
    def __init__(self):
        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(250)
        self.win.setMinimumHeight(400)
        self.win.setWindowTitle("Nmap")
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
        self.scan_range_edit=QLineEdit()
        self.scan_range_edit.setPlaceholderText("1.1.1.1/24")
        self.output_file_edit=QLineEdit()
        self.type_xml=QRadioButton("XML Output")
        self.type_txt=QRadioButton("TXT Output")
        self.scrolableOptions()
        self.speedComboBox()
        self.port_range=QLineEdit()
        self.button_scan=QPushButton("Scan")
        self.button_scan.clicked.connect(lambda : self.buttonHandler())


        self.vBox.addWidget(QLabel("Scan Range (e.g. 1.1.1.1/24)"))
        self.vBox.addWidget(self.scan_range_edit)
        self.vBox.addWidget(QLabel("Output Type"))
        self.vBox.addWidget(self.type_xml)
        self.vBox.addWidget(self.type_txt)
        self.vBox.addWidget(QLabel("Output File Name"))
        self.vBox.addWidget(self.output_file_edit)
        self.vBox.addWidget(self.options)
        self.vBox.addWidget(self.speedGBox)
        self.vBox.addWidget(QLabel("Port Range (e.g. 1-1000, default= all ports)"))
        self.vBox.addWidget(self.port_range)
        self.vBox.addWidget(self.button_scan)

    def scrolableOptions(self):
        self.options=QGroupBox("Options")
        self.options.setMaximumHeight(200)
        top_lvl_vBox=QVBoxLayout()
        self.optionScrollArea = QScrollArea()
        optionGBox = QGroupBox()
        vBox = QVBoxLayout()

        self.enableOSDetect = QCheckBox("Enable OS Detection")
        self.version_info = QCheckBox("Determine Service/Version İnfo")
        self.scan_Udp = QCheckBox("UDP Scan")
        self.scan_TCP_SYN = QCheckBox("TCP SYN Scan")
        self.scan_connect = QCheckBox("Connect Scan")
        self.scan_ACK = QCheckBox("ACK Scan")
        self.scan_window = QCheckBox("Window Scan")
        self.scan_maimon = QCheckBox("Maimon Scan")
        self.scan_TCP_null = QCheckBox("TCP Null Scan")
        self.scan_TCP_FIN = QCheckBox("TCP FIN Scan")
        self.scan_TCP_xmas = QCheckBox("TCP Xmas Scan")
        self.scan_SCTP_INIT = QCheckBox("SCTP INIT Scan")
        self.scan_COOKIE_ECHO = QCheckBox("COOKIE-ECHO Scan")


        vBox.addWidget(self.enableOSDetect)
        vBox.addWidget(self.version_info)
        vBox.addWidget(self.scan_Udp)
        vBox.addWidget(self.scan_TCP_SYN)
        vBox.addWidget(self.scan_connect)
        vBox.addWidget(self.scan_ACK)
        vBox.addWidget(self.scan_window)
        vBox.addWidget(self.scan_maimon)
        vBox.addWidget(self.scan_TCP_null)
        vBox.addWidget(self.scan_TCP_FIN)
        vBox.addWidget(self.scan_TCP_xmas)
        vBox.addWidget(self.scan_SCTP_INIT)
        vBox.addWidget(self.scan_COOKIE_ECHO)

        optionGBox.setLayout(vBox)
        self.optionScrollArea.setWidget(optionGBox)
        top_lvl_vBox.addWidget(self.optionScrollArea)
        self.options.setLayout(top_lvl_vBox)

    def speedComboBox(self):
        self.speedGBox=QGroupBox()
        self.speedGBox.setStyleSheet("QGroupBox { border-style: none;}")
        hbox=QHBoxLayout()
        hbox.addWidget(QLabel("Speed"))
        self.combobox=QComboBox()
        self.combobox.addItems(["Default(5)","1","2","3","4","5"])
        self.combobox.setCurrentText("Default(5)")
        hbox.addWidget(self.combobox)
        self.speedGBox.setLayout(hbox)

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
            self.ui = Nmap()
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


    def buttonHandler(self):
        if(self.enableOSDetect.isChecked()):
            self.__command.append("-O")
        if(self.version_info.isChecked()):
            self.__command.append("-sV")
        if(self.scan_Udp.isChecked()):
            self.__command.append("-sU")
        if(self.scan_TCP_SYN.isChecked()):
            self.__command.append("-sS")
        if(self.scan_connect.isChecked()):
            self.__command.append("-sT")
        if(self.scan_ACK.isChecked()):
            self.__command.append("-sA")
        if(self.scan_window.isChecked()):
            self.__command.append("-sW")
        if(self.scan_maimon.isChecked()):
            self.__command.append("-sM")
        if(self.scan_TCP_null.isChecked()):
            self.__command.append("-sN")
        if(self.scan_TCP_FIN.isChecked()):
            self.__command.append("-sF")
        if(self.scan_TCP_xmas.isChecked()):
            self.__command.append("-sX")
        if(self.scan_SCTP_INIT.isChecked()):
            self.__command.append("-sY")
        if(self.scan_COOKIE_ECHO.isChecked()):
            self.__command.append("-sZ")

        if(self.combobox.currentText()=="1"):
            self.__command.append("-T1")
        elif(self.combobox.currentText()=="2"):
            self.__command.append("-T2")
        elif(self.combobox.currentText()=="3"):
            self.__command.append("-T3")
        elif(self.combobox.currentText()=="4"):
            self.__command.append("-T4")
        elif(self.combobox.currentText()=="5"):
            self.__command.append("-T5")

        if(self.port_range.text()==""):
            self.__command.append("-p-")

        else:
            self.__command.append("-p")
            self.__command.append( self.port_range.text())

        if(self.type_txt.isChecked()):
            self.__command.append("-oN")
            self.__command.append(self.output_file_edit.text())
        elif(self.type_xml.isChecked()):
            self.__command.append("-oX")
            self.__command.append(self.output_file_edit.text())
        else:
            self.__command.append("-oX")
            self.__command.append("nmap.xml")

        self.__command.append(self.scan_range_edit.text())
        print(self.__command)

        cexec = CommandExecuter("nmap", self.__command)
        cexec.run()
        res = cexec.getResult()
        print(res.stdout.decode("utf-8"))


        self.__command.clear()
        cexec.clear()


    def __del__(self):
        self.win.close()