class Compiler(object):
    def __init__(self) -> None:
        self.functions:list = []
    
    def compile(self) -> None:
        i:int = 0
        while i < len(self.functions):
            # Compile the function at [i]
            i+=1


c = Compiler()
print(c.resolveFormula("1+(2+3)*4"))
        