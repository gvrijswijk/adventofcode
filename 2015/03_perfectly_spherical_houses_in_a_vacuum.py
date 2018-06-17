#!/usr/bin/env python

headings = {
    "^": 1j,
    "v": -1j,
    "<": -1,
    ">": 1,
}

location = complex
location = 0
visited = {
    0: 1
}

with open('03_input.txt') as f:
    input = f.read()

for character in input:
    location = location + headings[character]
    if location in visited:
        visited[location] += 1
    else:
        visited[location] = 1


print(len(visited))
print(len(input))

location = 0
visited = {
    0: 2
}

for character in input[::2]:
    location = location + headings[character]
    if location in visited:
        visited[location] += 1
    else:
        visited[location] = 1

location = 0
for character in input[1::2]:
    location = location + headings[character]
    if location in visited:
        visited[location] += 1
    else:
        visited[location] = 1

print(len(visited))
print(len(input))
