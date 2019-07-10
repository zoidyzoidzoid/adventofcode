#!/usr/bin/env python3
import fileinput
from collections import defaultdict
from copy import deepcopy
from datetime import datetime

LEN = 50


def print_grid(grid, full=False):
    global LEN
    for y in range(LEN):
        line = '{:2d}: '.format(y)
        for x in range(LEN):
            line += grid[x, y]
        print(line)


SPLITS = (55,)

cache = None


def a(lines, minutes=10):
    global LEN
    LEN = len(lines[0])
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '.':
                grid[x, y] = 0
            elif c == '|':
                grid[x, y] = 1
            elif c == '#':
                grid[x, y] = 2

    # print('Initial state')
    # print_grid(grid)

    dirs = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )

    empty_counts = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
    }

    global cache
    if cache is None:
        cache = {}

    set_work = set()
    for y in range(LEN):
        for x in range(LEN):
            set_work.add((x, y))

    work = set_work.copy()
    new_grid = deepcopy(grid)
    replacements = defaultdict(int)

    minute = 0
    while minute < minutes:
        if minute % 10000 == 0:
            print('{1}: Minute {0} {2}/{3}'.format(minute, datetime.utcnow(), len(work), LEN * LEN))
            print(dict(replacements))
        # elif work:
        #     print('{1}: Minute {0} {2}/{3}'.format(minutes - (minute + 1), datetime.utcnow(), len(work), LEN * LEN))

        while work:
            x, y = work.pop()
            counts = empty_counts.copy()
            for d_x, d_y in dirs:
                if not 0 <= x + d_x < LEN:
                    continue
                if not 0 <= y + d_y < LEN:
                    continue
                counts[grid[x + d_x, y + d_y]] += 1

            if grid[x, y] == 0 and counts[1] >= 3:
                new_grid[x, y] = 1
            elif grid[x, y] == 1 and counts[2] >= 3:
                new_grid[x, y] = 2
            elif grid[x, y] == 2 and (counts[2] < 1 or counts[1] < 1):
                new_grid[x, y] = 0

        # End of frame, update state
        work = set_work.copy()
        old_grid = grid.copy()
        grid = new_grid.copy()
        new_grid = grid.copy()

        # Update and check cache
        for y in range(-1, LEN - 1):
            for x in range(-1, LEN - 1):
                for d_y in SPLITS:
                    d_x = d_y
                    if x + d_x > LEN + 4 or y + d_y > LEN + 4:
                        continue
                    if (x + 1, y + 1) not in work and (x + int(d_x / 2) - 1, y + int(d_y / 2) - 1) not in work:
                        continue
                    # print('Trying grid {0} by {0} at {1},{2}'.format(d, x, y))
                    keys, values = [], []
                    for j in range(y, y + d_y):
                        for i in range(x, x + d_x):
                            keys.append(old_grid.get((i, j), 3))
                            values.append(grid.get((i, j), 3))
                    key = tuple(keys)
                    value = tuple(values)
                    if key not in cache:
                        cache[key] = value, minute
                    if value in cache:
                        replacements[(d_x, d_y)] += 1
                        value, last_minute = cache[value]
                        diff = minute - last_minute + 1
                        if minute - last_minute > 1 and minute + diff < minutes:
                            while minute + (diff * 2) < minutes:
                                minute += diff
                        for c_y in range(y + 1, y + d_y - 1):
                            for c_x in range(x + 1, x + d_x - 1):
                                if (c_x, c_y) in work:
                                    new_grid[c_x, c_y] = int(value[((c_y - y) * d_x) + (c_x - x)])
                                    work.remove((c_x, c_y))
                        break

        minute += 1
        # print('After {} minutes'.format(i + 1))
        # print_grid(grid)

    # print('Final state')
    # print_grid(grid)

    ws = sum(1 for v in grid.values() if v == 1)
    lys = sum(1 for v in grid.values() if v == 2)
    result = ws * lys
    print('Woods:', ws,', lumberyards:', lys)
    print('Result:', result)
    return result


def b(lines):
    a(lines, minutes=1000000000)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
