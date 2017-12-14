# Advent of Code 2017
# Day 14; Puzzle 27
# Disk Defragmentation

input = 'ljoxqyyw'
#input = 'flqrgnkx' # Testinput

total = 0

def bin(x):
    lib = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'a': '1010',
        'b': '1011',
        'c': '1100',
        'd': '1101',
        'e': '1110',
        'f': '1111'}
    return lib[x]

for p in range(128):
    # iterable list
    h = list(range(0, 256))

    # default starting position
    s1 = 0
    s2 = 0
    sk = 0

    solution = ""
    y = ""
    input2 = input + "-" + str(p)
    #print(input2)
    for j in input2:
        y = y + str(ord(j)) + ","
    y = y + "17,31,73,47,23"

    x = y.split(',')
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
        #    r += 1

    for l in range(16):
        q = 0
        for m in range(16):
            q = q ^ h[l * 16 + m]
            #print(q)
        if len(format(q, '02x')) == 1:
            solution = solution + "0" + format(q, '02x')
        else:
            solution = solution + format(q,'02x')

    w = ""

    for c in solution:
        w = w + bin(c)

    total += w.count('1')

    #print("Solution: " + solution)
    #print("Binary: " + w)
print(total)
