#!/usr/bin/env python

# testing the efficiency of reading 100000 (x,y) data points
# from file and writing (x,f(y)) data back to file again

# note: there may be some overhead in calling os.system;
# compare with datatrans-eff.sh, which is an identical script,
# except that it is written in Bourne shell

import os

print 'generating input file with (x,y) coordinates... (takes some time)'
cmd = os.path.join(os.environ['scripting'], 'src', 'efficiency',
                   'datatrans','xygenerator.py') \
      + ' 0:10,0.0001 'x*x' > datatrans.tmp'
os.system('python ' + cmd)
print ' '

def runtest(dir, file, description):
    print 'running', file, ' (' + description + ')'
    t0 = os.times()
    os.system(os.path.join(dir, file) + ' datatrans.tmp tmp.1')
    t1 = os.times()
    cpu = t1[3] + t1[2] - t0[3] - t0[2]
    print '....CPU time:', cpu

root = os.path.join(os.environ['scripting'], 'src', 'py', 'intro')
runtest(root, 'datatrans1.py', 'plain Python')
runtest(root, 'datatrans2.py', 'Python w/plain arrays')
runtest(root, 'datatrans3a.py', 'Python w/NumPy arrays and filetable')
runtest(root, 'datatrans3b.py', 'Python w/NumPy arrays and TableIO')
runtest(root, 'datatrans3c.py', 'Python w/NumPy arrays and split of file.read()')
runtest(root, 'datatrans3d.py', 'Python w/NumPy arrays and Scientific.IO.ArrayIO')

root = os.path.join(os.environ['scripting'], 'src', 'perl')
runtest(root, 'datatrans1.pl', 'plain Perl')

root = os.path.join(os.environ['scripting'], 'src', 'tcl')
runtest(root, 'datatrans1.tcl', 'plain Tcl')

print '\ncompiling C and C++ codes in scripting/src/misc/datatrans'
thisdir = os.getcwd()
os.chdir(os.path.join(os.environ['scripting'], 'src', 'efficiency',
                      'datatrans', 'C'))
os.system('./make.sh')
os.chdir('../C++')
os.system('./make.sh')
os.chdir(thisdir)
print ' '
root = os.path.join(os.environ['scripting'], 'src', 'efficiency',
                    'datatrans', 'C')
runtest(root, 'datatrans1.app'), 'plain C')
root = os.path.join(os.environ['scripting'], 'src', 'efficiency',
                    'datatrans', 'C++')
runtest(root, 'datatrans1.app'), 'plain C++')

# clean up:
#rm -f datatrans.tmp tmp.1 \
#  $scripting/src/misc/datatrans/C/datatrans1.app \
#  $scripting/src/misc/datatrans/C++/datatrans1.app




