from PyQt5.QtWidgets import QMainWindow, QGridLayout, QPushButton, QVBoxLayout, QGroupBox, QWidget, QLabel, QLineEdit, \
    QHBoxLayout, QCheckBox, QScrollArea, QRadioButton
from Utils.Tools import Tools


class Crunch:

    def __init__(self):

        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setGeometry(50, 50, 680, 557)
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
        g1.setLayout(hbox)
        self.top_lvl_vBox.addWidget(g1)

        outputfileLabel = QLabel("Output File Name")
        self.outputfileEdit = QLineEdit(self.win)
        self.outputfileEdit.setPlaceholderText("Output File Name")
        v3 = QVBoxLayout()
        v3.addWidget(outputfileLabel)
        v3.addWidget(self.outputfileEdit)
        gbox=QGroupBox()
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
        self.numeric.toggled.connect(lambda: self.btnstate(self.b1))
        vs.addWidget(self.numeric)

        self.ualpha = QRadioButton("ualpha")
        self.ualpha.setChecked(False)
        self.ualpha.toggled.connect(lambda: self.btnstate(self.b1))
        vs.addWidget(self.ualpha)

        self.ualpha_numeric = QRadioButton("ualpha_numeric")
        self.ualpha_numeric.setChecked(False)
        self.ualpha_numeric.toggled.connect(lambda: self.btnstate(self.b1))
        vs.addWidget(self.ualpha_numeric)

        self.ualpha_numeric_all = QRadioButton("ualpha_numeric_all")
        self.ualpha_numeric_all.setChecked(False)
        self.ualpha_numeric_all.toggled.connect(lambda: self.btnstate(self.b1))
        vs.addWidget(self.ualpha_numeric_all)

        self.lalpha = QRadioButton("lalpha")
        self.lalpha.setChecked(False)
        self.lalpha.toggled.connect(lambda: self.btnstate(self.b1))
        vs.addWidget(self.lalpha)

        self.lalpha_numeric = QRadioButton("lalpha_numeric")
        self.lalpha_numeric.setChecked(False)
        self.lalpha_numeric.toggled.connect(lambda: self.btnstate(self.b1))
        vs.addWidget(self.lalpha_numeric)

        self.lalpha_numeric_all = QRadioButton("lalpha_numeric_all")
        self.lalpha_numeric_all.setChecked(False)
        self.lalpha_numeric_all.toggled.connect(lambda: self.btnstate(self.b1))
        vs.addWidget(self.lalpha_numeric_all)

        self.mixalpha = QRadioButton("mixalpha")
        self.mixalpha.setChecked(False)
        self.mixalpha.toggled.connect(lambda: self.btnstate(self.b1))
        vs.addWidget(self.mixalpha)

        self.mixalpha_numeric = QRadioButton("mixalpha_numeric")
        self.mixalpha_numeric.setChecked(False)
        self.mixalpha_numeric.toggled.connect(lambda: self.btnstate(self.b1))
        vs.addWidget(self.mixalpha_numeric)

        self.mixalpha_numeric_all = QRadioButton("mixalpha_numeric_all")
        self.mixalpha_numeric_all.setChecked(False)
        self.mixalpha_numeric_all.toggled.connect(lambda: self.btnstate(self.b1))
        vs.addWidget(self.mixalpha_numeric_all)
        gboxs=QGroupBox()
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
        self.gbox3.setLayout(v5)
        self.gbox3.setVisible(False)
        self.top_lvl_vBox.addWidget(self.gbox3)

        self.button=QPushButton("Create List")
        self.top_lvl_vBox.addWidget(self.button)

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

    def checkBoxController(self,checkBox):
        if (checkBox.isChecked()):
            self.scrollArea.setVisible(True)
            self.gbox3.setVisible(False)
        else:
            self.scrollArea.setVisible(False)
            self.gbox3.setVisible(True)


