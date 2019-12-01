with open ('input01.txt') as f:
    weights = f.readlines()

subtotal = 0
subtotal2 = 0

for weight in weights:
    fuel_added = int(weight)/3//1 - 2
    subtotal += fuel_added
    subtotal2 += fuel_added
    while fuel_added/3//1 - 2 > 0:
        fuel_added = fuel_added/3//1 - 2
        if fuel_added > 0:
            subtotal2 += fuel_added

print("Part 1:")
print(subtotal)

print("Part 2:")
print(subtotal2)
