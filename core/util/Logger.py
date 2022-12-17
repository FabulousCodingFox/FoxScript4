from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from datetime import datetime

def _prepareMessage(col:Fore, state:str, stage:str, txt:str) -> str:
    currentDateAndTime = datetime.now().strftime("%H:%M:%S")
    return f"{col}[{currentDateAndTime}][{state}][{stage}]: {Style.RESET_ALL}{txt}"

def init() -> None:
    colorama_init()

def log(stage:str, txt:str) -> None:
    print(Logger._prepareMessage(Fore.WHITE, "LOG", stage, txt))

def error(stage:str, txt:str) -> None:
    print(Logger._prepareMessage(Fore.RED, "ERROR", stage, txt))

def warning(stage:str, txt:str) -> None:
    print(Logger._prepareMessage(Fore.YELLOW, "WARNING", stage, txt))