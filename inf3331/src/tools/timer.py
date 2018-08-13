#!/usr/bin/env python
"""
Time a command to be run in the operating system.
Writes timing results to standard output
(/usr/bin/time type of tools write to standard error,
which may be inconvenient when timings are mixed with
other kinds of output in efficiency tests).
"""
import os, sys
t0 = os.times()
cmd = ' '.join(sys.argv[1:])
os.system(cmd)
t1 = os.times()
elapsed_time = t1[4] - t0[4]
cpu_time_child = t1[2]-t0[2] + t1[3]-t0[3]
print 'cmd: %s; elapsed=%f.2 cpu=%f.2' % (cmd, elapsed_time, cpu_time_child)


          
