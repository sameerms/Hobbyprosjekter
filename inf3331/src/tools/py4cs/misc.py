"""
A collection of Python utilities developed for the
"Python for Scientific Computing" book.
"""

import time, sys, os, re, getopt, math, threading, shutil
from FuncDependenceViz import *


def dump(obj, hide_nonpublic=True):
    """
    Inspect an object obj by the dir function.
    This function first prints the repr(obj) of the object,
    then all data attributes and their values are
    listed, and finally a line listing all functions/methods
    is printed.
    """
    print repr(obj)
    try:  # dump class name if it exists
        print 'object of class', obj.__class__.__name__
    except:
        pass
    try:
        print 'object with name', obj.__name__
    except:
        pass
    methods = [];  attrs = []
    for a in dir(obj):
        if a.startswith('_') and hide_nonpublic:
            pass
        else:
            try:
                s = a + '=' + str(getattr(obj,a))
                if s.find(' method ') != -1 or \
                   s.find('function ') != -1 or \
                   s.find('ufunc ') != -1:
                    methods.append(a) # skip function addresses
                else:
                    attrs.append(s)  # variable=value
            except:
                pass
    print 'attributes:', ', '.join(attrs)
    print 'methods:', ', '.join(methods)


def str2obj(s):
    """
    Turn string s into the corresponding object.
    eval(s) normally does this, but if s is just a string ready
    from file, GUI or the command-line, eval will not work when
    s really represents a string:
    >>> eval('some string')
    Traceback (most recent call last):
    SyntaxError: unexpected EOF while parsing
    It tries to parse 'some string' as Python code.

    In this function we try to eval(s), and if it works, we
    return that object. If it does not work, s probably has
    meaning as just a string, and we return just s.

    You can safely apply eval on the output of this function.

    >>> from py4cs.misc import str2obj
    >>> s = str2obj('0.3')
    >>> s, type(s)
    0.3 <type 'float'>
    >>> s = str2obj('3')
    >>> s, type(s)
    3 <type 'int'>
    >>> s = str2obj('(1,8)')
    >>> s, type(s)
    (1, 8) <type 'tuple'>
    >>> s = str2obj('some string')
    'some string' <type 'str'>
    """
    try:
        s = eval(s, locals())  # y gets the right type
        return se
    except:
        # x is a string, return repr(x) so it gets quotes:
        return s
    

def before(str, character):   
    """Return part of str before character."""
    for i in range(len(str)):
        if c == character:
            return str[:i-1]

def after(str, character):
    """Return part of str after character."""
    for i in range(len(str)):
        if c == character:
            return str[i+1:]

def find(func, rootdir, arg=None):
    """
    Traverse the directory tree rootdir and call func for each file.
    arg is a user-provided argument transferred to func(filename,arg).
    """
    files = os.listdir(rootdir)  # get all files in rootdir
    files.sort(lambda a,b: cmp(a.lower(),b.lower()))
    for file in files:
        filepath = os.path.join(rootdir,file) # make complete path
        if os.path.islink(filepath):
            pass # drop links...
        elif os.path.isdir(filepath):
            find(func, filepath, arg) # recurse into directory
        elif os.path.isfile(filepath):
            func(filepath, arg) # file is regular, apply func
        else:
            print 'find: cannot treat ',filepath

class Command:
    """Alternative to lambda functions."""

    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        args = args + self.args
        kwargs.update(self.kwargs)  # override kw with orig self.kw
        #apply(self.func, args, kwargs)  # old style
        self.func(*args, **kwargs)

def timer(func, args=[], kwargs={}, repetitions=10, comment=''):
    """
    Run a function func, with arguments given by the tuple
    args and keyword arguments given by the dictionary kwargs,
    a specified number of times (repetitions) and
    write out the elapsed and CPU times together.
    """
    t0 = time.time();  c0 = time.clock()
    for i in range(repetitions):
        func(*args, **kwargs)
    cpu_time = time.clock()-c0
    elapsed_time = time.time()-t0
    try:    # instance method?
        name = func.im_class.__name__ + '.' + func.__name__
    except: # ordinary function
        try:
            name = func.__name__
        except:
            name = ''
    print '%s %s (%d calls): elapsed=%g, CPU=%g' % \
          (comment, name, repetitions, elapsed_time, cpu_time)
    return cpu_time/float(repetitions)


