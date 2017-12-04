# Advent of Code 2017
# Day 04; Puzzle 07

count = 0

with open('input2.txt') as input:
    x = input.read().strip()

for line in x.split('\n'):
    if line.islower and line.isalpha:
        words = line.split(' ')
        if len(words) == len(set(words)):
            count += 1

print(count)
