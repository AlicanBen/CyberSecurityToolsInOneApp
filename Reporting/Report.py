import datetime
import sys

import pdfcrowd

from Utils import FileGenerator
from Utils.ReportPositions import ReportPositions
class Report:
    __fileGenerator=FileGenerator()
    __files={
        ReportPositions.NETDISCOVER.name :"",
        ReportPositions.DNSENUM.name :"",
        ReportPositions.DMITRY.name :"",
        ReportPositions.DIRB.name :"",
        ReportPositions.NMAP.name :"",
        ReportPositions.NIKTO.name :"",
        ReportPositions.SEARCHPLOIT.name :"",
        ReportPositions.HASHIDENTIFIER.name :"",
        ReportPositions.JOHNTHERIPPER.name :""
    }

    def setFileName(self,filename):
        if(filename == ReportPositions.NETDISCOVER.name):
            self.__files[ReportPositions.NETDISCOVER.name]=ReportPositions.NETDISCOVER.name

        elif(filename == ReportPositions.DNSENUM.name):
            self.__files[ReportPositions.DNSENUM.name]=ReportPositions.DNSENUM.name

        elif(filename == ReportPositions.DMITRY.name):
            self.__files[ReportPositions.DMITRY.name]=ReportPositions.DMITRY.name

        elif(filename == ReportPositions.DIRB.name):
            self.__files[ReportPositions.DIRB.name]=ReportPositions.DIRB.name

        elif(filename == ReportPositions.NMAP.name):
            self.__files[ReportPositions.NMAP.name]=ReportPositions.NMAP.name

        elif(filename == ReportPositions.NIKTO.name):
            self.__files[ReportPositions.NIKTO.name]=ReportPositions.NIKTO.name

        elif(filename == ReportPositions.SEARCHPLOIT.name):
            self.__files[ReportPositions.SEARCHPLOIT.name]=ReportPositions.SEARCHPLOIT.name

        elif(filename == ReportPositions.HASHIDENTIFIER.name):
            self.__files[ReportPositions.HASHIDENTIFIER.name]=ReportPositions.HASHIDENTIFIER.name

        elif(filename == ReportPositions.JOHNTHERIPPER.name):
            self.__files[ReportPositions.JOHNTHERIPPER.name]=ReportPositions.JOHNTHERIPPER.name

    def getFiles(self):
        return self.__files

    def generateReport(self):
        print(self.__files)
        count=0
        for key,value in self.__files.items():
            if(value!=""):
                count+=1
        if(count==0):
            return
        self.__fileGenerator.concat(self.__files)
        self.createReportName()
        try:
            client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
            output_stream = open( "./results/pdfs/"+self.__pdfFileName, 'wb')
            client.convertFileToStream('./results/temp/concat.html', output_stream)
            output_stream.close()
        except pdfcrowd.Error as why:
            sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
            raise

    def createReportName(self):
        self.__pdfFileName="Report"+datetime.datetime.now().strftime("_%Y%m%d%H%M%S")+".pdf"