def timer_system(command, comment=''):
    """
    Run an os.system(command) statement and measure the CPU time.
    With os.system, the CPU time is registered as the user and
    system time of child processes.
    """
    t0 = os.times()
    failure = os.system(command)
    t1 = os.times()
    # some programs return nonzero even when they work (grep, for inst.)
    if failure:
        print 'Note: os.system(%s) failed' % command, 'returned', failure
    cpu_time = t1[2]-t0[2] + t1[3]-t0[3]
    print '%s system command: "%s": elapsed=%g CPU=%g' % \
          (comment, command, t1[4]-t0[4], cpu_time)
    return cpu_time


def findprograms(programs, searchlibs=[], write_message=0):
    """
    Given a list of programs (programs), find the full path
    of each program and return a dictionary with the program
    name as key and the full path as value. The value is None
    if the program is not found.
    The program list can either be a list/tuple or a
    dictionary (in the latter case, the keys are the programs
    and the values are explanations of the programs).
    If write_message is true, the function writes a message
    if a program is not found. In that case, None is returned
    if not all programs are found.

    Example on usage:
    if findprograms(['plotmtv'], write_message=1):
        os.system('plotmtv ...')

    programs = ['gs', 'convert']
    path = findprograms(programs)
    if path['gs']:
        os.system('gs ...')
    if path['convert']:
        os.system('convert ...')

    programs = { 'gs' : 'Ghostscript: file format conversions',
                 'convert' : 'File format conversion from ImageMagick',
               }
    if not findprograms(programs, write_message=1):
        print 'the mentioned programs need to be installed'
        sys.exit(1)
    """
    def program_exists(fullpath):
        if sys.platform.startswith('win'):
            # add .exe or .bat to program filename:
            if os.path.isfile(fullpath+'.exe') or \
               os.path.isfile(fullpath+'.bat'):
                return True
        elif os.name == 'posix': # Unix
            if os.path.isfile(fullpath):
                return True
        else:
            raise TypeError, \
                  'platform %s/%s not supported' % \
                  (sys.platform, os.name)
        return False # otherwise
        
    path = os.environ['PATH']  # /usr/bin:/usr/local/bin:/usr/X11/bin
    paths = re.split(os.pathsep, path)
    fullpaths = {}
    if isinstance(programs, (list,tuple)):
        # initialize with None:
        for program in programs:  fullpaths[program] = None
        for program in programs:
            for dir in paths:
                if os.path.isdir(dir): # skip non-existing directories
                    fullpath = os.path.join(dir,program)
                    if program_exists(fullpath):
                        fullpaths[program] = fullpath
                        break  # stop when the program is found

    elif isinstance(programs, dict):
        # initialize with None:
        for program in programs.keys():  fullpaths[program] = None
        for program in programs.keys():
            for dir in paths:
                if os.path.isdir(dir): # skip non-existing directories
                    fullpath = os.path.join(dir,program)
                    if program_exists(fullpath):
                        fullpaths[program] = fullpath
                        break
        
    if write_message:
        missing = 0
        for program in fullpaths.keys():
            if not fullpaths[program]:
                if isinstance(program, dict):
                    print "program '%s' (%s) not found" % \
                          (program,programs[program])
                else:  # list or tuple
                    print 'program "%s" not found' % program
                missing = 1
        if missing:
            return None
        
    return fullpaths


def pathsearch(programs=[], modules=[], where=0):
    """
    Given a list of programs (programs) and modules (modules),
    search for these programs and modules in the directories
    in the PATH and PYTHONPATH environment variables, respectively.
    Check that each directory has read and write access too.
    The function is useful for checking that PATH and PYTHONPATH
    are appropriately set in CGI scripts.
    """

    path = os.environ['PATH']  # /usr/bin:/usr/local/bin:/usr/X11/bin
    paths = re.split(os.pathsep, path)
    for program in programs:
        found = 0
        for dir in paths:
            if os.path.isdir(dir): # skip non-existing directories
                # check read and execute access in this directory:
                if not os.access(dir, os.R_OK | os.X_OK):
                    print dir, 'does not have read/execute access'
                    sys.exit(1)
                fullpath = os.path.join(dir,program)
                if os.path.isfile(fullpath):
                    found = 1
                    if where:
                        print program, 'found in', dir
                    break
        if not found:
            print "The program '%s' was not found" % program
            print 'PATH contains the directories\n','\n'.join(paths)

    path = os.environ['PYTHONPATH']
    paths = re.split(os.pathsep, path)
    for module in modules:
        found = 0
        for dir in paths:
            if os.path.isdir(dir): # skip non-existing directories
                # check read and execute access in this directory:
                if not os.access(dir, os.R_OK | os.X_OK):
                    print dir, 'does not have read/execute access'
                    sys.exit(1)
                fullpath = os.path.join(dir,module) + '.py'
                if os.path.isfile(fullpath):
                    found = 1
                    if where:
                        print module, 'found in', dir
                    break
        if not found:
            print "The module '%s' was not found" % module
            print 'PYTHONPATH contains the directories\n',\
            '\n'.join(paths)


