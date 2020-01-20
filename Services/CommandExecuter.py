import subprocess

from Services.HashID import HashID


class CommandExecuter:
    __result=""
    __command=[]

    def __init__(self,command,*params):
        self.__command.append(command)
        for i in range(len(params)):
            self.__command.append(params[i])

    def execute(self):
        self.__result=subprocess.run(self.__command,capture_output=True)
        return True

    def getResult(self):
        return self.__result


if __name__ == '__main__':
    test=CommandExecuter("hash-identifier","098f6bcd4621d373cade4e832627b4f6")
    result=test.execute()
    print(result)
    print("****************")
    res=test.getResult().stdout.decode("utf-8")
    if(res==""):
        print("Ne result")
    else:
        print(res)
    """  f=HashID("098f6bcd4621d373cade4e832627b4f6")
    f.exec()"""