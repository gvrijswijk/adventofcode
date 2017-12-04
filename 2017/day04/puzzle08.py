# Advent of Code 2017
# Day 04; Puzzle 07

count = 0

with open('input.txt') as input:
    x = input.read().strip()

for line in x.split('\n'):
    result = []
    if line.islower and line.isalpha:
        words = line.split(' ')
        for word in words:

            chars = [c for c in word]
            newword = "".join(sorted(chars))
            result.append(newword)

        if len(result) == len(set(result)):
            count += 1

print("Lines: " + str(len(x.split('\n'))))
print("Valid: " + str(count))
