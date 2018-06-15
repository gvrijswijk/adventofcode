#!/usr/bin/env python

import re

paper = 0

with open('02_input.txt') as f:
    input = f.readlines()

for line in input:
    dim = []
    dims = re.match(r'(\d+)[x](\d+)[x](\d+)', line)
    dim.append(int(dims[1]) * int(dims[2]))
    dim.append(int(dims[2]) * int(dims[3]))
    dim.append(int(dims[1]) * int(dims[3]))
    for item in dim:
        paper += 2 * item
    paper += min(dim)

print(paper)
