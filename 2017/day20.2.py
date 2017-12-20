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

        for i, p1 in list(particles.items()):
            match = False
            for j, p2 in list(particles.items()):
                if i == j:
                    continue
                if all(p1[k] == p2[k] for k in range(3)):
                    match = True
                    del particles[j]
            if match:
                del particles[i]

    print(c.most_common(3))
    return len(particles)


print(process(open('day20.txt').read().strip().split('\n')))
