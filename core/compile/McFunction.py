class McFunction:
    def __init__(self, pContent:str, pPath:str, pNamespace:str) -> None:
        self.path:str = pPath
        self.namespace:str = pNamespace
        self.rawContent:str = pContent
        self.isCompiled:bool = False
        self.compiledContent:str = ""

    def compile(pCompiler) -> None:
        pass