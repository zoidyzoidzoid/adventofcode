#!/usr/bin/env python3
# coding: utf-8
from collections import Counter
from sys import maxsize


def process(inp):
    particles = {}
    for index, line in enumerate(inp):
        p = []
        line = line.split(', ')
        for chunk in line:
            p.extend(map(int, chunk[3:-1].split(',')))
        particles[index] = p
    c = Counter()
    while len(c) < 1 or c.most_common(1)[0][1] < 5000:
        closest = None
        r = maxsize
        for index, particle in particles.items():
            curr_r = sum(map(abs, particle[:3]))
            if curr_r < r:
                closest = index
                r = curr_r
        c[closest] += 1

        for particle in particles.values():
            particle[3] += particle[6]
            particle[4] += particle[7]
            particle[5] += particle[8]
            particle[0] += particle[3]
            particle[1] += particle[4]
            particle[2] += particle[5]

    return c.most_common(3)


print(process(open('day20.txt').read().strip().split('\n')))
