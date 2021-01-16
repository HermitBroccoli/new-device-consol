from colorama import init
from colorama import Fore, Back, Style

init()

def help():

    print(Fore.LIGHTBLUE_EX)
    print("Команды для работы с консолью: \nping --проверяет время сооединения между пунктами\nсls  --очищает консоль\n" + 
    "pip install [name_packeg] -- установка pip пакетов если есть такая возможность\nsystem --спецрежим в котором можно применеять обычные команды консольной команды Win|Linux")
