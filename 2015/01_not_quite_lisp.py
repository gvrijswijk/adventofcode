#!/usr/bin/env python

with open('01_input.txt') as f:
    input = f.read()

print("Part 1: " + str(input.count('(') - input.count(')')))

score = 0
i = 0
while score >= 0:
    i = i + 1
    if input[i - 1] == '(':
        score += 1
    else:
        score -= 1

print("Part 2: " + str(i))
