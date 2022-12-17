from compile.McFunction import McFunction

class Compiler(object):
    def __init__(self) -> None:
        self.functions:list = []

    def addFunction(self, func:McFunction) -> None:
        self.functions.append(func)
    
    def compile(self) -> None:
        while True:
            for i,f in list(enumerate(self.functions)):
                i:int
                f:McFunction
                if not f.isCompiled:
                    f.compile()
                




c = Compiler()
print(c.resolveFormula("1+(2+3)*4"))
        