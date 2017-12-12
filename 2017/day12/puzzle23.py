# Advent of Code 2017
# Day 12; Puzzle 23
# Digital Plumber

import re


d1 = {}
c = 1

with open('input.txt') as input:

    for line in input:
        #print(line)
        m = re.match(r'(\w+) (<->) (.+)', line)
        n = m.group(1)
        o = m.group(3).split(', ')
        d1[n] = o

d2 = ['0']
for item in d2:
    for item2 in d1[item]:
        if item2 not in d2:
            d2.append(item2)
            c += 1

print(len(d2))
