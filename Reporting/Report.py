import datetime
import pathlib
import subprocess
import sys

import pdfcrowd
import pdfkit
from Utils.ReportPositions import ReportPositions
class Report:

    __files={
        ReportPositions.NETDISCOVER.name :"NETDISCOVER",
        ReportPositions.DNSENUM.name :"",
        ReportPositions.DMITRY.name :"",
        ReportPositions.DIRB.name :"",
        ReportPositions.NMAP.name :"NMAP",
        ReportPositions.NIKTO.name :"",
        ReportPositions.SEARCHPLOIT.name :"",
        ReportPositions.HASHIDENTIFIER.name :"",
        ReportPositions.JOHNTHERIPPER.name :""
    }

    def setFileName(self,filename):
        if(filename[:-4] == ReportPositions.NETDISCOVER.name):
            self.__files[ReportPositions.NETDISCOVER.name]=ReportPositions.NETDISCOVER.name

        elif(filename[:-4] == ReportPositions.DNSENUM.name):
            self.__files[ReportPositions.DNSENUM.name]=ReportPositions.DNSENUM.name

        elif(filename[:-4] == ReportPositions.DMITRY.name):
            self.__files[ReportPositions.DMITRY.name]=ReportPositions.DMITRY.name

        elif(filename[:-4] == ReportPositions.DIRB.name):
            self.__files[ReportPositions.DIRB.name]=ReportPositions.DIRB.name

        elif(filename[:-4] == ReportPositions.NMAP.name):
            self.__files[ReportPositions.NMAP.name]=ReportPositions.NMAP.name

        elif(filename[:-4] == ReportPositions.NIKTO.name):
            self.__files[ReportPositions.NIKTO.name]=ReportPositions.NIKTO.name

        elif(filename[:-4] == ReportPositions.SEARCHPLOIT.name):
            self.__files[ReportPositions.SEARCHPLOIT.name]=ReportPositions.SEARCHPLOIT.name

        elif(filename[:-4] == ReportPositions.HASHIDENTIFIER.name):
            self.__files[ReportPositions.HASHIDENTIFIER.name]=ReportPositions.HASHIDENTIFIER.name

        elif(filename[:-4] == ReportPositions.JOHNTHERIPPER.name):
            self.__files[ReportPositions.JOHNTHERIPPER.name]=ReportPositions.JOHNTHERIPPER.name

    def getFiles(self):
        return self.__files()

    def generateReport(self):
        self.createReportName()
        try:
            client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
            client.convertFileToFile('./../results/temp/concat.html', "./../results/pdfs/"+self.__pdfFileName)
        except pdfcrowd.Error as why:
            sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

            # rethrow or handle the exception
            raise

    def createReportName(self):
        self.__pdfFileName="Report"+datetime.datetime.now().strftime("_%Y%m%d%H%M%S")+".pdf"


if __name__ == '__main__':
    ns=Report()
    ns.generateReport()