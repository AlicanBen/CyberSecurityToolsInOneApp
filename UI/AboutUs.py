import qtawesome as qtawesome
from PyQt5 import QtSvg, Qt, QtCore
from PyQt5.QtCore import QRect, QUrl
from PyQt5.QtGui import QPixmap, QPainter, QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QGroupBox, QWidget, QLabel, QLineEdit, \
    QHBoxLayout, QCheckBox, QScrollArea, QRadioButton, QDesktopWidget, QGridLayout, QTextBrowser
from qtpy.QtGui import QDesktopServices

from Reporting import Report
from Services import CommandExecuter
from Utils.Tools import Tools

from UI import Crunch, Dirb, Dmitry, Dnsenum, GppDecrypt, HashIdentifier, Hashcat, Hping3, JohnTheRipper, Maskprocessor, \
    Netdiscover, Nikto, Nmap, Searchploit, TheHarvester, Home, AboutUs


class AboutUs:
    __command=[]
    __checkedRB=None
    def __init__(self):

        super().__init__()

    def createWindow(self):
        self.win = QMainWindow()
        self.win.setFixedWidth(700)
        self.win.setFixedHeight(500)
        self.win.setWindowTitle("About Us")
        self.center(self.win)
        self.form()
        wid = QWidget(self.win)
        self.win.setCentralWidget(wid)
        wid.setLayout(self.hBox)
        self.createMenu()

    def center(self,data):
        frameGm = data.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        data.move(frameGm.topLeft())
    def showWindow(self):
        self.win.show()

    def form(self):
        self.hBox = QHBoxLayout()
        self.leftSide()
        self.rightSide()
        self.hBox.addWidget(self.leftBox)
        self.hBox.addWidget(self.rightBox)

    def link(self, linkStr):

        QDesktopServices.openUrl(QUrl(linkStr))
    def leftSide(self):
        self.leftBox = QGroupBox()
        self.leftBox.setMinimumWidth(250)

        vLayout = QGridLayout()

        self.leftBox.setStyleSheet("QGroupBox { border-style: none;}")

        b=QLabel()
        b.setFixedWidth(30)
        svg=QSvgWidget("assets/engineerBlack.svg")
        hl=QHBoxLayout()
        hl.addWidget(svg)
        hl.setGeometry(QRect(0,0,190,190))
        box=QGroupBox()
        box.setStyleSheet("QGroupBox { border-style: none;}")
        box.setLayout(hl)
        box.setFixedWidth(190)
        box.setFixedHeight(190)
        vLayout.addWidget(b, 0, 0)
        vLayout.addWidget(b, 0, 2)
        vLayout.addWidget(box, 0, 1)
        vLayout.addWidget(b, 1, 0)
        vLayout.addWidget(b, 1, 2)
        vLayout.addWidget(b, 2, 0)
        vLayout.addWidget(b, 2, 2)
        vLayout.addWidget(b, 3, 0)
        vLayout.addWidget(b, 3, 2)
        designer=QLabel("Designer : Ali Can BEN")
        designer.setStyleSheet("QLabel{font-size:15px;}")
        designer.setFixedHeight(40)
        vLayout.addWidget(designer,1,1)
        github=QLabel()
        github.setText('<a href="https://github.com/AlicanBen" style="font-size:15px;text-align: center;'
                       'text-decoration:none; color:black"><img src="assets/github_square.svg" height="25" width="25"/>'
                       '  Ali Can BEN</a>')
        github.linkActivated.connect(self.link)
        github.setFixedHeight(30)
        vLayout.addWidget(github,2,1)
        linkedin=QLabel()
        linkedin.setText('<a href="https://www.linkedin.com/in/ali-can-ben-22929b151/" style="font-size:15px;'
                         'text-align: center; text-decoration:none; color:black"><img src="assets/linkedin.svg" '
                         'height="25" width="25"/>  Ali Can BEN</a>')
        linkedin.linkActivated.connect(self.link)
        linkedin.setFixedHeight(30)
        vLayout.addWidget(linkedin,3,1)
        self.leftBox.setLayout(vLayout)


    def rightSide(self):
        self.rightBox = QGroupBox()
        self.rightBox.setMinimumWidth(300)
        self.rightBox.setObjectName("ColoredGroupBox")
        self.rightBox.setStyleSheet("QGroupBox#ColoredGroupBox { border: 1px solid black;}")
        self.rightBox.setTitle("GNU General Public Licance")
        vLayout = QVBoxLayout()
        lbl=QLabel()
        lbl.setFixedWidth(250)
        lbl.setText('ToolPack Version 1.1.12\n\nThis program is free software; you can redistribute it and/or modify it '
                    'under the terms of the GNU General Public License as published by the Free Software Foundation;'
                    ' either version 2 of the License, or (at your option) any later version.\n\nThis program is '
                    'distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the '
                    'implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General '
                    'Public License for more details.\n\n You should have received a copy of the GNU General Public '
                    'License along with this program; if not, write an e-mail to')
        lbl.setWordWrap(True)

        vLayout.addWidget(lbl)
        mail=QLabel()
        mail.setText(u'<a href='"'https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=alican.ben.97@gmail.com'"''
                     'style="''text-align: center; text-decoration:none; color:black">Ali Can BEN</a>')
        mail.setOpenExternalLinks(True)
        mail.setFixedHeight(30)
        vLayout.addWidget(mail)
        self.rightBox.setLayout(vLayout)

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

        report = bar.addMenu("Reporting")

        self.createReport=report.addAction("Create")
        self.createReport.triggered.connect(lambda: self.creatingReport())

        self.actionAboutUs = bar.addAction("About Us")
        self.actionAboutUs.triggered.connect(lambda: self.buttonClickHandler(self.actionAboutUs.text()))

    def creatingReport(self):
        r=Report()
        r.generateReport()

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
            self.ui = Home.Home()
        elif (text == "About Us"):
            self.ui = AboutUs()
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
