#!/usr/bin/env python

# Advent of Code 2017 - 00 Elvish Cheat Codes

import time

time_mp0 = time.time()

def parse(m):
    t, X, Y = [], [], []
    x, y = 0, 0

    for e in m:

        if e == "A" or e == "B":
            t.append(e)
            X.append(x)
            Y.append(y)
        elif e == "Up":
            y += 1
        elif e == "Down":
            y -= 1
        elif e == "Left":
            x -= 1
        elif e == "Right":
            x += 1

    return (t, X, Y)

def manhattan_distance(start, end=(0, 0)):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)

def part1(x):
    result = parse(x)
    return max(manhattan_distance(pair) for pair in zip(result[1], result[2]))

def part2(x):
    max_distance = 0
    result = parse(x)
    coordinates = list(zip(result[0],zip(result[1],result[2])))

    for start in coordinates:
        for end in coordinates:
            if start[0] != end[0]:
                distance = abs(end[1][0]-start[1][0]) + abs(end[1][1]-start[1][1])
                if distance > max_distance:
                    max_distance = distance

    return max_distance

if __name__ == "__main__":

    print("Advent of Code 2017 Warmup - Elvish Cheat Codes")

    with open('00_input.txt') as f:
        input = f.read().strip().split(', ')

    time_mp1 = time.time()

    p1 = part1(input)
    print(p1)

    time_mp2 = time.time()

    p2 = part2(input)
    print(p2)

    time_mp3 = time.time()

    print("Part 1: %.3f" % (time_mp2 - time_mp1))
    print("Part 2: %.3f" % (time_mp3 - time_mp2))
    print("Total:  %.3f" % (time.time() - time_mp0))
