# Advent of Code 2017
# Day 02; Puzzle 03

solution = 0

# Open the input file
with open('input.txt') as input:
    x = input.read().strip()

for line in x.split('\n'):
    values = list(map(int, line.split('\t')))
    for i in range(len(values)):
        for j in range(len(values)):
            if (i != j) and (values[i]/values[j] == int(values[i]/values[j])):
                solution += int(values[i]/values[j])

print(solution)
