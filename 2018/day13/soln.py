#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def a(lines):
    return
    grid = dict()
    ints = dict()
    intersections = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ' ':
                continue
            elif c in ('+', '/', '\\'):
                intersections[(x, y)] = c
            elif c in ('<', '>', '^', 'v'):
                ints[x, y] = 0
            grid[x, y] = c
    print(grid)

    dirs = {
        '<': (-1, 0),
        '>': (+1, 0),
        '^': (0, -1),
        'v': (0, +1),
    }
    og = {
        '^': '|',
        'v': '|',
        '>': '-',
        '<': '-',
    }
    dirs_l = {
        (-1, 0): '<',
        (+1, 0): '>',
        (0, -1): '^',
        (0, +1): 'v',
    }
    int_states = [
        'LEFT', 'STRAIGHT', 'RIGHT'
    ]

    def left(x, y):
        return y, -x

    def straight(x, y):
        return x, y

    def right(x, y):
        return -y, x

    rots = {
        'LEFT':     left,
        'STRAIGHT': straight,
        'RIGHT':    right,
    }

    x_l = -1
    y_l = -1
    x_r = max((i[0] for i in grid.keys())) + 1
    y_r = max((i[1] for i in grid.keys())) + 1
    for y in range(y_l, y_r):
        for x in range(x_l, x_r):
            print(grid.get((x, y), ' '), end='')
        print()

    original_grid = grid.copy()

    result = None
    crash = False
    while not crash:
        new_grid = grid.copy()
        for x, y in sorted(grid, key=lambda x: x[1]):
            c = grid[x, y]
            if c in dirs:
                d_x, d_y = dirs[c]
                n_x, n_y = x + d_x, y + d_y
                print(grid[x, y])
                print(grid[n_x, n_y])
                n_c = grid[n_x, n_y]
                ints[n_x, n_y] = ints.pop((x, y))
                if new_grid[n_x, n_y] in og:
                    result = n_x, n_y
                    crash = True
                    break
                if n_c == '+':
                    rot = int_states[ints[n_x, n_y]]
                    ints[n_x, n_y] = (ints[n_x, n_y] + 1) % 3
                    if (x, y) in intersections:
                        new_grid[x, y] = '+'
                    else:
                        new_grid[x, y] = og[c]
                    new_grid[n_x, n_y] = dirs_l[rots[rot](d_x, d_y)]
                elif n_c == '\\':
                    if (x, y) in intersections:
                        new_grid[x, y] = '+'
                    elif c == '>':
                        new_grid[x, y] = '-'
                    elif c == '^':
                        new_grid[x, y] = '|'
                    elif c == '<':
                        new_grid[x, y] = '-'
                    elif c == 'v':
                        new_grid[x, y] = '|'
                    if c == '>':
                        new_grid[n_x, n_y] = 'v'
                    elif c == '^':
                        new_grid[n_x, n_y] = '<'
                    elif c == '<':
                        new_grid[n_x, n_y] = '^'
                    elif c == 'v':
                        new_grid[n_x, n_y] = '>'
                elif n_c == '/':
                    if (x, y) in intersections:
                        new_grid[x, y] = '+'
                    elif c == '>':
                        new_grid[x, y] = '-'
                    elif c == '^':
                        new_grid[x, y] = '|'
                    elif c == '<':
                        new_grid[x, y] = '-'
                    elif c == 'v':
                        new_grid[x, y] = '|'
                    if c == '>':
                        new_grid[n_x, n_y] = '^'
                    elif c == '^':
                        new_grid[n_x, n_y] = '>'
                    elif c == '<':
                        new_grid[n_x, n_y] = 'v'
                    elif c == 'v':
                        new_grid[n_x, n_y] = '<'
                else:
                    if (x, y) in intersections:
                        new_grid[x, y] = intersections[(x, y)]
                    else:
                        new_grid[x, y] = og[c]
                    new_grid[n_x, n_y] = c
        grid = new_grid

        # for y in range(y_l, y_r):
        #     print('{:3d}: '.format(y), end='')
        #     for x in range(x_l, x_r):
        #         print(grid.get((x, y), ' '), end='')
        #     print()

    print(result)


