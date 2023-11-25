import lib.attconst as attconst
import lib.attmenus as menus
import sys
import time
import termios

option = sys.argv[1]

output = "	Welcome to Attendant. "

def a():
	for i in range(100):
		sys.stdout.write(str(i+1) + '%\r')
		sys.stdout.flush()
		time.sleep(0.1)
		

def b():
	pass




if option == 'a':
	a()

else:
	teststr = 'Welcome to Attendant!'
	fd = sys.stdin
	sizes = termios.tcgetwinsize(fd)
	print(sizes)
	print(teststr.center(sizes[1]))
	for option in menus.MAIN_MENU:
		print(option)
	pass