def pow_eff(a,b, powfunc=math.pow):
    """
    Returns a^b. Smart function that happened to be slower
    than a straight math.pow.
    """
    if b == 2:
        return a*a
    elif b == 3:
        return a*a
    elif b == 4:
        h = a*a
        return h*h
    elif b == 1:
        return a
    elif abs(b) < 1.0E-15:  # x^0 ?
        return 1.0
    elif a == 0.0:
        return 0.0
    else:
        # check if b is integer:
        bi = int(b)
        if bi == b:
            r = 1
            for i in range(bi):
                r *= a
            return r
        else:
            if a < 0:
                raise ValueError, 'pow(a,b) with a=%g<0'
            else:
                return powfunc(a, b)

    
def lines2paragraphs(lines):
    """
    Return a list of paragraphs from a list of lines
    (normally holding the lines in a file).
    """
    p = []             # list of paragraphs to be returned
    firstline = 0      # first line in a paragraph
    currentline = 0    # current line in the file
    for line in lines:
        # for each new blank line, join lines from firstline
        # to currentline to a string defining a new paragraph:
        #if re.search(r'^\s*$', line):  # blank line?
        if line.isspace():  # blank line?
            if currentline > firstline:
                p.append(''.join(lines[firstline:currentline+1]))
                #print 'paragraph from line',firstline,'to',currentline
            # new paragraph starts from the next line:
            firstline = currentline+1  
        currentline += 1
    return p

            
def fontscheme1(root):
    """Alternative font scheme for Tkinter-based widgets."""
    default_font  = ('Helvetica', 13, 'normal')
    pulldown_font = ('Helvetica', 13, 'italic bold')
    scale_font    = ('Helvetica', 13, 'normal')
    root.option_add('*Font', default_font)
    root.option_add('*Menu*Font', pulldown_font)
    root.option_add('*Menubutton*Font', pulldown_font)
    root.option_add('*Scale.*Font', scale_font)

def fontscheme2(root):
    """Alternative font scheme for Tkinter-based widgets."""
    default_font  = ('Helvetica', 10, 'normal')
    pulldown_font = ('Helvetica', 10, 'italic bold')
    scale_font    = ('Helvetica', 10, 'normal')
    root.option_add('*Font', default_font)
    root.option_add('*Menu*Font', pulldown_font)
    root.option_add('*Menubutton*Font', pulldown_font)
    root.option_add('*Scale.*Font', scale_font)

def fontscheme3(root):
    """Alternative font scheme for Tkinter-based widgets."""
    default_font  = ('Fixed', 12, 'normal')
    root.option_add('*Font', default_font)

def fontscheme4(root):
    """Alternative font scheme for Tkinter-based widgets."""
    default_font  = ('Fixed', 14, 'normal')
    root.option_add('*Font', default_font)

def fontscheme5(root):
    """Alternative font scheme for Tkinter-based widgets."""
    default_font  = ('comic sans ms', 12, 'normal')
    root.option_add('*Font', default_font)

def fontscheme6(root):
    """Alternative font scheme for Tkinter-based widgets."""
    default_font  = ('trebuchet ms', 12, 'normal bold')
    root.option_add('*Font', default_font)

def fontscheme7(root):
    """Alternative font scheme for Tkinter-based widgets."""
    default_font  = ('verdana', 12, 'normal bold')
    root.option_add('*Font', default_font)

def fontscheme8(root):
    """Alternative font scheme for Tkinter-based widgets."""
    default_font  = ('verdana', 14, 'normal')
    root.option_add('*Font', default_font)




