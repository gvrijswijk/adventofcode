#!/usr/bin/env python

# Advent of Code 2017 - 01 Inverse Captcha

import time

time_mp0 = time.time()

def captcha(x):
    c = 0
    l = len(x)
    for i in range(l):
        if x[i] == x[i - 1]:
            c += int(x[i])
    return c

def circular_captcha(x):
    c = 0
    l = int(len(x)/2)
    for i in range(l):
        if x[i] == x[i + l]:
            c += 2 * int(x[i])
    return c

if __name__ == "__main__":

    with open('01_input.txt') as f:
        input = f.read().strip()

time_mp1 = time.time()

print("Part 1: " + str(captcha(input)))

time_mp2 = time.time()

print("Part 2: " + str(circular_captcha(input)))

time_mp3 = time.time()

print("Part 1: %.3f" % (time_mp2 - time_mp1))
print("Part 2: %.3f" % (time_mp3 - time_mp2))
print("Total:  %.3f" % (time.time() - time_mp0))
