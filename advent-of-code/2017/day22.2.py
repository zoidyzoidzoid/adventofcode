#!/usr/bin/env python3
# coding: utf-8


def process(inp, iterations=10000000):
    grid = {}
    for i, row in enumerate(inp):
        for j, c in enumerate(row):
            x = -(((len(row) - 1)  / 2) - j)
            y = -(((len(row) - 1)  / 2) - i)
            x = int(x)
            y = int(y)
            if c == '#':
                grid[x, y] = c
    pos_x, pos_y = 0, 0
    dir_x, dir_y = (0, -1)
    count = 0
    for i in range(iterations):
        c = grid.get((pos_x, pos_y), '.')
        if c == '.':
            dir_x, dir_y = dir_y, -dir_x
            grid[pos_x, pos_y] = 'W'
            pos_x, pos_y = pos_x + dir_x, pos_y + dir_y
        elif c == 'W':
            count += 1
            grid[pos_x, pos_y] = '#'
            pos_x, pos_y = pos_x + dir_x, pos_y + dir_y
        elif c == '#':
            grid[pos_x, pos_y] = 'F'
            dir_x, dir_y = -dir_y, dir_x
            pos_x, pos_y = pos_x + dir_x, pos_y + dir_y
        else:
            dir_x, dir_y = -dir_x, -dir_y
            del grid[pos_x, pos_y]
            pos_x, pos_y = pos_x + dir_x, pos_y + dir_y
    print(count)


# process("""..#
# #..
# ...""".split('\n'))

process(open('day22.txt').read().strip().split('\n'))
