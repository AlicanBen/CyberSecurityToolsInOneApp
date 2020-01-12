from PyQt5.QtWidgets import QPushButton,  QVBoxLayout, QGroupBox, QLabel, QLineEdit, QMainWindow, QWidget

from Utils.Tools import Tools


class Maskprocessor:
    def __init__(self):
        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(250)
        self.win.setWindowTitle("Maskprocessor")
        self.form()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        wid.setLayout(self.vBox)
        self.createMenu()

    def showWindow(self):
        self.win.show()

    def form(self):
        self.vBox = QVBoxLayout()

        lbl_password=QLabel("Password (with builtin charset)")
        self.password_edit=QLineEdit()

        lbl_file_name = QLabel("Output File Name")
        self.file_name_edit = QLineEdit()

        gbox=QGroupBox()
        g_vBox=QVBoxLayout()

        g_vBox.addWidget(QLabel("Buildin charsets:"))
        g_vBox.addWidget(QLabel("     ?l = abcdefghijklmnopqrstuvwxyz"))
        g_vBox.addWidget(QLabel("     ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        g_vBox.addWidget(QLabel("     ?d = 0123456789"))
        g_vBox.addWidget(QLabel("     ?s =  !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"))
        g_vBox.addWidget(QLabel("     ?h = 8 bit characters from 0xc0 - 0xff"))
        g_vBox.addWidget(QLabel("     ?D = 8 bit characters from german alphabet"))
        g_vBox.addWidget(QLabel("     ?F = 8 bit characters from french alphabet"))
        g_vBox.addWidget(QLabel("     ?R = 8 bit characters from russian alphabet"))
        gbox.setLayout(g_vBox)

        self.createButton = QPushButton("Create List")

        self.vBox.addWidget(lbl_password)
        self.vBox.addWidget(self.password_edit)
        self.vBox.addWidget(lbl_file_name)
        self.vBox.addWidget(self.file_name_edit)
        self.vBox.addWidget(gbox)
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

    def __del__(self):
        self.win.close()