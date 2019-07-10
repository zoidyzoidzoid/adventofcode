#!/usr/bin/env python3
import fileinput
from collections import defaultdict


def process(lines):
    grid = defaultdict(str)
    needed = defaultdict(int)
    found = defaultdict(int)
    for i, line in enumerate(lines):
        claim, line = line.lstrip("#").split(" @ ")
        coords, size = line.split(": ")
        x, y = coords.split(",")
        x_l, y_l = size.split("x")
        x, y = int(x), int(y)
        x_l, y_l = int(x_l), int(y_l)
        needed[claim] = x_l * y_l
        for i in range(x, x + x_l):
            for j in range(y, y + y_l):
                if grid[i, j] == '':
                    grid[i, j] = claim
                else:
                    grid[i, j] = 'X'
    for val in grid.values():
        found[val] += 1
    for k, v in needed.items():
        if found[k] == v:
            print(k)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


process(lines)
