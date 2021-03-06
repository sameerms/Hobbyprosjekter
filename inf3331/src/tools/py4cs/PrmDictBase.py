#!/usr/bin/env python
import re, os, sys

def message(m):
    if os.environ.get('DEBUG', '1') == '1':
        print m
    

class PrmDictBase(object):
    """
    Base class for solvers with parameters stored in dictionaries.

    Data dicts whose keys are fixed (non-extensible):
      self.*_prm
    These are filled in subclasses by, e.g.,
      self.physical_prm['someprm'] = value
    or
      self.physical_prm.update({'someprm': value,
                                'another': other_value})
    The dictionary with all legal keys should be defined in the subclass.

    List of the dictionaries with fixed keys:
      self._prm_list = [self.physical_prm, self.numerical_prm]
    Subclasses define any self._*_prm dicts and append
    them to self._prm_list.

    Meta data given by the user can be stored in self.user_prm.
    This attribute is None if meta data are not allowed,
    otherwise it is a dictionary that holds parameters.

    self._type_check[prm] is defined if we want to type check
    a parameter prm.
    if self._type_check[prm] is True (or False), prm must
    be None, of the same type as the previous registered
    value of prm, or any number (float, int, complex) if
    the previous value prm was any number.
    """
    
    def __init__(self):
        # dicts whose keys are fixed (non-extensible):
        self._prm_list = []     # fill in subclass
        self.user_prm = None    # user's meta data
        self._type_check = {}   # fill in subclass

    def _prm_dict_names(self):
        """Return the name of all self.*_prm dictionaries."""
        #names = []
        #for attr in self.__dict__:
        #    print attr
        #    if re.search(r'^[^_].*_prm$', attr):
        #        names.append(attr)
        names = [attr for attr in self.__dict__ if \
                 re.search(r'^[^_].*_prm$', attr)]
        return names
                
    def usage_set(self):
        """Print the name of parameters that can be set."""
        prm_dict_names = self._prm_dict_names()
        prm_names = []
        for name in prm_dict_names:
            d = self.__dict__[name]
            if isinstance(d, dict):
                k = d.keys()
                k.sort(lambda a,b: cmp(a.lower(),b.lower()))
                prm_names += k
        print 'registered parameters:\n'
        for i in prm_names:
            print i
        # alternative:
        # names = []
        # for d in self._prm_list:
        #     names += d.keys()
        # names.sort
        # print names

    def dump_set(self):
        for d in self._prm_list:
            keys = d.keys()
            keys.sort(lambda a,b: cmp(a.lower(),b.lower()))
            for prm in keys:
                print '%s = %s' % (prm, d[prm])
        
    def set(self, **kwargs):
        """Set kwargs data in parameter dictionaries."""
        # print usage message if no arguments:
        if len(kwargs) == 0:
            self.usage_set()
            return
        
        for prm in kwargs:
            set = False
            for d in self._prm_list:
                if len(d.keys()) == 0:
                    raise ValueError, 'self._prm_list is wrong (empty)'
                try:
                    if self.set_in_dict(prm, kwargs[prm], d):
                        set = True
                        break
                except TypeError, msg:
                    print msg
                    #break
                    sys.exit(1)  # type error is fatal

            if not set:   # maybe set prm as meta data?
                if isinstance(self.user_prm, dict):
                    # not a registered parameter:
                    self.user_prm[prm] = kwargs[prm]
                    message('%s=%s assigned in self.user_prm' % \
                            (prm, kwargs[prm]))
                else:
                    raise NameError, \
                          'parameter "%s" not registered' % prm
        self._update()

    def set_in_dict(self, prm, value, d):
        """
        Set d[prm]=value, but check if prm is registered in class
        dictionaries, if the type is acceptable, etc.
        """
        can_set = False
        # check that prm is a registered key
        if prm in d:
            if prm in self._type_check:
                # prm should be type-checked
                if isinstance(self._type_check[prm], int):
                    # (bool is subclass of int)
                    if self._type_check[prm]:
                        # type check against prev. value or None:
                        if isinstance(value, (type(d[prm]), None)):
                            can_set = True
                        # allow mixing int, float, complex:
                        elif operator.isNumberType(value) and\
                                 operator.isNumberType(d[prm]):
                            can_set = True
                elif isinstance(self._type_check[prm], (tuple,list,type)):
                    # self._type_check[prm] holds tuple of
                    # legal types:
                    #print 'testing %s=%s against type %s' % (prm,value,self._type_check[prm])
                    if isinstance(value, self._type_check[prm]):
                        can_set = True
                    else:
                        raise TypeError, \
                              '\n\n%s=%s has type %s, not %s or None\n'\
                              'self._type_check=%s' % \
                              (prm, value, type(d[prm]),
                               self._type_check[prm],
                               self._type_check)
                else:
                    raise TypeError, 'self._type_check["%s"] must be '\
                          'int/book or type (float,int,...) values, '\
                          'not %s' % (prm,type(self._type_check[prm]))
            else:
                can_set = True
        else:
            message('%s is not registered in\n%s' % (prm, d))
        if can_set:
            d[prm] = value
            message('%s=%s is assigned' % (prm, value))
            return True
        return False
        

    def _update(self):
        """Check data consistency and make updates."""
        # to be implemented in subclasses
        pass

    def properties(self, global_namespace):
        """Make properties out of local dictionaries."""
        for ds in self._prm_dict_names():
            d = eval('self.' + ds)
            for prm in d:
                # properties cannot have whitespace:
                prm = prm.replace(' ', '_')
                cmd = '%s.%s = property(fget='\
                      'lambda self: self.%s["%s"], %s)' % \
                      (self.__class__.__name__, prm, ds, prm,
                       ' doc="read-only property"')
                print cmd
                exec cmd in global_namespace, locals()

    def dicts2namespace(self, namespace, dicts, overwrite=True):
        """Make namespace variables out of dict items."""
        # can be tuned in subclasses
        for d in dicts:
            if overwrite:
                namespace.update(d)
            else:
                for key in d:
                    if key in namespace and not overwrite:
                        print 'cannot overwrite %s' % key
                    else:
                        namespace[key] = d[key]

    def dicts2namespace2(self, namespace, dicts):
        """As dicts2namespace2, but use exec."""
        # can be tuned in subclasses
        for d in dicts:
            for key in d:
                exec '%s=%s' % (key,repr(d[key])) in globals(), namespace

    def namespace2dicts(self, namespace, dicts):
        """Update dicts from variables in a namespace."""
        keys = []    # all keys in namespace that are keys in dicts
        for key in namespace:
            for d in dicts:
                if key in d:
                    d[key] = namespace[key]  # update value
                    keys.append(key)         # mark for delete
        # clean up what we made in self.dicts2namespace:
        for key in keys:
            del namespace[key]

# initial tests are found in src/py/examples/classdicts.py
