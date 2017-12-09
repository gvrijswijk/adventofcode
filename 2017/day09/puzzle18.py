# Advent of Code 2017
# Day 09; Puzzle 18

import re
count = 0
score = 0

# Delete !
# Delete garbage
# Count groups

with open('input.txt') as input:
    t = input.read().strip()
    t = re.sub('(!!)*', "", t)
    t = re.sub('!.', "", t)
    bto = len(t)
    bags = len(re.findall('(<[^>]*>)', t))
    print(bags)
    t = re.sub('(<[^>]*>)',"", t)
    nto = len(t)
    print(nto)
    garbage = (bto - nto) - bags * 2

for i in range(len(t)):
    if t[i] == '{':
        count += 1
    elif t[i] == '}':
        score += count
        count -= 1

print("Groupscore: " + str(score))
print("Garbage deleted: " + str(garbage))
