def containsAny(txt: str, chars: list[str]) -> bool:
    """
    Checks if a string contains any of the given characters
    :param txt:
    :param chars:
    :return bool:
    """
    for c in chars:
        if c in txt:
            return True
    return False


def splitPackages(txt: str, delimiters: list[str]) -> list[str]:
    level: int = 0
    index: int = 0
    mode: str = "+"
    split: list[dict] = []

    for n, c in enumerate(list(txt)):
        if c in delimiters and level == 0:
            split.append({"value": txt[index:n], "mode": mode})
            index = n
            mode = c
        elif c == "(":
            level += 1
        elif c == ")":
            level -= 1

    split.append(
        {
            "value": txt[(index + 1) if txt[index] in delimiters else index :],
            "mode": mode,
        }
    )

    return split


class StaticCountingInt:
    def __init__(self, value: int = 0):
        self.value: int = value

    def request(self):
        self.value += 1
        return self.value - 1


class CodeWrapper:
    def __init__(self):
        self.code = ""

    def __str__(self):
        return self.code

    def add(self, code: str):
        self.code += code

    def addLine(self, code: str):
        self.code += code + "\n"

    def insert(self, code: str, index: int):
        self.code = self.code[:index] + code + self.code[index:]

    def insertLine(self, code: str, index: int):
        self.code = self.code[:index] + code + "\n" + self.code[index:]


class MathPacket(object):
    def __init__(
        self,
        value: str,
        mode: str,
        top: bool,
        level: int,
        idCounter: StaticCountingInt,
        codeWrapper: CodeWrapper,
    ):
        self.value: str = value
        self.mode: str = mode
        self.top: bool = top
        self.children: list[MathPacket] = []
        self.level: int = level
        self.idCounter: StaticCountingInt = idCounter
        self.id = self.idCounter.request()
        self.result = None
        self.codeWrapper = codeWrapper

    def resolve(self):
        # If the equation has no operations, terminate resolving process and mark as a top equation
        if not containsAny(self.value, ["+", "-", "*", "/"]):
            self.top = True
            return

        # Split the equation into packages containing +- operations
        p0: list[dict] = splitPackages(self.value, ["+", "-"])
        if p0[0]["value"] == self.value:
            p1: list[dict] = splitPackages(self.value, ["*", "/"])
            if p1[0]["value"] == self.value:
                if self.value.startswith("(") and self.value.endswith(")"):
                    self.value = self.value[1:-1]
                    self.resolve()
                    return
                else:
                    self.children.append(
                        MathPacket(
                            value=p1[0]["value"],
                            mode=p1[0]["mode"],
                            top=True,
                            level=self.level + 1,
                            idCounter=self.idCounter,
                            codeWrapper=self.codeWrapper,
                        )
                    )
            else:
                for j in p1:
                    self.children.append(
                        MathPacket(
                            value=j["value"],
                            mode=j["mode"],
                            top=False,
                            level=self.level + 1,
                            idCounter=self.idCounter,
                            codeWrapper=self.codeWrapper,
                        )
                    )
        else:
            for j in p0:
                self.children.append(
                    MathPacket(
                        value=j["value"],
                        mode=j["mode"],
                        top=False,
                        level=self.level + 1,
                        idCounter=self.idCounter,
                        codeWrapper=self.codeWrapper,
                    )
                )

        for i in self.children:
            if not i.top and i.level <= 6:
                i.resolve()

    def output(self, intendation: int = 0):
        print(
            "   " * intendation, "(", self.mode, ") ", self.value, "      => ", self.id
        )
        for i in self.children:
            i.output(intendation + 1)

    def build(self):
        for child in self.children:
            if child.result == None:
                child.build()

        if self.top:
            self.codeWrapper.insertLine(
                f"scoreboard players set var{self.id} math {self.value}", 0
            )
            self.result = ""
            return

        code: str = ""

        # setup the first child
        if self.children[0].mode == "+":
            code += f"scoreboard players operation var{self.id} math = var{self.children[0].id} math\n"
        elif self.children[0].mode == "-":
            code += f"scoreboard players operation var{self.id} math = var{self.children[0].id} math\n"

        # Skip the first child
        for n, child in enumerate(self.children):
            if n <= 0:
                continue

            if child.mode == "+":
                code += f"scoreboard players operation var{self.id} math += var{child.id} math\n"
            elif child.mode == "-":
                code += f"scoreboard players operation var{self.id} math -= var{child.id} math\n"
            elif child.mode == "*":
                code += f"scoreboard players operation var{self.id} math *= var{child.id} math\n"
            elif child.mode == "/":
                code += f"scoreboard players operation var{self.id} math /= var{child.id} math\n"

        self.result = code
        self.codeWrapper.add(code)


def resolveFormula(self, formula: str) -> str:
    """
    Gives the .mcfunction equivalent of a formula
    :param formula:
    :return mcfunctionCode:
    """

    formula = formula.replace(" ", "").replace("\n", "")
    idCounter = StaticCountingInt()
    code = CodeWrapper()

    root = MathPacket(
        value = formula,
        mode = "+",
        top = False,
        level = 0,
        idCounter = idCounter,
        codeWrapper = code,
    )
    root.resolve()
    root.build()

    return code
