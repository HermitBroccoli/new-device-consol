from colorama import init
from colorama import Fore, Back, Style
from os import system, name

def clear():
    
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
#
#def info():
#
#    print(platform)
#
def pip_install(pip):

    system(f"pip install {pip}")