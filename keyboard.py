import curses

stdscr = None

def init():
	global stdscr
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(1)

def close():
	global stdscr
	curses.nocbreak()
	stdscr.keypad(0)
	curses.echo()
	curses.endwin()

init()

while 1:
	c = stdscr.getch()
	if c == curses.KEY_UP:
		stdscr.addstr(0, 0, "UP   ")
	if c == curses.KEY_DOWN:
		stdscr.addstr(0, 0, "DOWN ")
	if c == curses.KEY_LEFT:
		stdscr.addstr(0, 0, "LEFT ")
	if c == curses.KEY_RIGHT:
		stdscr.addstr(0, 0, "RIGHT")

	if c == ord('q'):
		break;

close()
