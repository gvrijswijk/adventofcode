# Advent of Code 2017
# Day 12; Puzzle 24
# Digital Plumber

# TODO: Popping is the issue?

import re
import itertools

d1 = {}
d2 = []
c = 1

with open('input.txt') as input:

    for line in input:
        #print(line)
        m = re.match(r'(\w+) (<->) (.+)', line)
        n = m.group(1)
        o = m.group(3).split(', ')
        d1[n] = o

for k in d1:
    if k not in list(itertools.chain(d2)):
        d2.append([])
        d2[-1].append(k)
        for item in d2[-1]:
            for item2 in d1[item]:
                if item2 not in list(itertools.chain(d2)):
                    d2[-1].append(item2)
                    c += 1
            print(len(d2[0]))
print(len(d2))
