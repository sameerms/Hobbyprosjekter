#!/usr/bin/env python
import py4cs.Regression, sys

usage = "Usage: " + sys.argv[0] + " verify|update root-dir [ opt|nopt]" 


try:
  task = sys.argv[1]
except:
  print usage; sys.exit(1)

try:
  root = sys.argv[2]
except:
  print usage; sys.exit(1)

# options sys.argv[3] is only relevant for Diffpack applications:
try:
  mode = sys.argv[3]
except:
  mode = "opt"

if task in ('verify', 'update'):
    #v = py4cs.Regression.Verify(root=root, task=task, makemode=mode)
    # use VerifyDiffpack as this handles all simple .verify scripts
    # and also scripts requiring compilation of Diffpack applications
    v = py4cs.Regression.VerifyDiffpack(root=root, task=task, makemode=mode)
    # the constructor does it all...
else:
    print "wrong task", task
    

  
