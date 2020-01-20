from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGroupBox, QHBoxLayout, \
    QFileDialog, QCheckBox, QScrollArea, QRadioButton

from Utils.Tools import Tools

from UI import Crunch, Dirb, Dmitry, Dnsenum, GppDecrypt, HashIdentifier, Hashcat, Hping3, JohnTheRipper, Maskprocessor, \
    Netdiscover, Nikto, Nmap, Searchploit, TheHarvester,Home

class Hashcat:
    def __init__(self):
        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(250)
        self.win.setWindowTitle("Hashcat")
        self.form()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        wid.setLayout(self.vBox)
        self.createMenu()

    def showWindow(self):
        self.win.show()

    def form(self):
        self.vBox = QVBoxLayout()

        self.fileDialog()
        self.vBox.addWidget(self.fileGBox)

        self.vBox.addWidget(QLabel("How To Seperate"))
        self.seperator = QLineEdit()
        self.vBox.addWidget(self.seperator)

        self.vBox.addWidget(QLabel("Output File Name"))
        self.outputFileedit = QLineEdit()
        self.vBox.addWidget(self.outputFileedit)
        self.outputFormatScrollAreas()
        self.attackModeScrollAreas()

        self.outputFormat = QCheckBox("Output Format")
        self.outputFormat.toggled.connect(lambda: self.checkboxHandler(self.outputFormat,self.outputFormatScrollArea))
        self.vBox.addWidget(self.outputFormat)
        self.vBox.addWidget(self.outputFormatScrollArea)

        self.attackMode = QCheckBox("Attack Mode")
        self.attackMode.toggled.connect(lambda: self.checkboxHandler(self.attackMode, self.attackModeScrollArea))
        self.vBox.addWidget(self.attackMode)
        self.vBox.addWidget(self.attackModeScrollArea)
        self.startButton = QPushButton("Start")
        self.vBox.addWidget(self.startButton)

    def fileDialog(self):
        self.fileGBox = QGroupBox("Hashed File")
        fileHbox = QHBoxLayout()
        self.fileLabel = QLabel("Select file")
        fileHbox.addWidget(self.fileLabel)
        self.fileButton = QPushButton("File")
        self.fileButton.clicked.connect(self.pushButton_handler)
        fileHbox.addWidget(self.fileButton)
        self.fileGBox.setLayout(fileHbox)

    def open_dialog_box(self):
        filedesc = QFileDialog.getOpenFileName()
        path = filedesc[0]
        fileName = path.split("/")
        self.fileLabel.setText(fileName[-1])

    def pushButton_handler(self):
        print("Button pressed")
        self.open_dialog_box()

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
            self.ui = TheHarvester.TheHarvester()
        elif (text == "Home"):
            self.win.close()
            self.ui = Home.Home()
        self.ui.createWindow()
        self.ui.showWindow()
        self.win.close()

    def checkboxHandler(self, checbox, groupBox):
        if (checbox.isChecked()):
            self.win.setMinimumWidth(300)
            self.win.setMinimumHeight(500)
            groupBox.setVisible(True)
        else:
            self.win.setFixedWidth(250)
            self.win.setFixedHeight(300)
            groupBox.setVisible(False)

    def outputFormatScrollAreas(self):
        self.outputFormatScrollArea = QScrollArea()
        self.outputFormatScrollArea.setVisible(False)
        self.outputFormatScrollArea.setFixedHeight(100)
        outputFormatGBox = QGroupBox()
        vBox = QVBoxLayout()
        self.hashWithSalt = QRadioButton("hash[:salt]")
        self.plain = QRadioButton("plain")
        self.hashWithSaltAndplain = QRadioButton("hash[:salt]: plain")
        self.hexPlain = QRadioButton("hex_plain")
        self.hashSaltWithHexPlain = QRadioButton("hash[:salt]: hex_plain")
        self.plainWithHexPlain = QRadioButton("plain: hex_plain")
        self.hashSaltPlainWithHexPlain = QRadioButton("hash[:salt]: plain:hex_plain")
        self.crackpos = QRadioButton("crackpos")
        self.hashSaltWithCrackpos = QRadioButton("hash[:salt]: crack_pos")
        self.plainWithCrackpos = QRadioButton("plain: crack_pos")
        self.hashSaltPlainWithCrackpos = QRadioButton("hash[:salt]: plain: crack_pos")
        self.hexPlainWithCrackpos = QRadioButton("hex_plain: crack_pos")
        self.hashSaltHexPlainWithCrackpos = QRadioButton("hash[:salt]: hex_plain:crack_pos")
        self.plainHexPlainWithCrackpos = QRadioButton("plain: hex_plain:crack_pos")
        self.hashSaltPlainHexPlainWithCrackpos = QRadioButton("hash[:salt]: plain:hex_plain: crack_pos")

        vBox.addWidget(self.hashWithSalt)
        vBox.addWidget(self.plain)
        vBox.addWidget(self.hashWithSaltAndplain)
        vBox.addWidget(self.hexPlain)
        vBox.addWidget(self.hashSaltWithHexPlain)
        vBox.addWidget(self.plainWithHexPlain)
        vBox.addWidget(self.hashSaltPlainWithHexPlain)
        vBox.addWidget(self.crackpos)
        vBox.addWidget(self.hashSaltWithCrackpos)
        vBox.addWidget(self.plainWithCrackpos)
        vBox.addWidget(self.hashSaltPlainWithCrackpos)
        vBox.addWidget(self.hexPlainWithCrackpos)
        vBox.addWidget(self.hashSaltHexPlainWithCrackpos)
        vBox.addWidget(self.plainHexPlainWithCrackpos)
        vBox.addWidget(self.hashSaltPlainHexPlainWithCrackpos)

        outputFormatGBox.setLayout(vBox)
        self.outputFormatScrollArea.setWidget(outputFormatGBox)

    def attackModeScrollAreas(self):
        self.attackModeScrollArea = QScrollArea()
        self.attackModeScrollArea.setVisible(False)
        self.attackModeScrollArea.setFixedHeight(100)
        attackModeGBox = QGroupBox()
        vBox = QVBoxLayout()
        self.straight = QRadioButton("Straight")
        self.combination = QRadioButton("Combination")
        self.bruteForce = QRadioButton("Brute - force")
        self.hybridWordlistPlusMask = QRadioButton(" Hybrid Wordlist + Mask")
        self.hybridMaskPlusWordlist = QRadioButton(" Hybrid Mask + Wordlist")



        vBox.addWidget(self.straight)
        vBox.addWidget(self.combination)
        vBox.addWidget(self.bruteForce)
        vBox.addWidget(self.hybridWordlistPlusMask)
        vBox.addWidget(self.hybridMaskPlusWordlist)

        attackModeGBox.setLayout(vBox)
        self.attackModeScrollArea.setWidget(attackModeGBox)

    def __del__(self):
        self.win.close()