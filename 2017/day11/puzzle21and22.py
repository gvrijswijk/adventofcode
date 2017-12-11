# Advent of Code 2017
# Day 11; Puzzle 21 & 22

m = {
    'n': [0, 2],
    's': [0, -2],
    'nw': [-1, 1],
    'ne': [1, 1],
    'sw': [-1, -1],
    'se': [1, -1]
}

x = 0
y = 0
moves = 0
maxmoves = 0

with open('input.txt') as input:
    n = input.read().strip().split(',')

    for i in range(len(n)):
        x += int(m[n[i]][0])
        y += int(m[n[i]][1])
        moves = abs(x) + (abs(y) - abs(x)) / 2
        if moves > maxmoves:
            maxmoves = moves

print(moves)
print(maxmoves)
