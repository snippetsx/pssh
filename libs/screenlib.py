from random import *
from os import *
import hashlib
import platform
import datetime

release_id = 2

ver = 0.1

beta = False

def clear():
    system('cls' if name == 'nt' else 'clear')


def about_page():
    print("TermSSH manager verson ", ver)
    print("Program platform: ", platform.system())
    print("Kernel version: ", platform.release())
    if (beta == True):
        print("Beta Features: enabled")
        print("Update channel: No")

    else:
        print("Update channel: Stable")
    print("Build id: ", release_id)


def end_page():
    print()
    print()
    input("Please ENTER to contninue")


def quest_page():
    print()
    print()
    print("Enter Answer: yes or no", end="")
    char = input()
    if (char == "Yes" or char == "yes"):
        return 1
    elif(char == "No" or char == "no"):
        return 2;


def start_page():
    print("Welcome to TermSSH manager, ver.", ver, end="")
    if (beta == True):
        print(" !!!Beta mode!!!")
    else:
        print()
    print("You can connect to other servers via this")
    print("Select any host:")
    print()
    #for i in range()
    print("L. Local terminal")
    print("A. Add host")