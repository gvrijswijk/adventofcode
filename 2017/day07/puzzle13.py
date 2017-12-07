# Advent of Code 2017
# Day 07; Puzzle 13

#x = "pwaugpr (6) -> utnhs, xjqta, ssmfscq"
#x = "pwaugpr (6)"

w = []

with open('input.txt') as input:
    x = input.read()
    y = x.strip().split('\n')

for i in range(len(y)):
    w = y[i].split(' ')
    if x.count(w[0]) == 1:
        print(w[0])
