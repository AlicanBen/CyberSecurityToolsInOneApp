from PyQt5.QtWidgets import QMainWindow, QGridLayout, QPushButton, QVBoxLayout, QGroupBox, QWidget, QLabel, QLineEdit, \
    QHBoxLayout, QCheckBox, QScrollArea, QRadioButton, QFileDialog
from Utils.Tools import Tools


class Dmitry:

    def __init__(self):

        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(250)
        self.win.setMinimumHeight(200)
        self.win.setWindowTitle("Dmitry")
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
        self.vBox.addWidget(self.startButton)

    def options(self):
        self.optionsGBox=QGroupBox("Options");
        vBox=QVBoxLayout()

        whois_IP = QCheckBox()
        whois_Domain = QCheckBox()
        netCraft_info = QCheckBox()
        possible_subDomains = QCheckBox()
        possible_eMails = QCheckBox()
        tcp_port_scan = QCheckBox()

        whois_IP.setText("Whois lookup on the IP address of a host")
        whois_Domain.setText("Whois lookup on the domain name of a host ")
        netCraft_info.setText("Netcraft.com information on a host")
        possible_subDomains.setText("Search for possible subdomains")
        possible_eMails.setText("Search for possible email addresses")
        tcp_port_scan.setText("TCP port scan on a host")

        vBox.addWidget(whois_IP)
        vBox.addWidget(whois_Domain)
        vBox.addWidget(netCraft_info)
        vBox.addWidget(possible_subDomains)
        vBox.addWidget(possible_eMails)
        vBox.addWidget(tcp_port_scan)
        self.optionsGBox.setLayout(vBox)

    def optionsController(self, checkBox):
        if (checkBox.isChecked()):
            self.optionsGBox.setVisible(True)
            self.win.setMinimumHeight(400)


        else:
            self.optionsGBox.setVisible(False)
            self.win.setFixedHeight(200)



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