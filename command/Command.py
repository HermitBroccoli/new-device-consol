from colorama import init
from colorama import Fore, Back, Style
from os import system, name

def clear():
    init()
    if name == "nt":
        system("cls")
        print(Fore.GREEN + "———————————————————————————————————————————————————\n‖Версия: 1.0                                      ‖\n" + 
                   "‖OC: Windows                                      ‖\n‖© Broccoli                                       ‖" + 
                   "\n———————————————————————————————————————————————————")


def ping(ip):
    if ip != "":
        system(f"ping {ip}")
    else:
        print("Некоректный адрес")    

def pip_install(pip):

    system(f"pip install {pip}")

def sstem():

    init()
    while True:

        text = input(Fore.CYAN + "($CMD)>")

        if text != "system exit":
            system(text)
            print("Для того чтобы выйти из супер режима пропишите команду system exit")
        else:
            print(Fore.GREEN + "———————————————————————————————————————————————————\n‖Версия: 1.0                                      ‖\n" + 
                   "‖OC: Windows                                      ‖\n‖© Broccoli                                       ‖" + 
                   "\n———————————————————————————————————————————————————")
            break