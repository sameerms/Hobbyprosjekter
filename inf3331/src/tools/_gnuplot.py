#!/usr/bin/env python
# solution to exercise \ref{intro:python:exer8b4}

"""
Cross-platform handling of Gnuplot. The script accepts the
same command-line arguments as on Unix systems, but on
Windows the scriptfile (if present) is renamed to GNUPLOT.INI
and gnuplot is run without arguments.
"""

import sys, os

if sys.platform.startswidth('win'):
    # parse the command-line; it's easy since we drop all X11 options and
    # only need to grab the scriptfile name, and it's the last argument:
    scriptfile = sys.argv[-1]
    if os.path.isfile("GNUPLOT.INI"):
        os.remove("GNUPLOT.INI")
    os.rename(scriptfile, "GNUPLOT.INI")
    os.system("gnuplot")
elif os.name == "posix":
    os.system("gnuplot " + " ".join(sys.argv[1:]))
else:
    print "Platform", sys.platform, " on OS", os.name, "is not supported"
    sys.exit(1)
