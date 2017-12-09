# Advent of Code 2017
# Day 03; Puzzle 06

t = 1
x = 0
y = 0
v = 0

d = {
    '0,0': 1
}

while v < 277678:

    s = int(t / 2)

    for i in range(s):
        if s % 2 == 0:
            if s == t / 2:
                x = x - 1
            else:
                y = y -1
        else:
            if s == t / 2:
                x = x + 1
            else:
                y = y + 1

        l = str(x)+","+str(y)

        w = 0

        for i in range(x - 1,x + 2, 1):
            for j in range(y - 1,y + 2, 1):
                m = str(i)+","+str(j)
                w += d.get(m, 0)
        v = max(1,w)

        d[l] = v

    t += 1

print(v)
