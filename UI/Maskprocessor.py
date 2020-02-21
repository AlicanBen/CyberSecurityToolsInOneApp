from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QGroupBox, QLabel, QLineEdit, QMainWindow, QWidget, QDesktopWidget

from Services import CommandExecuter
from Utils.Tools import Tools
from UI import Crunch, Dirb, Dmitry, Dnsenum, GppDecrypt, HashIdentifier, Hashcat, Hping3, JohnTheRipper, Maskprocessor, \
    Netdiscover, Nikto, Nmap, Searchploit, TheHarvester, Home, AboutUs


class Maskprocessor:
    __command=[]
    def __init__(self):
        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(250)
        self.win.setWindowTitle("Maskprocessor")
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
        self.createButton.clicked.connect(lambda :self.buttonHandler())

        self.vBox.addWidget(lbl_password)
        self.vBox.addWidget(self.password_edit)
        self.vBox.addWidget(lbl_file_name)
        self.vBox.addWidget(self.file_name_edit)
        self.vBox.addWidget(gbox)
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
        self.actionAboutUs = bar.addAction("About Us")
        self.actionAboutUs.triggered.connect(lambda: self.buttonClickHandler(self.actionAboutUs.text()))


    def buttonHandler(self):
        self.__command.append(self.password_edit.text())
        if(self.file_name_edit.text()!=""):
            self.__command.append("-o")
            self.__command.append(self.file_name_edit.text())
        print(self.__command)
        cexec = CommandExecuter("mp64", self.__command)
        cexec.run()
        res = cexec.getResult()
        print(res.stdout.decode("utf-8"))
        cexec.clear()


        self.__command.clear()
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
            self.ui = Maskprocessor()
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
            self.ui = Home.Home()
        elif (text == "About Us"):
            self.ui = AboutUs.AboutUs()
        self.ui.createWindow()
        self.ui.showWindow()
        self.win.close()

    def __del__(self):
        self.win.close()