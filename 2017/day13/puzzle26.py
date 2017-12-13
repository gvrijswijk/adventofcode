# Advent of Code 2017
# Day 13; Puzzle 26
# Digital Plumber

# If there is a scanner at the top of the layer as your packet enters it,
# you are caught. (If a scanner moves into the top of its layer while you
# are there, you are not caught: it doesn't have time to notice you before
# you leave.)

c = 0
d = 0

def parse(row):
    n, m = row.strip('\n').split(': ')
    return [n, m]

with open('input.txt') as input:
    firewalls = [parse(row) for row in input.readlines()]
    #firewalls = [[0, 3], [1, 2], [4, 4], [6, 4]]

for fw in firewalls:
    if int(fw[0]) % (int(fw[1]) - 1) == 0 and int(fw[0]) / (int(fw[1]) - 1) % 2 == 0:
        c += int(fw[0]) * int(fw[1])

print("Part 1: " + str(c) +" points")

# Brute forcing part 2
# TODO: Implementing Chinese Remainder Theorem

while True:
    c = 0
    for fw in firewalls:
        if (int(fw[0]) + d) % (int(fw[1]) - 1) == 0 and (int(fw[0]) + d) / (int(fw[1]) - 1) % 2 == 0:
            c += int(fw[0]) * int(fw[1])
            d += 1
    if c == 0:
        print("Part 2: delay is " + str(d) + " picoseconds")
        False
        break
