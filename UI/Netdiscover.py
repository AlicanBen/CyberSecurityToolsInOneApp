from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QLineEdit, QGroupBox, QMainWindow, QWidget, QComboBox, \
    QCheckBox, QHBoxLayout, QFileDialog

from Utils.Tools import Tools


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