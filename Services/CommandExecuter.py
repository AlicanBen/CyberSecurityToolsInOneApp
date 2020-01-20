import subprocess


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
    test=CommandExecuter("crunch","4", "4", "0123456789abcdef", "-o", "4chars.txt")
    result=test.execute()
    print(result)
    print("****************")
    res=test.getResult().stdout.decode("utf-8")
    if(res==""):
        print("Ne result")
    else:
        print("asd")
        print(res)
