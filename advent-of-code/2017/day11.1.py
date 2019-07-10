#!/usr/bin/env python3
# coding: utf-8
import fileinput

def process(inp):
    directions = {
        'n': (1, -1, 0),
        'nw': (0, -1, 1),
        'ne': (1, 0, -1),
        's': (-1, 1, 0),
        'sw': (-1, 0, 1),
        'se': (0, 1, -1)
    }
    pos = 0, 0, 0
    for step in inp:
        pos = tuple(pos[i] + directions[step][i] for i, _ in enumerate(pos))
    print(pos)
    print(sum(abs(x) for x in pos) / 2)


process('ne,ne,ne'.split(','))
process('ne,ne,sw,sw'.split(','))
process('ne,ne,s,s'.split(','))
process('se,sw,se,sw,sw'.split(','))


for line in fileinput.input():
    print(process(line.strip().split(',')))
