from colorama import init
from colorama import Fore, Back, Style

init()

def help():

    print(Fore.GREEN)
    print("Команды для работы с консолью: \nping --проверяет время сооединения между пунктами\nсls  --очищает консоль\n" + 
    "pip install [name_packeg] -- установка pip пакетов если есть такая возможность")
