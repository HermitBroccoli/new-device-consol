from os import system, name
from sys import *

def clear():
    
    if name == "nt":
        system("cls")

def ping(ip):

    try:
        system(f"ping {ip}")
    except:
        print("не указан адрес")

def info():

    print(platform)
