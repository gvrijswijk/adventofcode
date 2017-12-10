# Advent of Code 2017
# Day 09; Puzzle 20

# iterable list
h = list(range(0, 256))

# default starting position
s1 = 0
s2 = 0
sk = 0

solution = ""

with open('input.txt') as input:
    x = input.read().strip()
    y = ""
    for i in range(len(x)):
        y = y + str(ord(x[i])) + ","
    y = y + "17,31,73,47,23"
    x = y
    x = x.split(',')
    #x = [3,4,1,5]
    #print(x)

    for r in range(64):
        for i in range(len(x)):

            j = h * 2
            s2 = s1 + int(x[i])

            j[s1:s2] = reversed(j[s1:s2])
            for k in range(s1, s2):
                h[k % len(h)] = j[k]

            s1 = (s2 + sk) % len(h)
            sk += 1
            sk = sk % len(h)
        r += 1

    for l in range(16):
        q = 0
        for m in range(16):
            q = q ^ h[l * 16 + m]
        if len(format(q, '02x')) == 1:
            solution = solution + "0" + format(q, '02x')
        else:
            solution = solution + format(q,'02x')

    print("Solution: " + solution)
