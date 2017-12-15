# Questions: https://pastebin.com/BMd61PUv

# Monitor x and y
coordinates = [0, 0]
locations = []
distance = []

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

for l in locations:
    for m in range(len(locations)):
        if l[0] != locations[m][0]:
            distx = int(l[1]) - locations[m][1]
            disty = int(l[2]) - locations[m][2]
            distance.append(abs(distx) + abs(disty))

print(max(distance))
