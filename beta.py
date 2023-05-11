from curses import wrapper
import getpass

ver = "0.1"

beta = False

def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    stdscr.addstr('Welcome to TemSSH manager, ver. 0.1\n')
    if (beta == True):
        stdscr.addstr('Beta mode enabled\n')
    else:
        stdscr.addstr('\n')
    stdscr.addstr('You can connect to other servers via this console app\n')
    stdscr.addstr('Select any host:\n')
    stdscr.addstr('\n')
    stdscr.addstr('L. Local terminal\n')
    stdscr.addstr('A. Add host\n')
    stdscr.addstr('G. Guest host connection\n')
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)