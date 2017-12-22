#!/usr/bin/env python3
# coding: utf-8


def process(inp, iterations=10000):
    grid = {}
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            x = -(((len(row) - 1)  / 2) - j)
            y = -(((len(row) - 1)  / 2) - i)
            x = int(x)
            y = int(y)
            if c == '#':
                grid[x, y] = c
    pos = 0, 0
    dir_x, dir_y = (0, -1)
    count = 0
    for i in range(iterations):
        if pos not in grid:
            dir_x, dir_y = dir_y, -dir_x
            grid[pos] = '#'
            count += 1
            pos = pos[0] + dir_x, pos[1] + dir_y
        else:
            dir_x, dir_y = -dir_y, dir_x
            del grid[pos]
            pos = pos[0] + dir_x, pos[1] + dir_y
    print(count)


process("""..#
#..
...""".split('\n'))
process(open('day22.txt').read().strip().split('\n'))
