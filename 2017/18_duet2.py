#!/usr/bin/env python


# Advent of Code 2017 - 18 Duet


def RepsInt(x, d):
    try:
        int(x) % 1 == 0
        r = int(x)
    except:
        r = int(d.get(x, 0))
    return r


def process(pid, k, input, register, queue, sent):
    if len(input[k]) == 3:
        r = RepsInt(input[k][1], register[pid])
        s = RepsInt(input[k][2], register[pid])

    if input[k][0] == "set":
        register[pid][input[k][1]] = s
        k += 1
    elif input[k][0] == "mul":
        register[pid][input[k][1]] = r * s
        k += 1
    elif input[k][0] == "jgz":
        if r > 0:
            k += s
        else:
            k += 1
    elif input[k][0] == "add":
        register[pid][input[k][1]] = r + s
        k += 1
    elif input[k][0] == "mod":
        register[pid][input[k][1]] = r % s
        k += 1
    elif input[k][0] == "snd":
        if pid == 0:
            queue[1].append(register[0].get(input[k][1]))
        else:
            queue[0].append(register[1].get(input[k][1]))
            sent += 1
        k += 1
    elif input[k][0] == "rcv":
        if len(queue[pid]) > 0:
            register[pid][input[k][1]] = queue[pid].pop(0)
            k += 1

    return pid, k, register, queue, sent


if __name__ == "__main__":

    input = []
    queue = [[], []]
    p = [0, 0]
    register = [{'p': 0}, {'p': 1}]
    sent = 0

    with open('18_input.txt') as f:
        for line in f.readlines():
            input.append(line.strip('\n').split(' '))

    while True:
        for pid in range(len(p)):
            if p[pid] > len(input):
                exit()
            else:
                k = p[pid]

            r = process(pid, k, input, register, queue, sent)
            print(sent)
            p[r[0]] = r[1]
            register = r[2]
            queue = r[3]
            sent = r[4]
