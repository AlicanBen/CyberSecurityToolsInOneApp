import os
import pathlib

from bs4 import BeautifulSoup


class TextToHTML:
    __fileName = ""
    __fileDirectory = "./results/txts/"
    __htmlDirectory = "./results/htmls/"
    __absoluteHtmlDirectory = "/root/Masaüstü/Project/results/htmls/"
    __soup = BeautifulSoup(features="html.parser")


    def setFileName(self,fileName):
        self.__fileName=fileName

    def getFileName(self):
        return self.__fileName

    def generateHtmlFile(self):
        if(self.__fileName[-4:]!=".txt"):
            return False
        else:
            if(pathlib.Path(self.__absoluteHtmlDirectory+self.__fileName[:-4]+".html").exists()==True):
                os.remove(self.__absoluteHtmlDirectory+self.__fileName[:-4]+".html")
                self.__soup.clear()
            body = self.__soup.new_tag('body')
            self.__soup.insert(0, body)
            with open(self.__fileDirectory+self.__fileName) as infile:
                i=0
                for lines in infile:
                    line=self.__soup.new_tag("pre")
                    line.string=lines
                    body.insert(i,line)
                    i+=1
        with open(self.__htmlDirectory+self.__fileName[:-4]+".html", 'w') as outfile:
            outfile.write(self.__soup.prettify())
        return True




