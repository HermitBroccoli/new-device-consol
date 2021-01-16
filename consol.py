import sys

from colorama import init
from colorama import Fore, Back, Style
from command.help import *
from command.comman import *


print(Fore.LIGHTGREEN_EX + "———————————————————————————————————————————————————\n|Версия: 1.0                                      |\n" + 
                   "|OC: Windows                                      |\n|© Broccoli                                       |\n" + 
                   "———————————————————————————————————————————————————")         

while True:
    print(Fore.LIGHTBLUE_EX)
    command = str(input("$B> "))

    if command == "help":
        help()
    elif command == "exit":
        sys.exit()
    elif command == "ping":
        ping(input("Адрес: "))
    elif command == "cls":
        clear()
    #elif command == "info":
    #    info()
    elif command == "pip install":
        pip_install(input("name package: "))
    elif command == "system":
        sstem()
    else:
        print("no command\nчтобы посмотреть доступные команды воспользйтесь 'help'")
