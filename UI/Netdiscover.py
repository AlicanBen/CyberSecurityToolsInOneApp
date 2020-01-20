from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QLineEdit, QGroupBox, QMainWindow, QWidget, QComboBox, \
    QCheckBox, QHBoxLayout, QFileDialog

from Utils.Tools import Tools

from UI import Crunch, Dirb, Dmitry, Dnsenum, GppDecrypt, HashIdentifier, Hashcat, Hping3, JohnTheRipper, Maskprocessor, \
    Netdiscover, Nikto, Nmap, Searchploit, TheHarvester,Home

class Netdiscover:
    def __init__(self):
        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(250)
        self.win.setWindowTitle("Netdiscover")
        self.form()

        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        wid.setLayout(self.vBox)
        self.createMenu()

    def showWindow(self):
        self.win.show()

    def form(self):
        self.vBox = QVBoxLayout()

        self.range_comboBox=QComboBox()
        self.range_comboBox.addItems(["Select One","Range","List Of Range File"])
        self.range_comboBox.setCurrentText("Select One")
        self.range_comboBox.currentTextChanged.connect(self.comboBoxChange)
        self.comboBoxGbox=QGroupBox()
        vBox=QVBoxLayout()
        self.comboBoxGbox.setVisible(False)

        self.range_label=QLabel("Range (e.g. 1.1.1.1/24)")
        self.range_edit=QLineEdit()
        self.fileDialog()
        self.rangeDialog()
        vBox.addWidget(self.rangeGBox)
        vBox.addWidget(self.fileGBox)

        self.comboBoxGbox.setLayout(vBox)

        lbl_file_name = QLabel("Output File Name")
        self.file_name_edit = QLineEdit()

        self.createButton = QPushButton("Run")
        self.vBox.addWidget(self.range_comboBox)
        self.vBox.addWidget(self.comboBoxGbox)
        self.vBox.addWidget(lbl_file_name)
        self.vBox.addWidget(self.file_name_edit)
        self.options()
        self.vBox.addWidget(self.createButton)

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
            self.ui = Netdiscover()
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

    def options(self):
        optionsGBox = QGroupBox("Options");
        vBox = QVBoxLayout()

        self.passive_mode_check = QCheckBox()
        self.sleep_time_check = QCheckBox()
        self.count_of_request = QCheckBox()


        self.passive_mode_check.setText("Passive Mode")

        self.sleep_time_check.setText("Time To Sleep Between Each ARP Request (default 1)")
        self.sleep_time_check.toggled.connect(lambda : self.timeCheckHandler(self.sleep_time_check))
        self.sleep_time_check_gBox=QGroupBox()
        self.sleep_time_edit=QLineEdit()
        a= QVBoxLayout()
        a.addWidget(self.sleep_time_edit)
        self.sleep_time_check_gBox.setLayout(a)
        self.sleep_time_check_gBox.setVisible(False)
        self.sleep_time_check


        self.count_of_request.setText("Number Of Times To Send Request")
        self.count_of_request.toggled.connect(lambda : self.countOfRequestCheckHandler(self.count_of_request))
        self.count_of_request_gBox=QGroupBox()
        self.count_of_request_edit=QLineEdit()
        b = QVBoxLayout()
        b.addWidget(self.count_of_request_edit)
        self.count_of_request_gBox.setLayout(b)
        self.count_of_request_gBox.setVisible(False)

        vBox.addWidget(self.passive_mode_check)
        vBox.addWidget(self.sleep_time_check)
        vBox.addWidget(self.sleep_time_check_gBox)
        vBox.addWidget(self.count_of_request)
        vBox.addWidget(self.count_of_request_gBox)
        optionsGBox.setLayout(vBox)
        self.vBox.addWidget(optionsGBox)

    def timeCheckHandler(self,checkBox):
        if (checkBox.isChecked()):
            self.sleep_time_check_gBox.setVisible(True)
        else:
            self.sleep_time_check_gBox.setVisible(False)

    def countOfRequestCheckHandler(self,checkBox):
        if (checkBox.isChecked()):
            self.count_of_request_gBox.setVisible(True)
        else:
            self.count_of_request_gBox.setVisible(False)

    def fileDialog(self):
        self.fileGBox=QGroupBox("List Of Range File")
        fileHbox=QHBoxLayout()
        self.fileButton=QPushButton("Select File")
        self.fileButton.clicked.connect(self.pushButton_handler)
        fileHbox.addWidget(self.fileButton)
        self.fileGBox.setLayout(fileHbox)

    def rangeDialog(self):
        self.rangeGBox = QGroupBox("Range (e.g. 1.1.1.1/24)")
        rangeeHbox = QHBoxLayout()
        self.range_edit = QLineEdit()
        rangeeHbox.addWidget(self.range_edit)
        self.rangeGBox.setLayout(rangeeHbox)

    def open_dialog_box(self):
        filedesc = QFileDialog.getOpenFileName()
        path = filedesc[0]
        fileName=path.split("/")
        self.fileButton.setText(fileName[-1])


    def pushButton_handler(self):
        print("Button pressed")
        self.open_dialog_box()

    def comboBoxChange(self):
        if (self.range_comboBox.currentText()=="Select One"):
            self.comboBoxGbox.setVisible(False)
        elif(self.range_comboBox.currentText()=="Range"):
            self.comboBoxGbox.setVisible(True)
            self.fileGBox.setVisible(False)
            self.rangeGBox.setVisible(True)
        elif(self.range_comboBox.currentText()=="List Of Range File"):
            self.comboBoxGbox.setVisible(True)
            self.rangeGBox.setVisible(False)
            self.fileGBox.setVisible(True)

    def __del__(self):
        self.win.close()