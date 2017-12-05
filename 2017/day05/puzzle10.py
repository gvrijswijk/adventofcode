# Advent of Code 2017
# Day 05; Puzzle 09

count = 0
i = 0

with open('input.txt') as input:
    x = list(map(int, input.read().strip().split()))

while i < len(x) and i >= 0:
    count += 1
    oldval = x[i]
    oldind = i
    if oldval >= 3:
        newval = x[i] - 1
    else:
        newval = x[i] + 1
    i = i + oldval
    x[oldind] = newval

print("Number of moves: " + str(count))
