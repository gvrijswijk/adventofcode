input02 = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0"
#input02 = "1,9,10,3,2,3,11,0,99,30,40,50"

i = [int(e) for e in input02.split(',')]
i[1] = 12
i[2] = 2

for j in range(0, len(i), 4):
    if i[j] == 99:
        break
    elif i[j] == 1:
        i[i[j + 3]] = i[i[j + 1]] + i[i[j + 2]]
    elif i[j] == 2:
        i[i[j + 3]] = i[i[j + 1]] * i[i[j + 2]]

print('Part 1:')
print(i[0])

target = 19690720
maxi = 100
for verb in range(maxi):
    for noun in range(maxi):
        i = [int(e) for e in input02.split(',')]
        i[1] = noun
        i[2] = verb
        for j in range(0, len(i), 4):
            if i[j] == 99:
                break
            elif i[j] == 1:
                i[i[j + 3]] = i[i[j + 1]] + i[i[j + 2]]
            elif i[j] == 2:
                i[i[j + 3]] = i[i[j + 1]] * i[i[j + 2]]
        if i[0] == target:
            print(100 * noun + verb)
