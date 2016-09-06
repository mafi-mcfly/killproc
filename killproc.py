#!/usr/bin/env python

import curses, curses.ascii
import subprocess
import time

filter_string = None
process_name_start_index = 4 # beginning with the 5th word the process name starts

def get_processes(filter_str=None):
	p = subprocess.Popen("ps ax".split(" "), stdout=subprocess.PIPE)
	processes = []
	for l in p.stdout:
		processes.append(l.split(" "))

	# get rid of the table head
	processes = processes[1:]

	# get rid of empty strings in each process array
	_f = lambda x: x is not ''
	processes = [filter(_f, p) for p in processes]

	# make a tuple of process id and process name
	processes = map(lambda x: (x[0], (" ".join(x[process_name_start_index:])).strip()), processes)
	if filter_str:
		processes = filter(lambda (_id, name): filter_str in name, processes)
	return processes

def init_scr():
	scr = curses.initscr()
	height, width = scr.getmaxyx() # TODO: trim the process name nicely
	curses.noecho()
	curses.cbreak()
	return scr

def main():
	global filter_string

	scr = init_scr()
	scr.nodelay(1)
	while True:
		curses.flushinp()
		scr.erase()
		ps = get_processes(filter_string)
		for i in xrange(0, 9):
			if i == len(ps): break
			_id, name = ps[i]
			scr.insstr(i, 0, "%d %5s %s" % (i+1, _id, name))
		time.sleep(1)
		c = scr.getch()
		if c == -1:
			pass
		elif c == curses.ascii.ESC:
			break
		elif c == curses.ascii.NL:
			scr.nodelay(0)
			scr.erase()
			scr.addstr("New Filter: ")
			curses.echo()
			filter_string = scr.getstr(0, 12)
			curses.noecho()
			scr.erase()
			scr.nodelay(1)
		else:
			try:
				x = int(chr(c))
				if x > 0 and x <= 9:
					x -= 1
					if x <= len(ps):
						_id, _ = ps[x]
						cmd = ["kill", "-9", _id]
						subprocess.Popen(cmd)
			except:
				pass

	curses.endwin()
	return 0

if __name__ == '__main__':
	print "Current filter", filter_string
	print "Press ESCAPE to end."
	print "Use ENTER to enter a new filter."
	raw_input("ENTER to start.")
	main()
	# print get_processes()
	# print
	# print get_processes("killproc.py")
