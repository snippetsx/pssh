from libs import screenlib
from libs import sshconnect
import getpass

hosts = open("hosts.pssh", "r+")
credentials = open("credentials.pssh", "r+")

while (0 == 0):
    screenlib.clear()
    screenlib.start_page()
    l = 1
    for line in hosts:
        print(l, ".",  " ", line, sep="", end="")
        l += 1
    print()
    char = input()
    if(char == 'L' or char == "l"):
        screenlib.clear()
        screenlib.end()
    elif(char == 'A' or char == "a"):
        screenlib.clear()
        screenlib.new_host_page()
        host = input()
        print(host, file=hosts, end="\n")
        screenlib.clear()
        screenlib.host_credentials_page()
        user = input('Enter username, e.g. "user": ')
        pss = getpass.getpass('Enter password, e.g. "12345678": ')
        print(user, pss, sep="@", file=credentials, end="\n")
    elif(char == 'G' or char == 'g'):
        screenlib.clear()
        screenlib.guest_connection_host()
        host = input()
        screenlib.guest_connection_credentials()
        user = input('Enter username, e.g. "user": ')
        pss = getpass.getpass('Enter password, e.g. "12345678": ')
        ssh 





hosts.close()
credentials.close()