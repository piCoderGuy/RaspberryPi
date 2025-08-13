
import curses
stdscr = curses.initscr()
from time import sleep

maze = [
    [1,1,1],
    [0,0,0],
    [1,1,1]
    ]
def draw_maze(stdscr):
    stdscr.clear
    for y, row in enumerate(maze):
        for x, val in enumerate(row):
            if val ==1:
                stdscr.addnstr(y,x*2,'()', curses.color_pair(2))
            elif val ==0:
                stdscr.addnstr(y,x*2,'  ', curses.color_pair(1))
    stdscr.refresh()
    
def game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)
    #curses.start_color()
    #curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)		# Wall
    #curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)		# player
    #curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)		# Path
    #curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_MAGENTA) 	# goal
    
    while True:
        draw_maze(stdscr)
        
        sleep(1)
    
curses.wrapper(game)
