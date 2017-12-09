# Advent of Code 2017
# Day 09; Puzzle 17

import re
count = 0
score = 0

# Delete !
# Delete garbage
# Count groups

with open('input.txt') as input:
    t = input.read().strip()
    t = re.sub('(!!)*', "", t)
    t = re.sub('!<', "", t)
    t = re.sub('!>', "", t)
    t = re.sub('!{', "", t)
    t = re.sub('!}', "", t)
    t = re.sub('(<[^>]*>)',"", t)

for i in range(len(t)):
    if t[i] == '{':
        count += 1
    elif t[i] == '}':
        score += count
        count -= 1

print(score)
