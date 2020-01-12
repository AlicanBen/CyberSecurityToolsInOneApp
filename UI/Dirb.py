from PyQt5.QtWidgets import QMainWindow, QGridLayout, QPushButton, QVBoxLayout, QGroupBox, QWidget, QLabel, QLineEdit, \
    QHBoxLayout, QCheckBox, QScrollArea, QRadioButton, QFileDialog
from Utils.Tools import Tools


class Dirb:

    def __init__(self):

        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(250)
        self.win.setWindowTitle("DIRB")
        self.form()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        wid.setLayout(self.vBox)
        self.createMenu()

    def showWindow(self):
        self.win.show()

    def form(self):
        self.vBox=QVBoxLayout()
        self.vBox.addWidget(QLabel("Url"))
        self.urlEdit=QLineEdit()
        self.vBox.addWidget(self.urlEdit)
        self.fileDialog()
        self.vBox.addWidget(self.fileGBox)
        self.vBox.addWidget(QLabel("Output File Name"))
        self.outputFileedit = QLineEdit()
        self.vBox.addWidget(self.outputFileedit)
        self.startButton=QPushButton("Start")
        self.vBox.addWidget(self.startButton)

    def fileDialog(self):
        self.fileGBox=QGroupBox("Directory List")
        fileHbox=QHBoxLayout()
        self.fileLabel=QLabel("Select file")
        fileHbox.addWidget(self.fileLabel)
        self.fileButton=QPushButton("File")
        self.fileButton.clicked.connect(self.pushButton_handler)
        fileHbox.addWidget(self.fileButton)
        self.fileGBox.setLayout(fileHbox)


    def open_dialog_box(self):
        filedesc = QFileDialog.getOpenFileName()
        path = filedesc[0]
        fileName=path.split("/")
        self.fileLabel.setText(fileName[-1])


    def pushButton_handler(self):
        print("Button pressed")
        self.open_dialog_box()


    def createMenu(self):
        bar=self.win.menuBar()

        bar.addAction("Home")

        tools=bar.addMenu("Tools")

        tools.addAction(Tools.CRUNCH.name)
        tools.addAction(Tools.DIRB.name)
        tools.addAction(Tools.DMITRY.name)
        tools.addAction(Tools.DNSENUM.name)
        tools.addAction(Tools.GPP_DECRYPT.name.replace("_","-"))
        tools.addAction(Tools.HASH_IDENTIFIER.name.replace("_","-"))
        tools.addAction(Tools.HASHCAT.name)
        tools.addAction(Tools.HPING3.name)
        tools.addAction(Tools.JOHN_THE_RIPPER.name.replace("_"," "))
        tools.addAction(Tools.MASKPROCESSOR.name)
        tools.addAction(Tools.NETDISCOVER.name)
        tools.addAction(Tools.NIKTO.name)
        tools.addAction(Tools.NMAP.name)
        tools.addAction(Tools.SEARCHPLOIT.name)
        tools.addAction(Tools.THE_HARVESTER.name.replace("_"," "))

        report=bar.addMenu("Report")

        report.addAction("Create")
        report.addAction("Show")
        report.addAction("Delete")
        bar.addAction("About Us")

    def __del__(self):
        self.win.close()