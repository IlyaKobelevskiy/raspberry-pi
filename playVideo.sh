#!/bin/bash

#Start xterm in fullscreen mode, execute helper script in console passing it filename as an input
xterm -fn fixed -fullscreen -e omxplayer "$1" -r
#xrefresh
#xterm
