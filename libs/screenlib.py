from os import *
import platform
import datetime

lines = 1

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


def end():
    print("Connecting...")
    print()
    clear()
    print("Local Terminal opened")
    exit()


def quest_page():
    print()
    print()
    print("Enter Answer: yes or no", end="")
    char = input()
    if (char == "Yes" or char == "yes"):
        return 1
    elif(char == "No" or char == "no"):
        return 2


def start_page():
    print("Welcome to TermSSH manager, ver.", ver, end="")
    if (beta == True):
        print(" !!!Beta mode!!!")
    else:
        print()
    print("You can connect to other servers via this console app")
    print("Select any host:")
    print()
    for i in range(1, lines):
        print(i, ".", " ", sep="", end="")
        host.readline(i) 
    print("L. Local terminal")
    print("A. Add host")

def new_host_page():
    print("Enter IP, or domain name of the server")
    print()
    print()

def host_credentials_page():
    print("Enter valid username and password")
    print()
    print()

if __name__ == '__main__':
     print("Error: You trying to run lib")