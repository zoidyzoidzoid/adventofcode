#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def print_grid(grid, full=False):
    x_l = min((i[0] for i in grid.keys())) - 1
    y_l = min((i[1] for i in grid.keys())) - 1
    x_r = max((i[0] for i in grid.keys())) + 2
    y_r = max((i[1] for i in grid.keys())) + 2
    print()
    for y in range(y_l, y_r):
        line = '{:5d}: '.format(y)
        for x in range(x_l, x_r):
            line += grid.get((x, y), '.')
        if '|' in line or '~' in line or full:
            print(line)


def a(lines):
    return
    spring = 500, 0
    result = 0

    # init grid
    grid = {}
    grid[spring] = '+'
    for i, line in enumerate(lines):
        a, b = line.split(', ')
        if a.startswith('x'):
            _, _, x = a.partition('=')
            x = int(x)
            _, _, rng = b.partition('=')
            start, _, end = rng.partition('..')
            start = int(start)
            end = int(end)
            for y in range(start, end + 1):
                grid[x, y] = '#'
        elif a.startswith('y'):
            _, _, y = a.partition('=')
            y = int(y)
            _, _, rng = b.partition('=')
            start, _, end = rng.partition('..')
            start = int(start)
            end = int(end)
            for x in range(start, end + 1):
                grid[x, y] = '#'

    # process water
    y_l = min((i[1] for i in grid.keys()))
    y_r = max((i[1] for i in grid.keys())) - 1
    x_l = min((i[0] for i in grid.keys()))
    x_r = max((i[0] for i in grid.keys())) - 1


    def pour(x, y):
        res = 0
        if y > y_r or y < y_l:
            return res, (x, y)
        c = grid.get((x, y + 1), '.')
        if c in ('.', '|', '+'):
            if c == '.':
                grid[x, y + 1] = '|'
            return pour(x, y + 1)
        elif c == '~':
            y += 1
            l, r = x, x
            fall = False
            fs = []
            while grid.get((l - 1, y), '.') != '#':
                l = l - 1
                if grid.get((l, y + 1), '.') in ('.', '|'):
                    fall = True
                    fs.append((l, y))
                    break
            while grid.get((r + 1, y), '.') != '#':
                r = r + 1
                if grid.get((r, y + 1), '.') in ('.', '|'):
                    fall = True
                    fs.append((r, y))
                    break
            if fall:
                for x in range(l, r + 1):
                    grid[x, y] = '|'
                for f_x, f_y in fs:
                    r, loc = pour(f_x, f_y)
                    res += r
                return res, loc

            l, r = x, x
            while grid.get((l - 1, y), '.') != '#':
                l = l - 1
                if grid.get((l, y), '.') == '.':
                    break
            while grid.get((r + 1, y), '.') != '#':
                r = r + 1
                if grid.get((r, y), '.') == '.':
                    break
            if l != x and grid.get((l, y), '.') == '.':
                # print('l boop', l, y)
                grid[l, y] = '~'
                res = 1
            elif r != x and grid.get((r, y), '.') == '.':
                # print('r boop', r, y)
                grid[r, y] = '~'
                res = 1
            else:
                # print('stale above', x, y, grid.get((x, y), '.'))
                y = y-1
                l, r = x, x
                fall = False
                fs = []
                while grid.get((l - 1, y), '.') != '#':
                    l = l - 1
                    if grid.get((l, y + 1), '.') in ('.', '|'):
                        fall = True
                        fs.append((l, y))
                        break
                while grid.get((r + 1, y), '.') != '#':
                    r = r + 1
                    if grid.get((r, y + 1), '.') in ('.', '|'):
                        fall = True
                        fs.append((r, y))
                        break
                if fall:
                    for x in range(l, r + 1):
                        grid[x, y] = '|'
                    for f_x, f_y in fs:
                        r, loc = pour(f_x, f_y)
                        res += r
                    return res, loc
                else:
                    grid[x, y] = '~'
                    res += 1
        elif c == '#':
            grid[x, y] = '~'
            res = 1
        return res, (x, y)

    while True:
        res, loc = pour(500, 0)
        # print_grid(grid)
        if not res:
            break

    # print final grid
    print_grid(grid, full=True)

    y_l = min((i[1] for i, v in grid.items() if v == '#'))
    y_r = max((i[1] for i, v in grid.items() if v == '#'))
    print(sum(1 for i, v in grid.items() if v in ('~', '|') and i[1] >= y_l and i[1] <= y_r))


