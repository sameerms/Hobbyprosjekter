#!/usr/bin/env python
"""Tool for examining diferences of float data in regression tests."""
import py4cs.Regression
import Tkinter, sys
root = Tkinter.Tk()
#Pmw.initialise(root, fontScheme='pmw1')
root.title('intelligent float diff')

if len(sys.argv) == 3:
    fd = py4cs.Regression.FloatDiff(root, sys.argv[1], sys.argv[2])
    if fd.GUI:
        root.mainloop()
else:
    print "Usage: floatdiff.py file.vd file.rd"
    
