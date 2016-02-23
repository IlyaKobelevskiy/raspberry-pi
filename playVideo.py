#!/usr/bin/python

# Start xterm in fullscreen mode, execute helper script in console passing it filename as an input
from subprocess import call
import sys
import fcntl
import os
import re
import time
sys.stdout = open("/home/pi/playVideo.out", "a")
pid_file = 'omxplayer.pid'
fp = open(pid_file, 'w')
print "argc = " + str(len(sys.argv))
for idx, fname in enumerate(sys.argv):
        print idx, fname
        if idx == 0:
                print "Skipping program name"
                continue
        loop_condition = True
        while loop_condition:
                try:
                        fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
                        srt_file = ''
                        srt_pattern = re.compile('.srt')
                        dirname = os.path.dirname(sys.argv[1])
                        for filename in os.listdir(dirname):
                                if srt_pattern.search(filename):
                                        srt_file = dirname + "/" + filename
                                        break
                        if not srt_file:
                                call(["xterm", "-fn", "fixed", "-fg", "black", "-fullscreen", "-e", "omxplayer.sh", fname, "-rb"])
                                call(["xterm", "-fn", "fixed", "-fullscreen", "-e", "omxplayer", "-r"]);
                                print 'no subtitle'
                        else:
                                call(["xterm", "-fn", "fixed", "-fg", "black", "-fullscreen", "-e", "omxplayer.sh", fname, "--subtitle", srt_file, "-rb"])
                                call(["xterm", "-fn", "fixed", "-fullscreen", "-e", "omxplayer", "-r"]);
                                print 'found subtitle:'+srt_file
                        os.remove('omxplayer.pid')
                        loop_condition = False
                except IOError:
                        # another instance is running
                        print 'Other instance is running, waiting...'
                        time.sleep(0.5)
print "Done"