def movefiles(files, destdir, confirm=True, verbose=True, copy=True):
    """
    Move a set of files to a a destination directory tree,
    but let the original complete path be reflected in the
    destination tree.

    files         list of filenames
    destdir       root of destination directory tree
    confirm       let the user confirm movement of each file
    verbose       write out the original and new path of each file
    copy          True: copy, False: move

    The function is useful for backing up or temporarily moving
    files; the files are easily restored in their original
    locations since the original complete path is maintained in
    the destination directory tree.
    """
    if not os.path.isdir(destdir):
        os.mkdir(destdir)
    for file in files:
        perform_action = 'y'
        if confirm:
            print 'move %s to %s?' % (file, destdir)
            perform_action = sys.stdin.readline().strip()
        if perform_action in ('y', 'Y', 'yes', 'YES'):
            fullpath = os.path.abspath(file)
            # remove initial / (Unix) or C:\ (Windows):
            if sys.platform.startswith('win'):
                fullpath = fullpath[3:]
            else:  # Unix
                fullpath = fullpath[1:]
            newpath = os.path.join(destdir, fullpath)
            newdir = os.path.dirname(newpath)
            if not os.path.isdir(newdir): os.makedirs(newdir)
            shutil.copy2(file, newpath)
            if os.path.isfile(newpath):
                print 'fount',newpath
            s = 'copied'
            if not copy:  # pure move
                os.remove(file); s = 'moved'
            if verbose:
                print s, file, 'to', newpath


def debugregex(pattern, string):
    "debugging of regular expressions: write the match and the groups"
    s = "does '" + pattern + "' match '" + string + "'?\n"
    match = re.search(pattern, string)
    if match:
        s += string[:match.start()] + '[' + \
             string[match.start():match.end()] + \
             ']' + string[match.end():]
        if len(match.groups()) > 0:
            for i in range(len(match.groups())):
                s += '\ngroup %d: [%s]' % (i+1,match.groups()[i])
    else:
        s += 'No match'
    return s
                                     


# -- tests ---
def f(a, b, max=1.2, min=2.2):  # some function
    print 'a=%g, b=%g, max=%g, min=%g' % (a,b,max,min)


if __name__ == '__main__':
    task = 'Command'
    try:
        task = sys.argv[1]
    except:
        pass

    if task == 'Command':
        c = Command(f, 2.3, 2.1, max=0, min=-1.2)
        print 'Command.args=',c.args,'Command.kwargs=',c.kwargs
        c()         # call f(2.3, 2.1, 0, -1.2)
    elif task == 'debugregex':
        r = r'<(.*?)>'
        s = '<r1>is a tag</r1> and <s1>s1</s1> is too.'
        print debugregex(r,s)
        print debugregex(r'(\d+\.\d*)','a= 51.243 and b =1.45')


class BackgroundCommand(threading.Thread):
    """
    Run a function call with assignment in the background.
    Useful for putting time-consuming calculations/graphics
    in the background in an interactive Python shell.

    >>> b=BG('f', g.gridloop, 'sin(x*y)-exp(-x*y)')
    >>> b.start()
    running gridloop('sin(x*y)-exp(-x*y)',) in a thread
    >>> # continue with other interactive tasks
    >>> b.finished
    True
    >>> b.f  # result of function call
    """

    def __init__(self, result='result', func=None, args=[], kwargs={}):
        self.result = result
        self.__dict__[self.result] = None
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.finished = False
        threading.Thread.__init__(self)
    def run(self):
        kw = [key+'='+self.kwargs[key] for key in self.kwargs]
        cmd = '%s=%s(%s,%s)' % (self.result, self.func.__name__,
                                ','.join(self.args), ','.join(kw))
        print 'running %s in a thread' % cmd
        self.__dict__[self.result] = self.func(*self.args,**self.kwargs)
        self.finished = True
        print cmd, 'finished'

BG = BackgroundCommand  # short form

class Download(threading.Thread):
    def __init__(self, url, filename):
        self.url = url;  self.filename = filename
        threading.Thread.__init__(self)
    def run(self):
        print 'Fetching', self.url
        urllib.urlretrieve(self.url, self.filename)
        print self.filename, 'is downloaded'


def checkmathfunc(f, args):
    """
    Investigate the (mathematical) function f(*args):

       * Check that f works with scalar and array arguments

       * Check if args are scalars and if basic functions in
         f apply NumPy versions and not math
    """
    import numarray, Numeric
    # local import:
    __import__('Numeric', globals(), locals(), dir(Numeric))
    # could time f with scalar arguments
    # local import of math
    # time f again to see if f was faster

    # run f with 1D and 3D arrays, compare result with
    # corresponding loops and scalar evaluations
    raise Exception, 'NOT IMPLEMENTED YET'
