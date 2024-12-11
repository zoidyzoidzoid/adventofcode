#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import sys
import math
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt
from time import time_ns


def a(lines):
    grid = {}
    pos_x, pos_y = 0, 0
    dir_x, dir_y = 0, -1
    next_dir = {
        (0, -1): (1, 0),
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
    }
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ".":
                continue
            grid[x, y] = c
            if c == "^":
                pos_x, pos_y = x, y
    mx_x, mx_y = len(lines[0]), len(lines)
    visited = set()
    def print_grid(data):
        print("=" * mx_x)
        print("=" * mx_x)
        for j in range(mx_y):
            for i in range(mx_x):
                if (i, j) in visited:
                    print("X", end="")
                else:
                    print(data.get((i, j), "."), end="")
            print()
        print("=" * mx_x)
        print("=" * mx_x)
    while 0 <= pos_x  < mx_x and 0 <= pos_y < mx_y:
        visited.add((pos_x, pos_y))
        # print_grid(grid)
        if grid.get((pos_x + dir_x, pos_y + dir_y), ".") == "#":
            dir_x, dir_y = next_dir[(dir_x, dir_y)]
        else:
            pos_x, pos_y = pos_x + dir_x, pos_y + dir_y
    print_grid(grid)
    result = len(visited)
    print(result)


def b(lines):
    grid = {}
    pos_x, pos_y = 0, 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ".":
                continue
            grid[x, y] = c
            if c == "^":
                pos_x, pos_y = x, y
    next_dir = {
        (0, -1): (1, 0),
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
    }
    dir_sym2 = {
        (0, -1): "|",
        (1, 0): "-",
        (0, 1): "|",
        (-1, 0): "-",
    }
    dir_sym = {
        (0, -1): "^",
        (1, 0): ">",
        (0, 1): "v",
        (-1, 0): "<",
    }
    result = set()
    mx_x, mx_y = len(lines[0]), len(lines)
    def has_loop(grid, pos_x, pos_y, dir_x, dir_y, extra_x=None, extra_y=None, visited=None, extra_obstacle=False, turns=0):
        def print_grid(data):
            print("=" * mx_x)
            for j in range(mx_y):
                for i in range(mx_x):
                    if (i, j) == (pos_x, pos_y):
                        print(dir_sym[dir_x, dir_y], end="")
                    elif (i, j) == (extra_x, extra_y):
                        print("O", end="")
                    else:
                        print(data.get((i, j), "."), end="")
                print()
            print("=" * mx_x)
        while 0 <= pos_x  < mx_x and 0 <= pos_y < mx_y:
            if grid.get((pos_x + dir_x, pos_y + dir_y), ".") == "#":
                grid[pos_x, pos_y] = "+"
                dir_x, dir_y = next_dir[(dir_x, dir_y)]
                if extra_obstacle is True:
                    turns += 1
                    if turns > 5:
                        return
            else:
                # She can walk forward here
                # so let's check that if she couldn't walk forward here, she would get stuck in a loop
                # We can copy the grid, add an obstacle, then check if she gets stuck in a loop
                # We can see if she's stuck in a loop, if she's turned in this position before in the same direction?
                if extra_obstacle is False:
                    grid2 = grid.copy()
                    grid2[pos_x + dir_x, pos_y + dir_y] = "#"
                    has_loop(grid2, pos_x, pos_y, dir_x, dir_y, extra_x=pos_x + dir_x, extra_y=pos_y + dir_y, visited=visited.copy(), extra_obstacle=True)
                elif (pos_x, pos_y, dir_x, dir_y) in visited:
                    nonlocal result
                    result.add((extra_x, extra_y))
                    print_grid(grid)
                    return
                visited.add((pos_x, pos_y, dir_x, dir_y))
                if grid.get((pos_x, pos_y), ".") != ".":
                    grid[pos_x, pos_y] = "+"
                else:
                    grid[pos_x, pos_y] = dir_sym2[dir_x, dir_y]
                pos_x, pos_y = pos_x + dir_x, pos_y + dir_y
    has_loop(grid, pos_x, pos_y, 0, -1, visited=set())
    print(len(result))


lines = []
for line in fileinput.input():
    lines.append(line.strip())


class Timer(object):
    def __init__(self, description):
        self.description = description
    def __enter__(self):
        self.start = time_ns()
    def __exit__(self, type, value, traceback):
        self.end = time_ns()
        d = self.end - self.start
        if d > 1_000_000_000:
            d /= 1_000_000_000
            u = "s"
        elif d > 1_000_000:
            d /= 1_000_000
            u = "ms"
        elif d > 1_000:
            d /= 1_000
            u = "µs"
        else:
            u = "ns"
        print("{}: {} {}".format(self.description, d, u))


def main():
    # with Timer("Part 1"):
    #     a(lines)

    with Timer("Part 2"):
        b(lines)


if __name__ == "__main__":
    main()
