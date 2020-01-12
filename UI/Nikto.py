from PyQt5.QtWidgets import QPushButton, QLineEdit, QHBoxLayout, QGroupBox, QVBoxLayout, QWidget, QMainWindow, \
    QCheckBox, QLabel, QRadioButton, QScrollArea

from Utils.Tools import Tools


class Nikto:
    def __init__(self):
        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(500)
        self.win.setWindowTitle("Nikto")
        self.form()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        wid.setLayout(self.hBox)
        self.createMenu()

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

        self.outputFormats()
        self.outputDisplay()

        self.host=QLineEdit()
        self.port=QLineEdit()
        self.output=QLineEdit()
        self.outputFormat=QCheckBox("Output Format (default : plain text)")
        self.outputFormat.toggled.connect(lambda : self.checkboxHandler(self.outputFormat,self.outputscrollArea))
        self.dbCheck=QCheckBox("Check Database")
        self.displayOutput=QCheckBox("Display Output")
        self.displayOutput.toggled.connect(lambda : self.checkboxHandler(self.displayOutput,self.displayScrollArea))

        vLayout.addWidget(QLabel("Target Host"))
        vLayout.addWidget(self.host)
        vLayout.addWidget(QLabel("Target Port"))
        vLayout.addWidget(self.port)
        vLayout.addWidget(QLabel("Output File Name"))
        vLayout.addWidget(self.output)
        vLayout.addWidget(self.dbCheck)
        vLayout.addWidget(self.outputFormat)
        vLayout.addWidget(self.outputscrollArea)
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

        vLayout.addWidget(self.tuningCheck)
        vLayout.addWidget(self.tuningScrollArea)
        vLayout.addWidget(self.runButton)

        self.rightBox.setLayout(vLayout)
    def createMenu(self):
        bar = self.win.menuBar()

        bar.addAction("Home")

        tools = bar.addMenu("Tools")

        tools.addAction(Tools.CRUNCH.name)
        tools.addAction(Tools.DIRB.name)
        tools.addAction(Tools.DMITRY.name)
        tools.addAction(Tools.DNSENUM.name)
        tools.addAction(Tools.GPP_DECRYPT.name.replace("_", "-"))
        tools.addAction(Tools.HASH_IDENTIFIER.name.replace("_", "-"))
        tools.addAction(Tools.HASHCAT.name)
        tools.addAction(Tools.HPING3.name)
        tools.addAction(Tools.JOHN_THE_RIPPER.name.replace("_", " "))
        tools.addAction(Tools.MASKPROCESSOR.name)
        tools.addAction(Tools.NETDISCOVER.name)
        tools.addAction(Tools.NIKTO.name)
        tools.addAction(Tools.NMAP.name)
        tools.addAction(Tools.SEARCHPLOIT.name)
        tools.addAction(Tools.THE_HARVESTER.name.replace("_", " "))

        report = bar.addMenu("Report")

        report.addAction("Create")
        report.addAction("Show")
        report.addAction("Delete")
        bar.addAction("About Us")

    def outputFormats(self):
        self.outputscrollArea = QScrollArea()
        self.outputscrollArea.setVisible(False)
        self.outputscrollArea.setFixedHeight(100)
        formatGBox=QGroupBox()
        vBox=QVBoxLayout()
        self.csv=QRadioButton("Comma-separated-value (csv file)")
        self.json=QRadioButton("JSON Format")
        self.html=QRadioButton("HTML Format")
        self.nbe=QRadioButton("Nessus NBE Format (nbe file)")
        self.sqlShema=QRadioButton("Generic SQL Shema")
        self.plainText=QRadioButton("Plain Text")

        vBox.addWidget(self.csv)
        vBox.addWidget(self.json)
        vBox.addWidget(self.html)
        vBox.addWidget(self.nbe)
        vBox.addWidget(self.sqlShema)
        vBox.addWidget(self.plainText)
        formatGBox.setLayout(vBox)
        self.outputscrollArea.setWidget(formatGBox)

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

        tuningGBox.setLayout(vBox)
        self.tuningScrollArea.setWidget(tuningGBox)
    def checkboxHandler(self,checbox,groupBox):
        if(checbox.isChecked()):
            groupBox.setVisible(True)
        else:
            groupBox.setVisible(False)
    def __del__(self):
        self.win.close()