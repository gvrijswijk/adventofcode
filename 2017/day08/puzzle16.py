# Advent of Code 2017
# Day 08; Puzzle 16

import re
import operator
d = {}
maxv = 0

def evals(a,b,c):
    ops = {
        '>': operator.gt,
        '<': operator.lt,
        '==': operator.eq,
        '<=': operator.le,
        '>=': operator.ge,
        '!=': operator.ne,
        'inc': operator.add,
        'dec': operator.sub
    }
    return ops[c](a,b)

with open('input.txt') as input:

    for line in input:
        m = re.match(r'(\w+) (\w+) (\-?\d+)( if )(\w+) ([<>=!]+) (\-?\d+)', line)
        if evals(d.get(m.group(5), 0), int(m.group(7)), m.group(6)):
            k = m.group(1)
            v = evals(d.get(m.group(1), 0), int(m.group(3)), m.group(2))
            d[k] = v
            if v > maxv:
                maxv = v

# Copied from
key = max(d.keys(), key=(lambda k: d[k]))
print("Maximum: " + key + " --> " + str(d[key]))
print("Maximum value in registers at any point: " + str(maxv))
