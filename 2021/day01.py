def Input(day, year=2021):
    directory = "inputs" 
    filename = directory + '/input{}.txt'.format(day)
    return open(filename)

i = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
i = [int(e) for e in Input('01').readlines()]
o = [1 if e[0] > e[1] else 0 for e in list(zip(i[1:], i[:-1]))]

print(sum(o))

i = [sum(e) for e in list(zip(i[2:], i[1:], i))]
o = [1 if e[0] > e[1] else 0 for e in list(zip(i[1:], i[:-1]))]

print(sum(o))
