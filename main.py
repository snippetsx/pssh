from libs import screenlib

hosts = open("hosts.ssh", "r+")
credentials = open("credentials.ssh", "r+")

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
        s = input()
        print(s, file=hosts, end="\n")
        screenlib.clear()
        screenlib.host_credentials_page()
        s = input('Enter username, e.g. "root": ')
        s1 = input('Enter password, e.g. "12345678": ')
        print(s, s1, sep="@", file=credentials, end="\n")



hosts.close()
credentials.close()