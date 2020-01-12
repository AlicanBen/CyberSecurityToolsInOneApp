from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QGroupBox, QWidget, QLabel, QLineEdit, QCheckBox
from Utils.Tools import Tools


class Dnsenum:

    def __init__(self):

        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(250)
        self.win.setMinimumHeight(200)
        self.win.setWindowTitle("Dnsenum")
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

        self.startButton=QPushButton("Enumerate")
        self.vBox.addWidget(self.startButton)

    def options(self):
        self.optionsGBox=QGroupBox("Options");
        vBox=QVBoxLayout()

        skip_reverse_lookup = QCheckBox()
        threads = QCheckBox()
        all_progress = QCheckBox()


        skip_reverse_lookup.setText("Skip the reverse lookup operations.")
        threads.setText("The number of threads that will perform different queries.")
        all_progress.setText("Show all the progress and all the error messages.")


        vBox.addWidget(skip_reverse_lookup)
        vBox.addWidget(threads)
        vBox.addWidget(all_progress)

        self.optionsGBox.setLayout(vBox)

    def optionsController(self, checkBox):
        if (checkBox.isChecked()):
            self.optionsGBox.setVisible(True)
            self.win.setMinimumHeight(320)
            self.win.setMinimumWidth(420)


        else:
            self.optionsGBox.setVisible(False)
            self.win.setFixedHeight(200)
            self.win.setFixedWidth(250)



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