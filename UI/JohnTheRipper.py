from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QGroupBox, QRadioButton, QPushButton, \
    QHBoxLayout, QFileDialog

from Services import CommandExecuter
from UI import Crunch, Dirb, Dmitry, Dnsenum, GppDecrypt, HashIdentifier, Hashcat, Hping3, JohnTheRipper, Maskprocessor, \
    Netdiscover, Nikto, Nmap, Searchploit, TheHarvester,Home
from Utils.Tools import Tools


class JohnTheRipper:
    __command=[]

    def __init__(self):
        super().__init__()

    def createWindow(self):
        self.passFileDirectory = ""
        self.listDirectory = ""
        self.win = QMainWindow()
        self.win.setMinimumWidth(250)
        self.win.setWindowTitle("John The Ripper")
        self.form()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        wid.setLayout(self.vBox)
        self.createMenu()

    def showWindow(self):
        self.win.show()

    def form(self):
        self.vBox=QVBoxLayout()
        self.listGBox = self.fileDialog("List")
        self.vBox.addWidget(self.listGBox)
        self.passfileGBox= self.fileDialog("Password File")
        self.vBox.addWidget(self.passfileGBox)
        self.startButton=QPushButton("Decrypt")
        self.startButton.clicked.connect(lambda : self.buttonHandler())
        self.vBox.addWidget(self.startButton)

    def fileDialog(self,title):
        fileGBox=QGroupBox(title)
        fileHbox=QHBoxLayout()
        fileButton=QPushButton("Select File")
        fileButton.clicked.connect(lambda :self.open_dialog_box(fileButton,title))
        fileHbox.addWidget(fileButton)
        fileGBox.setLayout(fileHbox)
        return fileGBox

    def open_dialog_box(self,fileButton,title):


        filedesc = QFileDialog.getOpenFileName()
        path = filedesc[0]
        fileName = path.split("/")
        fileButton.setText(fileName[-1])
        if(title=="List"):
            self.listDirectory = path
            print("list:", self.listDirectory)
        elif(title=="Password File"):
            self.passFileDirectory=path
            print("Password File:", self.passFileDirectory)
        print("list:", self.listDirectory)
        print("Password File:", self.passFileDirectory)

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
            self.ui = JohnTheRipper()
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

    def buttonHandler(self):
        self.__command.append("--wordlist="+self.listDirectory)
        self.__command.append("--rules")
        self.__command.append(self.passFileDirectory)
        print(self.__command)
        cexec = CommandExecuter("john", self.__command)
        cexec.run()
        res = cexec.getResult()

        print(res.stdout.decode("utf-8"))

        self.__command.clear()

    def __del__(self):
        self.win.close()