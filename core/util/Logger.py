from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from datetime import datetime

class Logger:
    def _prepareMessage(col:Fore, txt:str) -> str:
        currentDateAndTime = datetime.now().strftime("%H:%M:%S")
        return f"{col}[{currentDateAndTime}]: {txt}"

    def init() -> None:
        colorama_init()

    def log(txt:str) -> None:
        print(Logger._prepareMessage(Fore.WHITE, txt))
    
    def error(txt:str) -> None:
        print(Logger._prepareMessage(Fore.RED, txt))