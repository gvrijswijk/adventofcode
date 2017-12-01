# Advent of Code 2017
# Day 01; Puzzle 01

solution = 0

# Open the input file
with open('input.txt') as input:
    x = input.read().strip()

# Iterate through the list
for i in range(len(x)):
    if x[i-1] == x[i]:
       solution += int(x[i])

# Check the last number in the string against the first ==> is already checked above
#if x[-1] == x[0]:
#    solution += int(x[-1])

# Display the solution
print(solution)
