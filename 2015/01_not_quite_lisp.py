#!/usr/bin/env python

with open('01_input.txt') as f:
    input = f.read()

print("Part 1: " + str(input.count('(') - input.count(')')))

score = 0
i = 0
while score >= 0:
    if input[i] == '(':
        score += 1
    else:
        score -= 1
    i += 1

print("Part 2: " + str(i))
