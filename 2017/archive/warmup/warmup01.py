# Questions: https://pastebin.com/BMd61PUv

# Monitor x and y
coordinates = [0, 0]
locations = []

# Open the input file
with open('input.txt') as input:
    x = input.read().split(', ')

# Follow the path ==> probably can be done much more elegant
for i in range(0, len(x)):
    move = x[i].strip()
    if move == "Up":
        coordinates[1] += 1
    elif move == "Down":
        coordinates[1] -= 1
    elif move == "Left":
        coordinates[0] -= 1
    elif move == "Right":
        coordinates[0] += 1
    elif move == "A":
        y = ["A", coordinates[0], coordinates[1]]
        locations.append(y)
    elif move == "B":
        y = ["B", coordinates[0], coordinates[1]]
        locations.append(y)

distance = [(abs(x[2]) + abs(x[1])) for x in locations]
print(max(distance))
