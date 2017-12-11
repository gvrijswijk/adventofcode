# Advent of Code 2017
# Day 10; Puzzle 19

from itertools import chain

# iterable list
h = list(range(0, 256))
#h = list(range(0, 5))

# default starting position
s1 = 0
s2 = 0
sk = 0

with open('input.txt') as input:
    # moveset as input
    x = input.read().strip().split(',')
    #x = [3,4,1,5]

    for i in range(len(x)):

        j = h * 2
        s2 = s1 + int(x[i])

        j[s1:s2] = reversed(j[s1:s2])
        for k in range(s1, s2):
            h[k % len(h)] = j[k]

        s1 = (s2 + sk) % len(h)
        sk += 1

        print(h)
    print("Solution: " + str(h[0] * h[1]))
