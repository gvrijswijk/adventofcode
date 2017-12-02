# Advent of Code 2017
# Day 02; Puzzle 03

solution = 0

# Open the input file
with open('input.txt') as input:
    x = input.read().strip()

for line in x.split('\n'):
    values = list(map(int, line.split('\t')))
    solution += (max(values) - min(values))

print(solution)
