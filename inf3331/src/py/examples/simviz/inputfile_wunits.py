#!/usr/bin/env python
import sys, re
from py4cs.ParameterInterface import Parameters, AutoSimVizGUI
from Scientific.Physics.PhysicalQuantities import PhysicalQuantity
from Tkinter import *

def parse_input_file(lines):
    line_re = re.compile(r'set (.*?)\s*=\s*([^!]*)\s*(!?.*)')
    comment_re = re.compile(r'!\s*\[(.*?)\](.*)')
    value_re = re.compile(r'([0-9.Ee\-+]+)\s+([A-Za-z0-9*/.()]+)')
    parsed_lines = []        # list of dictionaries
    output_lines = []        # new lines without units

    for line in lines:
        m = line_re.search(line)
        # split line into parameter, value, and comment:
        if m:
            parameter = m.group(1).strip()
            value = m.group(2).strip()
            try:  # a comment is optional
                comment = m.group(3)
            except:
                comment = ''
            ref_unit = None; unit = None  # default values
            if comment:
                # does the comment contain a unit specification?
                m = comment_re.search(comment)
                if m:
                    ref_unit = m.group(1)
                    # is the value of the form 'value unit'?
                    m = value_re.search(value)
                    if m:
                        number, unit = m.groups()
                    else: # no unit, use the reference unit
                        number = value;  unit = ref_unit
                        value += ' ' + ref_unit
                    # value now has value _and_ unit
                    # convert unit to ref_unit:
                    pq = PhysicalQuantity(value)
                    pq.convertToUnit(ref_unit)
                    value = str(pq).split()[0]
            output_lines.append('set %s = %s %s\n' % \
                                (parameter, value, comment))
            parsed_lines.append({'parameter' : parameter,
                                 'value' : value, # in ref_unit
                                 'ref_unit' : ref_unit,
                                 'unit' : unit,
                                 'comment' : comment})
        else:
            output_lines.append(line)
            parsed_lines.append(line)
    return output_lines, parsed_lines

def lines2prms(parsed_lines, parameters=None):
    if parameters is None:
        parameters = Parameters(interface='GUI')
    for line in parsed_lines:
        if isinstance(line, dict):
            comment = line['comment']
            if line['ref_unit'] is not None:
                # parameter has value with unit:
                help = 'unit: '+line['ref_unit']+'; '+comment[1:]
                unit = line['ref_unit']
                str2type = float  # unit conversions -> float
            else:
                help = comment[1:]
                unit = None
                str2type = str  # use strings in general
            parameters.add(name=line['parameter'],
                           default=line['value'],
                           str2type=str2type,
                           widget_type='entry',
                           help=help, unit=unit)
    return parameters

def GUI(parameters, root):
    gui = AutoSimVizGUI()
    gui.make_prmGUI(root, parameters, height=300)
    Button(root, text='Quit', command=root.destroy).pack()
    root.mainloop()
    return parameters

def prms2lines(parameters, parsed_lines):
    output_lines = []
    for line in parsed_lines:
        if isinstance(line, str):
            output_lines.append(line)
        else:
            # line is a dictionary; turn it into a line
            prm = line['parameter']
            value = parameters[prm]
            comment = line['comment']
            output_lines.append('set %s = %s %s\n' % \
                                (prm, value, comment))
    return output_lines

if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    new_lines, parsed_lines = parse_input_file(lines)
    for line in new_lines:
        print line,  # (line has a trailing newline, print adds one)
    for i in parsed_lines:
        print i
    root = Tk()  # Tk() must have been called before Parameters work
    p = lines2prms(parsed_lines)
    p = GUI(p, root)  # read values from a GUI
    lines = prms2lines(p, parsed_lines)
    print '\n\n\nfinal output:\n'
    sys.stdout.writelines(lines)
    



                    
            

