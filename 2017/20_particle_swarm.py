#!/usr/bin/env python


# Advent of Code 2017 - 20 Particle Swarm

# TODO: Lent part 2, need to comprehend it some more

class Particle(object):

    def __init__(self, inputstr):
        x, v, a = [tuple(map(int, re.findall(r'[-\d]+', x))) for x in inputstr.split()]
        self.x, self.y, self.z = x
        self.vx, self.vy, self.vz = v
        self.ax, self.ay, self.az = a

    def move(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def position(self):
        return self.x, self.y, self.z

    def estimate_position(self, t):
        x = self.x + self.vx * t + 0.5 * self.ax * (t ** 2)
        y = self.y + self.vy * t + 0.5 * self.ay * (t ** 2)
        z = self.z + self.vz * t + 0.5 * self.az * (t ** 2)
        return x, y, z

    def manhattan_distance(self, t):
        x, y, z = self.estimate_position(t)
        return abs(x) + abs(y) + abs(z)

def part1(input):
    for item in input:
        acceleration.append(abs(item[2][0]) + abs(item[2][1]) + abs(item[2][2]))

    print("Part 1: " + str(acceleration.index(min(acceleration))))


def part2(t):
    from collections import defaultdict
    f = open('20_input.txt')
    particles = f.readlines()
    particles = [Particle(p) for p in particles]
    for t in range(t):
        n = defaultdict(int)
        for particle in particles:
            particle.move()
            n[particle.position()] += 1
        particles = [p for p in particles if n[p.position()] == 1]
    print("Part 2: " + str(len(particles)))

if __name__ == '__main__':

    import re

    input, acceleration, distances = [], [], []

    with open('20_input.txt') as f:
        for line in f.readlines():
            r = re.match(r'p=<([-]*\d+),([-]*\d+),([-]*\d+)>, v=<([-]*\d+),([-]*\d+),([-]*\d+)>, a=<([-]*\d+),([-]*\d+),([-]*\d+)>', line)
            u = []
            for i in range(3):
                s = []
                for j in range(3):
                    t = i * 3 + (j + 1)
                    s.append(int(r.group(t)))
                u.append(s)
            input.append(u)

    part1(input)
    part2(10000)
