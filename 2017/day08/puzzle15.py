# Advent of Code 2017
# Day 08; Puzzle 15

import re
import operator
d = {}

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

# Copied from
key = max(d.keys(), key=(lambda k: d[k]))
print(key + ": " + str(d[key]))
