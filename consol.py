import sys

from colorama import init
from colorama import Fore, Back, Style
from command.help import *
from command.Command import *


init()

print(Fore.GREEN + "———————————————————————————————————————————————————\n‖Версия: 1.0                                      ‖\n" + 
                   "‖OC: Windows                                      ‖\n‖©Broccoli                                        ‖" + 
                   "\n———————————————————————————————————————————————————\n")

while True:
    print(Fore.BLUE)
    command = str(input("@> "))

    if command == "help":
        help()
    elif command == "exit":
        sys.exit()
    elif command == "ping":
        ping(input("Адрес: "))
    elif command == "cls":
        clear()
    elif command == "info":
        info()
    else:
        print("no command")
