import subprocess

class XmlToHTML:
    __fileName = ""
    __fileDirectory = "./../results/xmls/"
    __htmlDirectory = "./../results/htmls/"
    __command=["xsltproc", ""]
    def setFileName(self, fileName):
        self.__fileName = fileName
        self.__command[1]=self.__fileDirectory+fileName


    def getFileName(self):
        return self.__fileName

    def generateHtmlFile(self):
        if (self.__fileName[-4:] != ".xml"):
            return False
        else:
            result = subprocess.run(self.__command, capture_output=True)
            with open(self.__htmlDirectory+self.__fileName[:-4]+".html", 'w') as outfile:
                outfile.write(result.stdout.decode("utf-8"))
            return True
