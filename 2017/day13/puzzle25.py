# Advent of Code 2017
# Day 12; Puzzle 23
# Digital Plumber

c = 0

def parse(row):
    n, m = row.strip('\n').split(': ')
    return [n, m]

with open('input.txt') as input:
    firewalls = [parse(row) for row in input.readlines()]
    #firewalls = [[0, 3], [1, 2], [4, 4], [6, 4]]

for fw in firewalls:
    if int(fw[0]) % (int(fw[1]) - 1) == 0 and int(fw[0]) / (int(fw[1]) - 1) % 2 == 0:
        c += int(fw[0]) * int(fw[1])

print(c)
