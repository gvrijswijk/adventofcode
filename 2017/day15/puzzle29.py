# Advent of Code 2017
# Day 15; Puzzle 29 & 30
# Dueling Generators - Part 1 & 2

#borrowed from https://github.com/orez-/Advent-of-Code-2017/blob/master/day15/original.py

def do_while(fn):
    yield
    while fn():
        yield


gen_a, gen_b = 16807, 48271
div = 2147483647

run = 40000000
run2 = 5

mask = 2 ** 16 - 1

a, b = 116, 299 #real
#a, b = 65, 8921 #test

c = 0

for i in range(run):
    a *= gen_a
    a %= div
    b *= gen_b
    b %= div
    if a & mask == b & mask: # NOTE: how does this masking work
        c += 1

print(c)

a, b = 116, 299 #real
#a, b = 65, 8921 #test

c = 0

for i in range(run2):
    for _ in do_while(lambda: a % 4 != 0): # TODO: Read up on lambda + does it matter when input % 4 =0 (ie input 116 %4 =0)
        a *= gen_a
        a %= div
        print(a)
    for _ in do_while(lambda: b % 8 != 0):
        b *= gen_b
        b %= div
        print(b)
    if a & mask == b & mask:
        c += 1

print(c)
