# Advent of Code 2017
# Day 14; Puzzle 28
# Disk Defragmentation - Part 2

# TODO: Study this solution; conceptually this is what I wanted

input = 'ljoxqyyw'
#input = 'flqrgnkx' # Testinput

def solve(maze):
    visited = set()
    groups = 0
    for r in range(128):
        for c in range(128):
            if maze[r][c] == '#':
                if (r, c) not in visited:
                    group = dfs_trace_group(maze, r, c)
                    visited.update(group)
                    groups += 1
    #return groups
    print(groups)

def dfs_trace_group(maze, r, c):
    def is_valid(r, c):
        if r >= 0 and c >= 0 and r < 128 and c < 128:
            return maze[r][c] == '#'

    def generate_moves(pos):
        r, c = pos
        new_positions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        return [newpos for newpos in new_positions if is_valid(*newpos)]

    visited, queue = set(), [(r, c)]
    while queue:
        pos = queue.pop()
        if pos not in visited:
            visited.add(pos)
            queue.extend(generate_moves(pos))
    return visited



total = []
total2 = {}

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
    v = []

    for c in solution:
        w = w + bin(c)

    for char in w:
        if char == '1':
            v.append('#')
        else:
            v.append('.')

    total.append(v)

solve(total)
#print(groups)

#for k in range(len(total)):
#    print(''.join(total[k]))
