#!/usr/bin/env python
"""
Generate combination of multiple-valued parameters.

The purpose of this module is to set up parameter studies
based on a certain input format for variables where multiple
values of each parameter can be given.
"""

import re, operator
import py4cs.misc

def input2values(s):
    """
    Translate a string s with multiple loop syntax into
    a list of single values (for the corresponding parameter).

    Multiple loop syntax:
    '-1 & -3.4 & 20 & 70 & [0:10,1.3] & [0:10] & 11.76'
    """
    if not isinstance(s, basestring):
        return s
    
    items = s.split('&')

    values = []
    for i in items:
        i = i.strip()  # white space has no meaning
        # is i a loop?
        m = re.search(r'\[(.+):([^,]+),?(.*)\]',i)
        if m:
            # the group are numbers, take eval to get right type
            start = eval(m.group(1))
            stop  = eval(m.group(2))
            try:
                incr = m.group(3).strip()
                incr_op = operator.add
                if incr[0] == '*':
                    incr_op = operator.mul
                    incr = incr[1:]
                elif incr[0] == '+' or incr[0] == '-':
                    incr = incr[1:]
                incr = eval(incr)
            except:
                incr = 1
            r = start
            while (r <= stop and start <= stop) or \
                  (r >= stop and start >= stop):
                values.append(r)
                r = incr_op(r, incr)
        else:
            # just an ordinary item, convert i to right type:
            values.append(py4cs.misc.str2obj(i))
    # return list only if there are more than one item:
    if len(values) == 1:
        return values[0]
    else:
        return values

def _outer(a, b):
    """
    Return the outer product/combination of two lists.
    a        multi- or one-dimensional list or scalar
    b        one-dimensional list or scalar (new parameter)
    Return:  outer combination 'all'.
    The function is to be called repeatedly:
        all = _outer(all, p)
    """
    all = []
    if not isinstance(a, list):
        raise TypeError, 'a must be a list'
    if not isinstance(b, list):  b = [b]

    if len(a) == 0:
        # first call:
        for j in b:
            all.append([j])
    else:
        for j in b:
            for i in a:
                if not isinstance(i, list):
                    raise TypeError, 'a must be list of list'
                # note: i refers to a list; i.append(j) changes
                # the underlying list (in a), which is not what
                # we want, we need a copy, extend the copy, and
                # add to all
                k = i + [j]  # extend previous prms with new one
                all.append(k)
    return all

def combine(prm_values):
    """
    prm_values may be a nested list: prm_values[i] contains
        (parameter_name, list_of_parameter_values)
    for parameter no. i.
    prm_values may instead be a dictionary
        prm_values[parameter_name] = list_of_parameter_values
    
    Three lists are returned:
        all     all combinations (experiments)
                all[i] is the list of parameter values in
                experiment no i
        names   list of all parameter names
        varied  list of parameter names that are varied

    """
    if isinstance(prm_values, dict):
        # turn dict into list [(name,values),(name,values),...]:
        prm_values = [(name, prm_values[name]) \
                      for name in prm_values]
    all = []
    varied = []
    for name, values in prm_values:
        all = _outer(all, values)
        if isinstance(values, list) and len(values) > 1:
            varied.append(name)
    names = [name for name, values in prm_values]
    return all, names, varied



def dump(all, names, varied):
    e = 1
    for experiment in all:
        print 'Experiment %4d:' % e,
        for name, value in zip(names, experiment):
            print '%s:' % name, value,
        print # newline
        e += 1  # experiment counter

    for experiment in all:
        cmd = ' '.join(['-'+name+' '+repr(value) for \
                        name, value in zip(names, experiment)])
        print cmd

def options(all, names, prefix='--'):
    """
    Return a list of command-line options.
    Input:
    all[i]      list of parameter values in experiment no i
    names[i]    name of parameter no. i
    Return:
    cmd[i]      -name value pairs of all parameters in
                experiment no. i
    """
    cmd = []
    for experiment in all:
        cmd.append(' '.join([prefix+name+' '+repr(py4cs.misc.str2obj(value)) \
                   for name, value in zip(names, experiment)]))
    return cmd

def varied_parameters(parameters, varied, names):
    """
    Extract a subset of parameters corresponding to the
    names listed in the varied list. All names are in the
    list names. The parameters list corresponds to names.
    >>> parameters = [1,5,3]
    >>> names = ['a','b','c']
    >>> varied = ['a','c']
    >>> varied_parameteres(parameters, varied, names)
    [1,3]
    """
    indices_varied = [names.index(i) for i in varied]
    varied_parameters = [parameters[i] for i in indices_varied]
    return varied_parameters

def remove(condition, all, names):
    """
    Remove experiments that fulfill a boolean condition.
    Example:
    all = remove('w < 1.0 and p = 1.2) or (q in (1,2,3) and f < 0.1', all, names)
    (names of the parametes must be used)
    """
    import copy
    for ex in copy.deepcopy(all):  # iterate over a copy of all!
        c = condition
        for n in names:  # replace names by actual values
            print 'replace "%s" by "%s"' % (n, repr(ex[names.index(n)]))
            c = c.replace(n, repr(ex[names.index(n)]))
            # note the use of repr: strings must be quoted
            #print 'remove ',remove
        if eval(c):  # if condition
            all.remove(ex)
    return all  # modified list
    

