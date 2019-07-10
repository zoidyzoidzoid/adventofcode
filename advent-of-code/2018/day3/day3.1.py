#!/usr/bin/env python3
import fileinput
from collections import defaultdict


def process(lines):
    grid = defaultdict(str)
    for i, line in enumerate(lines):
        claim, line = line.lstrip("#").split(" @ ")
        coords, size = line.split(": ")
        x, y = coords.split(",")
        x_l, y_l = size.split("x")
        x, y = int(x), int(y)
        x_l, y_l = int(x_l), int(y_l)
        for i in range(x, x + x_l):
            for j in range(y, y + y_l):
                if grid[i, j] == '':
                    grid[i, j] = claim
                else:
                    grid[i, j] = 'X'

    result = 0
    for val in grid.values():
        if val == 'X':
            result += 1

    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


process(lines)
