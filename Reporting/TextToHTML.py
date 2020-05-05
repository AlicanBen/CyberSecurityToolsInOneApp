from bs4 import BeautifulSoup


class TextToHTML:
    __fileName = ""
    __fileDirectory = "./../results/txts/"
    __htmlDirectory = "./../results/htmls/"
    __soup = BeautifulSoup(features="html.parser")


    def setFileName(self,fileName):
        self.__fileName=fileName

    def getFileName(self):
        return self.__fileName

    def generateHtmlFile(self):
        if(self.__fileName[-4:]!=".txt"):
            return False
        else:
            body = self.__soup.new_tag('body')
            self.__soup.insert(0, body)
            with open(self.__fileDirectory+self.__fileName) as infile:
                for lines in infile:
                    line=self.__soup.new_tag("pre")
                    line.string=lines
                    body.insert(0,line)
        with open(self.__htmlDirectory+self.__fileName[:-4]+".html", 'w') as outfile:
            outfile.write(self.__soup.prettify())
        return True




