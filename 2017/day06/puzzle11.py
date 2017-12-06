# Advent of Code 2017
# Day 06; Puzzle 11

import copy

#x = [0, 2, 7, 0]

with open('input.txt') as input:
    x = list(map(int, input.read().strip().split()))

s = []
y = copy.copy(x)


while y not in s:
    s.append(y)
    v = max(x)
    i = x.index(v)
    x[i] = 0

    while v > 0:
        if i == len(x) - 1:
            i = 0
        else:
            i += 1
        x[i] += 1
        v -= 1

    y = copy.copy(x)

print(len(s))
