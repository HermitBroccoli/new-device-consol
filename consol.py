import sys

from colorama import init
from colorama import Fore, Back, Style
from command.help import *
from command.comman import *

print(Fore.LIGHTGREEN_EX + "———————————————————————————————————————————————————\n|Версия: 1.0                                      |\n" + 
                   "|OC: Windows                                      |\n|© Broccoli                                       |\n" + 
                   "———————————————————————————————————————————————————")         

print
help()

while True:
    command = input(Fore.LIGHTBLUE_EX + "$B> ")

    if command == "python":
        python()
    if command == "pip":
        pip()
    elif (command == "cls") or (command == "clear"):
        clear()
    elif command == "system":
        sstem()
    elif command == "help":
        help()
    else:
        print("no command\nчтобы посмотреть доступные команды воспользйтесь 'help'")
