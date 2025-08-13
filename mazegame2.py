# Maze game - run python3 mazegame.py
# from terminal
import curses
from time import sleep

maze = [
    [1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1],
    [1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1],
    ]

pos = [0,5]

def draw_maze(stdscr):
    stdscr.clear()
    for y, row in enumerate(maze):		# draw the maze using the maze array.
        for x, val in enumerate(row):
            if pos == [y,x]:			# position 0,5[x,y] is player
                stdscr.addnstr(y,x*2,':)', curses.color_pair(2)) # player
            elif val == 1:				# value == 1 it's a wall
                stdscr.addnstr(y,x*2,'##', curses.color_pair(1)) # wall
            elif val == 0:				# value == 0 it's a blank(path)
                stdscr.addnstr(y,x*2,'  ', curses.color_pair(3)) # path
            elif val == 2:				# value == 2 it's the finish
                stdscr.addnstr(y,x*2,'<>', curses.color_pair(4)) # goal win position
    stdscr.refresh()
    
def game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)
    
    # color, pair number, fore/back ground
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)		# Wall
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)		# player
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)		# Path
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_MAGENTA) 	# goal
    while True:
        draw_maze(stdscr)
        key = stdscr.getch()
        
        if key == curses.KEY_UP:			# UP key
            next = maze[pos[0] -1][pos[1]]	# move player up a space
            if next in [0, 2]:				# if pos y == 2 it's a wall...
                pos[0] -= 1					# put player down a space
        elif key == curses.KEY_DOWN:
            next = maze[pos[0] +1][pos[1]]
            if next in [0, 2]:
                pos[0] += 1
        elif key == curses.KEY_LEFT:
            next = maze[pos[0]][pos[1] -1]
            if next in [0, 2]:
                pos[1] -= 1
            
        elif key == curses.KEY_RIGHT:
            next = maze[pos[0]][pos[1] +1]
            if next in [0, 2]:
                pos[1] += 1
        elif key == ord('q'):
            break
        if maze[pos[0]][pos[1]] == 2:
            stdscr.clear()
            stdscr.addstr(3, 5, "!YOU ESCAPED!", curses.color_pair(4))
            stdscr.refresh()
            sleep(2)
            break
        sleep(0.1)
    
curses.wrapper(game)
