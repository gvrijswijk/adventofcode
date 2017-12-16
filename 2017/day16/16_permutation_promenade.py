#!/usr/bin/env python

# Advent of Code 2017 - 01 Inverse Captcha

import time
import re

time_mp0 = time.time()

def parse(x):
    print('hello also')

def the_moves():
    print('hello')


if __name__ == "__main__":

    with open('16_input.txt') as f:
        input = f.read().strip().split(',')
        #input = ['s1', 'x3/4', 'pe/b'] #Test

line = 'abcdefghijklmnop'
times = 1000000000
#line = 'abcde' #Test

time_mp1 = time.time()

line = list(line)

for l in input:
    if l[0] == "p":
        m = re.match(r'[p](\w+)[/](\w+)', l)
        n = line.index(m.group(1))
        o = line.index(m.group(2))
        line[n], line[o] = line[o], line[n]
    if l[0] == "s":
         m = re.match(r'[s](\w+)', l)
         n = len(line) - int(m.group(1))
         line = line[n:] + line[0:n]
    elif l[0] == "x":
        m = re.match(r'[x](\w+)[/](\w+)', l)
        n = int(m.group(1))
        o = int(m.group(2))
        line[n], line[o] = line[o], line[n]

line = ''.join(line)
print("Part 1: " + line)

time_mp2 = time.time()

line = 'abcdefghijklmnop'
line1 = line
times = 1000000000
#line = 'abcde' #Test
j = 0


line = list(line1)

while True:
    j = j + 1
    for l in input:
        if l[0] == "p":
            m = re.match(r'[p](\w+)[/](\w+)', l)
            n = line.index(m.group(1))
            o = line.index(m.group(2))
            line[n], line[o] = line[o], line[n]
        if l[0] == "s":
             m = re.match(r'[s](\w+)', l)
             n = len(line) - int(m.group(1))
             line = line[n:] + line[0:n]
        elif l[0] == "x":
            m = re.match(r'[x](\w+)[/](\w+)', l)
            n = int(m.group(1))
            o = int(m.group(2))
            line[n], line[o] = line[o], line[n]

    if ''.join(line) == line1:
        times = times % j
        break

line = list(line1)

for i in range(times):
    for l in input:
        if l[0] == "p":
            m = re.match(r'[p](\w+)[/](\w+)', l)
            n = line.index(m.group(1))
            o = line.index(m.group(2))
            line[n], line[o] = line[o], line[n]
        if l[0] == "s":
             m = re.match(r'[s](\w+)', l)
             n = len(line) - int(m.group(1))
             line = line[n:] + line[0:n]
        elif l[0] == "x":
            m = re.match(r'[x](\w+)[/](\w+)', l)
            n = int(m.group(1))
            o = int(m.group(2))
            line[n], line[o] = line[o], line[n]

line = ''.join(line)
print("Part 2: " + line)

time_mp3 = time.time()

print("Part 2: %.3f" % (time_mp2 - time_mp1))
print("Part 2: %.3f" % (time_mp3 - time_mp2))
print("Total:  %.3f" % (time.time() - time_mp0))
