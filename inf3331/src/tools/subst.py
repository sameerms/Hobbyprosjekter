#!/usr/bin/env python
import os, re, sys, shutil

def usage():
    print 'Usage:'
    print 'subst.py [-s] pattern replacement file1 file2 *.h ...'
    print 'subst.py --restore file1.old~ file2.old~ *.h.old~'
    sys.exit(1)

def subst(pattern, replacement, files, dotall=0):
    if isinstance(files, str):
        files = [files]  # convert single filename to list
    return_str = ''
    for file in files:
        if not os.path.isfile(file):
            print '%s is not a file!' % file;  continue
        shutil.copy2(file, file+'.old~')  # back up file
        f = open(file, 'r');
        filestr = f.read()
        f.close()
        if dotall:
            cp = re.compile(pattern, re.DOTALL)
        else:
            cp = re.compile(pattern)
        if cp.search(filestr):
            filestr = cp.sub(replacement, filestr)
            f = open(file, 'w')
            f.write(filestr)
            f.close()
            if not return_str:  # initialize return_str:
                return_str = pattern + ' replaced by ' + \
                             replacement + ' in'
            return_str += ' ' + file
    return return_str


if __name__ == '__main__':
    if len(sys.argv) < 3: usage()
    from getopt import getopt
    optlist, args = getopt(sys.argv[1:], 's', 'restore')
    restore = False; dotall = False
    for opt, value in optlist:
        if opt in ('-s',):
            dotall = True
        if opt in ('--restore',):
            restore = True

    if restore:
        for oldfile in args:
            newfile = re.sub(r'\.old~$', '', oldfile)
            if not os.path.isfile(oldfile):
                print '%s is not a file!' % oldfile; continue
            os.rename(oldfile, newfile)
            print 'restoring %s as %s' % (oldfile,newfile)
    else:
        pattern = args[0]; replacement = args[1]
        s = subst(pattern, replacement, args[2:], dotall)
        print s  # print info about substitutions
