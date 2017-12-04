# Advent of Code 2017
# Day 03; Puzzle 05

def moves(value):

    total = value
    count = 0
    step = 0

    while total > step:
        count = count + 1
        step = int(count/2)
        total = total - max(1, step)

        if total == 0:
            steps = step
        elif total > step/2:
            steps = total
        else:
            steps = step - total

    print(steps)

moves(277678)
