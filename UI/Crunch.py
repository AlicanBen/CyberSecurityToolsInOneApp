from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QGroupBox, QWidget, QLabel, QLineEdit, \
    QHBoxLayout, QCheckBox, QScrollArea, QRadioButton

from Services import CommandExecuter
from Utils.Tools import Tools

from UI import Crunch, Dirb, Dmitry, Dnsenum, GppDecrypt, HashIdentifier, Hashcat, Hping3, JohnTheRipper, Maskprocessor, \
    Netdiscover, Nikto, Nmap, Searchploit, TheHarvester,Home

class Crunch:
    __command=[]
    __checkedRB=None
    def __init__(self):

        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setMinimumWidth(300)
        self.win.setWindowTitle("Crunch")
        self.form()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        self.createMenu()
        hbox = QVBoxLayout()
        hbox.addLayout(self.top_lvl_vBox)
        wid.setLayout(hbox)

    def showWindow(self):
        self.win.show()

    def form(self):
        self.top_lvl_vBox=QVBoxLayout()
        hbox=QHBoxLayout()


        lbl_min_length= QLabel("Minumum Length")
        self.enrty_min_length= QLineEdit(self.win)
        self.enrty_min_length.setPlaceholderText("Minumum Length")
        v1=QVBoxLayout()
        v1.addWidget(lbl_min_length)
        v1.addWidget(self.enrty_min_length)
        hbox.addLayout(v1)

        lbl_max_length= QLabel("Maximum Length")
        self.enrty_max_length= QLineEdit(self.win)
        self.enrty_max_length.setPlaceholderText("Maximum Length")
        v2=QVBoxLayout()
        v2.addWidget(lbl_max_length)
        v2.addWidget(self.enrty_max_length)
        hbox.addLayout(v2)
        g1=QGroupBox()

        g1.setStyleSheet("QGroupBox { border-style: none;}")
        g1.setLayout(hbox)
        self.top_lvl_vBox.addWidget(g1)

        outputfileLabel = QLabel("Output File Name")
        self.outputfileEdit = QLineEdit(self.win)
        self.outputfileEdit.setPlaceholderText("Output File Name")
        v3 = QVBoxLayout()
        v3.addWidget(outputfileLabel)
        v3.addWidget(self.outputfileEdit)
        gbox=QGroupBox()
        gbox.setStyleSheet("QGroupBox { border-style: none;}")

        gbox.setLayout(v3)
        self.top_lvl_vBox.addWidget(gbox)

        self.checkBox=QCheckBox("Use Charset")
        self.checkBox.toggled.connect(lambda : self.checkBoxController(self.checkBox))
        self.top_lvl_vBox.addWidget(self.checkBox)

        self.scrollArea=QScrollArea()
        self.scrollArea.setVisible(False)
        self.scrollArea.setFixedHeight(100)
        vs=QVBoxLayout()
        self.numeric = QRadioButton("numeric")
        self.numeric.setChecked(False)
        self.numeric.toggled.connect(lambda: self.radioBtnHandler(self.numeric))
        vs.addWidget(self.numeric)

        self.ualpha = QRadioButton("ualpha")
        self.ualpha.setChecked(False)
        self.ualpha.toggled.connect(lambda: self.radioBtnHandler(self.ualpha))
        vs.addWidget(self.ualpha)

        self.ualpha_numeric = QRadioButton("ualpha_numeric")
        self.ualpha_numeric.setChecked(False)
        self.ualpha_numeric.toggled.connect(lambda: self.radioBtnHandler(self.ualpha_numeric))
        vs.addWidget(self.ualpha_numeric)

        self.ualpha_numeric_all = QRadioButton("ualpha_numeric_all")
        self.ualpha_numeric_all.setChecked(False)
        self.ualpha_numeric_all.toggled.connect(lambda: self.radioBtnHandler(self.ualpha_numeric_all))
        vs.addWidget(self.ualpha_numeric_all)

        self.lalpha = QRadioButton("lalpha")
        self.lalpha.setChecked(False)
        self.lalpha.toggled.connect(lambda: self.radioBtnHandler(self.lalpha))
        vs.addWidget(self.lalpha)

        self.lalpha_numeric = QRadioButton("lalpha_numeric")
        self.lalpha_numeric.setChecked(False)
        self.lalpha_numeric.toggled.connect(lambda: self.radioBtnHandler(self.lalpha_numeric))
        vs.addWidget(self.lalpha_numeric)

        self.lalpha_numeric_all = QRadioButton("lalpha_numeric_all")
        self.lalpha_numeric_all.setChecked(False)
        self.lalpha_numeric_all.toggled.connect(lambda: self.radioBtnHandler(self.lalpha_numeric_all))
        vs.addWidget(self.lalpha_numeric_all)

        self.mixalpha = QRadioButton("mixalpha")
        self.mixalpha.setChecked(False)
        self.mixalpha.toggled.connect(lambda: self.radioBtnHandler(self.mixalpha))
        vs.addWidget(self.mixalpha)

        self.mixalpha_numeric = QRadioButton("mixalpha_numeric")
        self.mixalpha_numeric.setChecked(False)
        self.mixalpha_numeric.toggled.connect(lambda: self.radioBtnHandler(self.mixalpha_numeric))
        vs.addWidget(self.mixalpha_numeric)

        self.mixalpha_numeric_all = QRadioButton("mixalpha_numeric_all")
        self.mixalpha_numeric_all.setChecked(False)
        self.mixalpha_numeric_all.toggled.connect(lambda: self.radioBtnHandler(self.mixalpha_numeric_all))
        vs.addWidget(self.mixalpha_numeric_all)
        gboxs=QGroupBox()

        gboxs.setStyleSheet("QGroupBox { border-style: none;}")
        gboxs.setLayout(vs)
        self.scrollArea.setWidget(gboxs)
        self.top_lvl_vBox.addWidget(self.scrollArea)

        charsetLbl= QLabel("Charset")
        self.charsetEdit = QLineEdit(self.win)
        self.charsetEdit.setPlaceholderText("Charset")
        v5 = QVBoxLayout()
        v5.addWidget(charsetLbl)
        v5.addWidget(self.charsetEdit)
        self.gbox3 = QGroupBox()
        self.gbox3.setStyleSheet("QGroupBox { border-style: none;}")
        self.gbox3.setLayout(v5)
        self.gbox3.setVisible(False)
        self.top_lvl_vBox.addWidget(self.gbox3)
        vs = QHBoxLayout()

        self.create=QPushButton("Create List")
        self.create.clicked.connect(lambda:self.runButtonClick())
        self.cancel=QPushButton("Cancel")
        self.cancel.clicked.connect(lambda:self.returnHome())
        vs.addWidget(self.cancel)
        vs.addWidget(self.create)
        ngbox=QGroupBox()
        ngbox.setLayout(vs)
        ngbox.setStyleSheet("QGroupBox { border-style: none;}")
        self.top_lvl_vBox.addWidget(ngbox)

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

    def returnHome(self):
        self.ui = Home.Home()
        self.ui.createWindow()
        self.ui.showWindow()
        self.win.close()

    def runButtonClick(self):
        self.__command.append(self.enrty_min_length.text())
        self.__command.append(self.enrty_max_length.text())
        if(self.checkBox.isChecked()):
            self.__command.append("-f")
            self.__command.append("/usr/share/crunch/charset.lst")
            self.__command.append(self.__checkedRB)
        elif(not(self.checkBox.isChecked()) and self.charsetEdit!=""):
            self.__command.append(self.charsetEdit.text())
        if(self.outputfileEdit.text()!=""):
            self.__command.append("-o ")
            self.__command.append(self.outputfileEdit.text())
        print(self.__command)
        cexec=CommandExecuter("crunch",self.__command)
        cexec.run()
        result=cexec.getResult()
        print(result.stderr.decode("utf-8"))
        print(result.stdout.decode("utf-8"))
        self.__command.clear()


    def buttonClickHandler(self, text):
        self.window = QWidget()
        self.ui = None;
        if (text == Tools.CRUNCH.name):
            self.ui = Crunch()
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

    def __del__(self):
        print("asd")
        self.win.destroy()

    def radioBtnHandler(self,radiobutton):
        if(radiobutton.isChecked()):
            self.__checkedRB=radiobutton.text()

    def checkBoxController(self,checkBox):
        if (checkBox.isChecked()):
            self.scrollArea.setVisible(True)
            self.gbox3.setVisible(False)
            self.win.setMinimumHeight(350)
        else:
            self.scrollArea.setVisible(False)
            self.gbox3.setVisible(True)
            self.win.setFixedHeight(400)
