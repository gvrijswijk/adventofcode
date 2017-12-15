# Advent of Code 2017
# Day 01; Puzzle 01

solution = 0

# Open the input file
with open('input.txt') as input:
    x = input.read().strip()

# Iterate through values
for i in range(len(x)/2):
    j = i + len(x)/2
    if x[i] == x[i + len(x)/2]:
        solution += 2 * int(x[i])

# Display the solution
print(solution)
