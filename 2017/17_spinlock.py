#!/usr/bin/env python

# Advent of Code 2017 = 17 Spinlock

input = 382
#input = 3 #Test

memory = [0]

def circular_memory(steps, length):
    for step in range(1, steps):
        memory.insert((memory.index(step - 1) + length) % len(memory) + 1, step)
        if step % 100000 == 0:
            print(step)
    return memory

def what_is(steps, length, index):
    insert_index = 0
    for step in range(steps):
        #memory.insert(insert_index, step)
        insert_index = (insert_index + length) % max(1, step+1) + 1
        if insert_index == index:
            value = step + 1
    return value

memory = circular_memory(2018, input)
print("Part 1: " + str(memory[memory.index(2017) + 1]))

print("Part 2: " + str(what_is(50000000, input, 1)))


# memory = [0]
# print(memory)
# print(input % len(memory))
# print(int(input / len(memory)))
#
# memory = [0, 1]
# print(memory)
# print(input % len(memory))
# print(int(input / len(memory)))
#
# memory = [0, 2, 1]
# print(memory)
# print(input % len(memory))
# print(int(input / len(memory)))
#
# memory = [0, 2, 3, 1]
# print(memory)
# print(input % len(memory))
# print(int(input / len(memory)))
#
# memory = [0, 2, 4, 3, 1]
# print(memory)
# print(input % len(memory))
# print(int(input / len(memory)))
#
# memory = [0, 5, 2, 4, 3, 1]
# print(memory)
# print(input % len(memory))
# print(int(input / len(memory)))
#
# memory = [0, 5, 2, 4, 3, 6, 1]
# print(memory)
# print(input % len(memory))
# print(int(input / len(memory)))