def b(lines):
    grid = dict()
    ints = dict()
    intersections = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ' ':
                continue
            elif c in ('+', '/', '\\'):
                intersections[(x, y)] = c
            elif c in ('<', '>', '^', 'v'):
                ints[x, y] = 0
            grid[x, y] = c
    print(grid)

    dirs = {
        '<': (-1, 0),
        '>': (+1, 0),
        '^': (0, -1),
        'v': (0, +1),
    }
    og = {
        '^': '|',
        'v': '|',
        '>': '-',
        '<': '-',
    }
    dirs_l = {
        (-1, 0): '<',
        (+1, 0): '>',
        (0, -1): '^',
        (0, +1): 'v',
    }
    int_states = [
        'LEFT', 'STRAIGHT', 'RIGHT'
    ]

    def left(x, y):
        return y, -x

    def straight(x, y):
        return x, y

    def right(x, y):
        return -y, x

    rots = {
        'LEFT':     left,
        'STRAIGHT': straight,
        'RIGHT':    right,
    }

    x_l = -1
    y_l = -1
    x_r = max((i[0] for i in grid.keys())) + 1
    y_r = max((i[1] for i in grid.keys())) + 1
    for y in range(y_l, y_r):
        for x in range(x_l, x_r):
            print(grid.get((x, y), ' '), end='')
        print()

    original_grid = grid.copy()
    for k, v in original_grid.items():
        x, y = k
        if v in ('<', '>'):
            original_grid[x, y] = '-'
        elif v in ('^', 'v'):
            original_grid[x, y] = '|'

    for y in range(y_l, y_r):
        for x in range(x_l, x_r):
            print(original_grid.get((x, y), ' '), end='')
        print()

    result = None
    o_c = None
    while True:
        new_grid = grid.copy()
        for x, y in sorted(grid, key=lambda x: x[1]):
            c = grid[x, y]
            if c in dirs:
                d_x, d_y = dirs[c]
                n_x, n_y = x + d_x, y + d_y
                n_c = grid[n_x, n_y]
                ints[n_x, n_y] = ints.pop((x, y))
                if new_grid[n_x, n_y] in og:
                    print('Crash!', new_grid[x, y], new_grid[n_x, n_y], x, y, n_x, n_y)
                    new_grid[x, y] = original_grid[x, y]
                    new_grid[n_x, n_y] = original_grid[n_x, n_y]
                    grid[x, y] = original_grid[x, y]
                    grid[n_x, n_y] = original_grid[n_x, n_y]
                    continue
                new_grid[x, y] = original_grid[x, y]
                if n_c == '+':
                    rot = int_states[ints[n_x, n_y]]
                    ints[n_x, n_y] = (ints[n_x, n_y] + 1) % 3
                    new_grid[n_x, n_y] = dirs_l[rots[rot](d_x, d_y)]
                elif n_c == '\\':
                    if c == '>':
                        new_grid[n_x, n_y] = 'v'
                    elif c == '^':
                        new_grid[n_x, n_y] = '<'
                    elif c == '<':
                        new_grid[n_x, n_y] = '^'
                    elif c == 'v':
                        new_grid[n_x, n_y] = '>'
                elif n_c == '/':
                    if c == '>':
                        new_grid[n_x, n_y] = '^'
                    elif c == '^':
                        new_grid[n_x, n_y] = '>'
                    elif c == '<':
                        new_grid[n_x, n_y] = 'v'
                    elif c == 'v':
                        new_grid[n_x, n_y] = '<'
                else:
                    new_grid[n_x, n_y] = c

        grid = new_grid

        # print(chr(27) + "[2J")
        # for y in range(35, 45):
        #     print('{:3d}: '.format(y), end='')
        #     for x in range(10, 20):
        #         print(grid.get((x, y), ' '), end='')
        #     print()
        # print()

        # print(chr(27) + "[2J")
        # for y in range(y_l, y_r):
        #     print('{:3d}: '.format(y), end='')
        #     for x in range(x_l, x_r):
        #         print(grid.get((x, y), ' '), end='')
        #     print()

        c = 0
        for k, v in grid.items():
            x, y = k
            if v in og:
                if c == 0:
                    result = x, y
                c += 1
        if c != o_c:
            o_c = c
            print("Count changed to", o_c)
        if c == 16:
            break
        if c == 1:
            break

    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip('\n'))


a(lines)
b(lines)
