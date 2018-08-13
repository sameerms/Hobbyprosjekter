#!/usr/bin/env python
import sys, math       # load system and math module
r = float(sys.argv[1]) # extract the 1st command-line arg.
s = math.sin(r)
print "Hello, World! sin(" + str(r) + ")=" + str(s)
