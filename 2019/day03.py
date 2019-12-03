import re

Point = complex
dir ={'R': 1, 'L': -1, 'U': 1j, 'D': -1j}

with open('input03.txt') as f:
    i = f.read().strip().split('\n')

visited = []

for c, j in enumerate(i):
    visited.append([])
    loc = 0
    for k in re.findall(r'([RLDU])(\d+)', j):
        for l in range(int(k[1])): 
            loc += dir[k[0]]
            visited[c].append(loc)

distances = []

for point in (set(visited[0]) & set(visited[1])):
    distances.append(point.real+point.imag) 

print("Part 1:")
print(min(distances))

d2 = []

for point in set(visited[0]) & set(visited[1]):
    d2.append(visited[0].index(point) + visited[1].index(point))

print(min(d2) + 2)
