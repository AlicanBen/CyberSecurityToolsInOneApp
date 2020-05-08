import os

from Reporting import XmlToHTML
from Reporting import TextToHTML
from bs4 import BeautifulSoup
import pathlib
import subprocess

from Utils import ReportPositions


class FileGenerator:
    __xmlToHtml= XmlToHTML()
    __txtToHtml= TextToHTML()

    def generateHtml(self, filename):

        if (filename[-4:] == ".txt"):
            self.__txtToHtml.setFileName(filename)
            return self.__txtToHtml.generateHtmlFile()
        elif (filename[-4:] == ".xml"):
            self.__xmlToHtml.setFileName(filename)
            return self.__xmlToHtml.generateHtmlFile()
        else:
            return False

    def concat(self,files):
        filesArr=[]
        str=""
        for key,value in files.items():
            if (pathlib.Path("./results/htmls/" + value + ".html").exists() == True):
                with open("./results/htmls/"+ value + ".html") as file:
                    filesArr.append(file.read())
        for f in filesArr:
            str=str+"\n"+f
        """if (pathlib.Path("./../results/temp/concat.html").exists() == False):
            pass"""
        with open("./results/temp/concat.html", 'w') as fp:
            fp.write(str)
if __name__ == '__main__':
    files=["NMAP","NETDISCOVER"]
    NSSS=FileGenerator()
    NSSS.concat(files)