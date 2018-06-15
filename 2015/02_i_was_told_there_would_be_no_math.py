#!/usr/bin/env python

import re

paper = 0
ribbon = 0

with open('02_input.txt') as f:
    input = f.readlines()

for line in input:

    dims = list(map(int, re.findall(r'(\d+)', line)))
    dims.sort()

    paper += 3 * dims[0] * dims[1] + 2 * dims[0] * dims[2] + 2 * dims[1] * dims[2]
    ribbon += 2 * (dims[0] + dims[1]) + dims[0] * dims[1] * dims[2]

print(paper)
print(ribbon)
