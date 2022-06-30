import curses
from curses import wrapper



def main(stdscr):
    stdscr.clear()
    stdscr.addstr("maketoolkit")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)