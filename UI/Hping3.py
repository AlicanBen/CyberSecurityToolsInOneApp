from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QLabel, \
    QRadioButton

from Utils.Tools import Tools


class Hping3:
    def __init__(self):
        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(250)
        self.win.setWindowTitle("Hping3")
        self.form()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        wid.setLayout(self.vBox)
        self.createMenu()

    def showWindow(self):
        self.win.show()

    def form(self):
        self.vBox = QVBoxLayout()

        lbl_url=QLabel("URL")
        self.url_edit=QLineEdit()

        gbox=QGroupBox("Mode")
        g_vBox=QVBoxLayout()

        self.mode_rawIp = QRadioButton("RAW IP mode")
        self.mode_ICMP = QRadioButton("ICMP mode")
        self.mode_UDP = QRadioButton("UDP mode")
        self.mode_SCAN = QRadioButton("SCAN mode")

        g_vBox.addWidget(self.mode_rawIp)
        g_vBox.addWidget(self.mode_ICMP)
        g_vBox.addWidget(self.mode_UDP)
        g_vBox.addWidget(self.mode_SCAN)
        gbox.setLayout(g_vBox)

        self.searchButton = QPushButton("Identify")

        self.vBox.addWidget(lbl_url)
        self.vBox.addWidget(self.url_edit)
        self.vBox.addWidget(gbox)
        self.vBox.addWidget(self.searchButton)

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

    def __del__(self):
        self.win.close()