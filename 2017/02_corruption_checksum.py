#!/usr/bin/env python

# Advent of Code 2017 = 02 Correction Checksum

def part_1(input):
    solution = 0
    for line in input.split('\n'):
        values = list(map(int, line.split('\t')))
        solution += (max(values) - min(values))
    return solution

def part_2(input):
    solution = 0
    for line in input.split('\n'):
        values = list(map(int, line.split('\t')))
        for i in range(len(values)):
            for j in range(len(values)):
                if (i != j) and values[i]%values[j] == 0:
                    solution += values[i]/values[j]
    return int(solution)

with open('02_input.txt') as f:
    input = f.read().strip()

print(part_1(input))
print(part_2(input))
