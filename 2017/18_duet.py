#!/usr/bin/env python


# Advent of Code 2017 - 18 Duet

# TODO: Integrate solution 1 and 2.

def RepsInt(x, d):
    try:
        int(x) % 1 == 0
        r = int(x)
    except:
        r = int(d.get(x, 0))
    return r


if __name__ == '__main__':

    input = []
    dic = {}
    # snd = []

    with open('18_input.txt') as f:
        for line in f.readlines():
            input.append(line.strip('\n').split(' '))

    k = 0
    while k in range(len(input)):
        if len(input[k]) == 3:
            r = RepsInt(input[k][1], dic)
            s = RepsInt(input[k][2], dic)

        if input[k][0] == "set":
            dic[input[k][1]] = s
            k += 1
        elif input[k][0] == "mul":
            dic[input[k][1]] = r * s
            k += 1
        elif input[k][0] == "jgz":
            if r > 0:
                k += s
            else:
                k += 1
        elif input[k][0] == "add":
            dic[input[k][1]] = r + s
            k += 1
        elif input[k][0] == "mod":
            dic[input[k][1]] = r % s
            k += 1
        elif input[k][0] == "snd":
            sound = dic.get(input[k][1])
            k += 1
        elif input[k][0] == "rcv":
            if input[k][1] != 0:
                print(sound)
                break
            k += 1

        # print(k)
        # print(dic)
        # print(snd)
