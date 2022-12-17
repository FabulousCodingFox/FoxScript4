from compile.McFunction import McFunction
import util.Logger as Logger
import util.FileUtils as FileUtils
import os, json

class Compiler(object):
    def __init__(self, pt:str) -> None:
        self.functions:list = []
        self.namespaces:list = ["foxscript"]



        self.projectPath:str = pt

        if not os.path.exist(pt):
            Logger.error("COMPILER INIT", "The path to the project does not exist")
            exit()

        if not os.path.exist(os.path.join(pt, "settings.json")):
            Logger.error("COMPILER INIT", "The path does not contain a project.json")
            exit()
        
        with open(os.path.join(pt, "settings.json")) as file:
            self.projectConfig:dict = json.load(file)

        self.targetPath:str = self.projectConfig["target-path"]

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
    
    def createFiles(self) -> None:
        Logger.log("SAVING", "Starting...")
        if not os.path.exists(self.targetPath):
            Logger.log("SAVING", "Target folder does not exist. Creating...")
            os.makedirs(self.targetPath)
        else:
            Logger.log("SAVING", "Clearing the target folder...")
            FileUtils.purgeFolder(self.targetPath)
            




c = Compiler("C:/Users/%USERNAME%/Documents/GitHub/FoxScript4/example-project/")
#print(c.resolveFormula("1+(2+3)*4"))
        