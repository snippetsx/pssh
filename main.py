from libs import screenlib

hosts = open("hosts.ssh", "r+")

while (0 == 0):
    screenlib.clear()
    screenlib.start_page()
    l = 1;
    for line in hosts:
        print(l, ".",  " ", line, sep="", end="")
        l += 1
    print()
    char = input()
    if(char == 'L' or char == "l"):
        screenlib.clear()
        screenlib.end()
    #elif(char == 'A' or char == "a"):
        