def b(lines):
    spring = 500, 0
    result = 0

    # init grid
    grid = {}
    grid[spring] = '+'
    for i, line in enumerate(lines):
        a, b = line.split(', ')
        if a.startswith('x'):
            _, _, x = a.partition('=')
            x = int(x)
            _, _, rng = b.partition('=')
            start, _, end = rng.partition('..')
            start = int(start)
            end = int(end)
            for y in range(start, end + 1):
                grid[x, y] = '#'
        elif a.startswith('y'):
            _, _, y = a.partition('=')
            y = int(y)
            _, _, rng = b.partition('=')
            start, _, end = rng.partition('..')
            start = int(start)
            end = int(end)
            for x in range(start, end + 1):
                grid[x, y] = '#'

    # process water
    y_l = min((i[1] for i in grid.keys()))
    y_r = max((i[1] for i in grid.keys())) - 1
    x_l = min((i[0] for i in grid.keys()))
    x_r = max((i[0] for i in grid.keys())) - 1


    def pour(x, y):
        res = 0
        if y > y_r or y < y_l:
            return res, (x, y)
        c = grid.get((x, y + 1), '.')
        if c in ('.', '|', '+'):
            if c == '.':
                grid[x, y + 1] = '|'
            return pour(x, y + 1)
        elif c == '~':
            y += 1
            l, r = x, x
            fall = False
            fs = []
            while grid.get((l - 1, y), '.') != '#':
                l = l - 1
                if grid.get((l, y + 1), '.') in ('.', '|'):
                    fall = True
                    fs.append((l, y))
                    break
            while grid.get((r + 1, y), '.') != '#':
                r = r + 1
                if grid.get((r, y + 1), '.') in ('.', '|'):
                    fall = True
                    fs.append((r, y))
                    break
            if fall:
                for x in range(l, r + 1):
                    grid[x, y] = '|'
                for f_x, f_y in fs:
                    r, loc = pour(f_x, f_y)
                    res += r
                return res, loc

            l, r = x, x
            while grid.get((l - 1, y), '.') != '#':
                l = l - 1
                if grid.get((l, y), '.') == '.':
                    break
            while grid.get((r + 1, y), '.') != '#':
                r = r + 1
                if grid.get((r, y), '.') == '.':
                    break
            if l != x and grid.get((l, y), '.') == '.':
                # print('l boop', l, y)
                grid[l, y] = '~'
                res = 1
            elif r != x and grid.get((r, y), '.') == '.':
                # print('r boop', r, y)
                grid[r, y] = '~'
                res = 1
            else:
                # print('stale above', x, y, grid.get((x, y), '.'))
                y = y-1
                l, r = x, x
                fall = False
                fs = []
                while grid.get((l - 1, y), '.') != '#':
                    l = l - 1
                    if grid.get((l, y + 1), '.') in ('.', '|'):
                        fall = True
                        fs.append((l, y))
                        break
                while grid.get((r + 1, y), '.') != '#':
                    r = r + 1
                    if grid.get((r, y + 1), '.') in ('.', '|'):
                        fall = True
                        fs.append((r, y))
                        break
                if fall:
                    for x in range(l, r + 1):
                        grid[x, y] = '|'
                    for f_x, f_y in fs:
                        r, loc = pour(f_x, f_y)
                        res += r
                    return res, loc
                else:
                    grid[x, y] = '~'
                    res += 1
        elif c == '#':
            grid[x, y] = '~'
            res = 1
        return res, (x, y)

    while True:
        res, loc = pour(500, 0)
        # print_grid(grid)
        if not res:
            break

    # print final grid
    print_grid(grid, full=True)

    y_l = min((i[1] for i, v in grid.items() if v == '#'))
    y_r = max((i[1] for i, v in grid.items() if v == '#'))
    print(sum(1 for i, v in grid.items() if v in ('~',) and i[1] >= y_l and i[1] <= y_r))


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
