#!/usr/bin/env python


# Advent of Code 2017 - 19 A Series Of Tubes


def part1(y, x, input, direction, output):
    if input[y][x] == '+':
        if direction[0] == 'y':
            if input[y][x + 1] == '-':
                direction = 'x+'
                x +=1
            else:
                direction = 'x-'
                x -= 1
        else:
            if input[y + 1][x] == '|':
                direction = 'y+'
                y += 1
            else:
                direction = 'y-'
                y -= 1
    elif input[y][x].isalnum():
        output.append(input[y][x])
        if direction == 'x+':
            x += 1
        elif direction == 'x-':
            x -= 1
        elif direction == 'y+':
            y += 1
        elif direction == 'y-':
            y -= 1
    else:
        if direction[0] == 'y':
            if direction[1] == '+':
                y += 1
            else:
                y -= 1
        else:
            if direction[1] == '+':
                x += 1
            else:
                x -= 1

    return y, x, direction, output


if __name__ == "__main__":

    input, output, locations = [], [], []

    with open('19_input.txt') as f:
        for line in f.readlines():
            input.append(line.strip('\n'))

    y = 0
    x = input[y].index('|')
    direction = 'y+'
    t = 0
    while True:
        locations.append(str(y) + ", " + str(x) + ", " + input[y][x])
        if x < 0 or y < 0:
            break
        try:
            r = part1(y, x, input, direction, output)
            y = r[0]
            x = r[1]

            direction = r[2]
            output = r[3]

        except:

            break
        t += 1
    print(len(locations))
    print(''.join(output))

    o = open('19_output.txt', 'a')
    for item in locations:
        o.write(item)
        o.write('\n')
    o.close
