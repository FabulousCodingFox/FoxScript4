from compile.McFunction import McFunction
from util.Logger import Logger
import os

class Compiler(object):
    def __init__(self, pt:str) -> None:
        self.functions:list = []
        self.projectPath:str = pt

        #Check if the project exists

        if not os.path.exist(pt):
            Logger.error("COMPILER INIT", "The path to the project does not exist")
            exit()

        if not os.path.exist(os.path.join(pt, "settings.json")):
            Logger.error("COMPILER INIT", "The path does not contain a project.json")
            exit()

    def addFunction(self, func:McFunction) -> None:
        self.functions.append(func)
    
    def compile(self) -> bool:

        while True:
            c = True
            for i,f in list(enumerate(self.functions)):
                i:int
                f:McFunction
                if not f.isCompiled:
                    c = False
                    f.compile(self)
            if c: break
            
c = Compiler("C:/Users/%USERNAME%/Documents/GitHub/FoxScript4/example-project/")
#print(c.resolveFormula("1+(2+3)*4"))
        