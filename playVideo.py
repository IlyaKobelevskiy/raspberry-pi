#!/usr/bin/python

# Start xterm in fullscreen mode, execute helper script in console passing it filename as an input
from subprocess import call
import sys
import fcntl 
pid_file = 'omxplayer.pid'
fp = open(pid_file, 'w')
try:
	fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
	# call(["sleep", "1"])
	# print 'Slept, finishing'
	call(["xterm", "-fn", "fixed", "-fullscreen", "-e", "omxplayer", sys.argv[1]])
except IOError:
	# another instance is running
	print 'Other instance is running, exiting...'