def _test1():
    s1 = ' -3.4 & [0:4,1.2] & [1:4,*1.5] & [0.5:6E-2,  *0.5]'
    #s2 = "method1 &  abc  & 'adjusted method1' "
    s2 = 0.22
    s3 = 's3'
    l1 = input2values(s1)
    l2 = input2values(s2)
    l3 = input2values(s3)
    p = [('prm1', l3), ('prm2', l2), ('prm3', l1)]
    all, names, varied = combine(p)
    dump(all, names, varied)
    p = {'w': [0.7, 1.3, 0.1], 'b': [1, 0], 'func': ['y', 'siny']}
    all, names, varied = combine(p)
    print '\n\n\n'
    dump(all, names, varied)
    print options(all, names, prefix='-')

def _test2():
    p = {'w': '[0.7:1.3,0.1]', 'b': '1 & 0.3 & 0', 'func': 'y & siny'}
    print input2values(p['w'])
    print input2values(p['b'])
    print input2values(p['func'])
    prm_values = [(name, input2values(p[name])) \
                  for name in p]
    print prm_values
    all, names, varied = combine(p)
    # rule out b=0 when w>1
    all_restricted = [];
    bi = names.index('b'); wi = names.index('w')
    for e in all:
        if e[bi] == 0 and e[wi] > 1:
            pass # rule out
        else:
            all_restricted.append(e)  # del would be dangerous!
    # b->damping, w->omega:
    names2 = names[:]
    names2[names.index('b')] = 'damping'
    names2[names.index('w')] = 'omega'
    print options(all, names, prefix='--')
    conditions = (('b',operator.eq,0), ('w',operator.gt,1))
    def rule_out(all, conditions):
        all_restricted = []
        for e in all:
            for name, op, r in conditions:
                pass

class MultipleLoop:
    """
    High-level, simplified interface to the functionality in
    the multipleloop module.

    Typical application:
    p = {'name1': 'multiple values', 'name2': 'values', ...}
    experiments = py4cs.multipleloop.MultipleLoop(option_prefix='-')
    for name in p:
        experiments.add(name, p[name])
    for cmlargs, parameters, varied_parameters in experiments:
        <run experiment: some program + cmlargs>
        <extract results and save>

    Attributes (m is some MultipleLoop object):
    m.names         names of all parameters
    m.varied        names of parameters with multiple values
    m.options       list of strings of all command-line arguments
                    (-name value), one for each experiment
    m.all           list of all experiments
    m.prm_values    list of (name, valuelist) tuples
    """
    def __init__(self, option_prefix='--'):
        self.option_prefix = option_prefix
        self.prm_values = []
        self.combined = False

    def add(self, prm_name, str_with_values):
        self.prm_values.append((prm_name, input2values(str_with_values)))

    def combine(self):
        self.all, self.names, self.varied = combine(self.prm_values)
        self.indices_varied = [self.names.index(i) for i in self.varied]
        self.options = options(self.all, self.names, prefix=self.option_prefix)
        self.combined = True

    def remove(self, condition):
        """
        Remove experiments that fulfill a boolean condition.
        Example:
        e.remove('w < 1.0 and p = 1.2) or (q in (1,2,3) and f < 0.1')
        (names of the parametes must be used)
        """
        self.combine() # compute all combinations
        nex_orig = len(self.all)
        self.all = remove(condition, self.all, self.names)
        # self.options depend on self.all, which might be alterend:
        self.options = options(self.all, self.names, prefix=self.option_prefix)
        # return no of removed experiments:
        return nex_orig-len(self.all)
        
    def __iter__(self):
        if not self.combined: self.combine()
        self.counter = 0
        return self

    def next(self):
        if self.counter > len(self.options)-1:
            raise StopIteration
        self.cmlargs = self.options[self.counter]
        self.parameters = self.all[self.counter]
        self.varied_parameters = \
             [self.parameters[i] for i in self.indices_varied]
        self.counter += 1
        return self.cmlargs, self.parameters, self.varied_parameters

class ReportHTML:
    def __init__(self, filename):
        self.filename = filename
        f = open(self.filename, 'w') # new file
        f.write("""<HTML><BODY>\n""")
        f.close()
        self._experiment_section_counter = 0

    def dump(self, text):
        f = open(self.filename, 'a')
        f.write(text)
        f.close()

    def experiment_section(self, parameters, names, varied):
        """
        Start new H1 section in the HTML document.
        parameters is a list of the values of all parameters
        in an experiment, names holds the names of all
        parameters, and varied holds the names of the
        parameters that are actually varied.
        The three input lists are computed by functions in
        this module (or the MultipleLoops class).
        """
        self._experiment_section_counter += 1
        t = """
<H1>Experiment no. %d</H1>
Varied parameters:
<UL>
""" % self._experiment_section_counter
        for n in varied:
            i = names.index(n)
            t += """\n<LI> %s: %s""" % (n, parameters[i])
        t += """
</UL>
Fixed parameters:
"""
        for n in names:
            if n not in varied:  # not treated above?
                i = names.index(n)
                t += """%s=%s, """ % (n, parameters[i])
        t = t[:-2]  # strip the last ', '
        self.dump(t)

        def __del__(self):
            self.dump("""\n</BODY></HTML>\n""")
        
if __name__ == '__main__':
    _test1()
    _test2()

    
