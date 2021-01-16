from colorama import init
from colorama import Fore, Back, Style

init()

def help():

    print(Fore.LIGHTBLUE_EX)
    print("Команды для работы с консолью: \npython --установка python 3.8.6\npip --проверка установился pip или же нет\nсls/clear  --очищает консоль\n" + 
    "system --спецрежим в котором можно применеять обычные команды консольной строки Win|Linux\n")
