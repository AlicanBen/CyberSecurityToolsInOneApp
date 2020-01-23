import subprocess

from Services.HashID import HashID


class CommandExecuter:
    __result=None
    __command=[]
    __proccesedVal=None

    def __init__(self,command,params):
        self.__command.append(command)
        for i in range(len(params)):
            self.__command.append(params[i])

    def run(self):
        if(self.__command[0]=="hash-identifier"):
            self.hashId = HashID(self.__command[1])
            self.__result=self.hashId.exec()
            return True
        else:
            self.__result=subprocess.run(self.__command,capture_output=True)
            return True

    def Popen(self):
        if (self.__command[0] == "hash-identifier"):
            self.hashId = HashID(self.__command[1])
            self.__result=self.hashId.exec()
        else:
            self.__proccesedVal =subprocess.call(self.__command,stdout=True)
        return True

    def getResult(self):
        if(self.__proccesedVal==None and self.__result==None):
            return "No result"
        elif(self.__result==None):
            return self.__proccesedVal

        elif(self.__proccesedVal==None):
            return self.__result



if __name__ == '__main__':
    test=CommandExecuter("theHarvester", "-d", "google.com", "-l", "500", "-b", "google")
    result=test.run()
    print(result)
    print("****************")
    #test.getResult().stdout.decode("utf-8")
    print(test.getResult().stdout.decode("utf-8"))

