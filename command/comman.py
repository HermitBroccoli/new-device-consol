from colorama import init
from colorama import Fore, Back, Style
from os import system, name, path

def clear():
    init()
    
    system("cls")
    print(Fore.LIGHTGREEN_EX + "———————————————————————————————————————————————————\n|Версия: 1.0                                      |\n" + 
                "|OC: Windows                                      |\n|© Broccoli                                       |" + 
                "\n———————————————————————————————————————————————————")


def ping(ip):
    if ip != "":
        system(f"ping {ip}")
    else:
        print("Некоректный адрес")    

def pip():

    system("pip")

def python():

    system(path.abspath("install/python-3.8.6-amd64.exe"))

def sstem():

    print(Fore.LIGHTCYAN_EX)
    print("Это специальный режим работы\n" + 
            "здесь используются все команды командной строки")

    while True:
        print(Fore.LIGHTCYAN_EX)
        text = input("($CMD)>")

        if text != "system exit":
            system(text)
            print("Для того чтобы выйти из супер режима пропишите команду system exit")
        elif text == "cls":
            print("Это специальный режим работы\n" + 
            "здесь используются все команды командной строки")
        else:
            print(Fore.GREEN + "———————————————————————————————————————————————————\n‖Версия: 1.0                                      ‖\n" + 
                   "‖OC: Windows                                      ‖\n‖© Broccoli                                       ‖" + 
                   "\n———————————————————————————————————————————————————")
            break