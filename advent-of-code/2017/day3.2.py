#!/usr/bin/env python3.6
import fileinput
from collections import *
from functools import *
from itertools import *
from math import *
from numpy import *

directions = ((0, -1), (-1, 0), (0, 1), (1, 0))

initial_step = [(1, 0), (-1, 0), (0, 1), (1, 0)]


def calc_val(grid, x, y):
    total = 0
    for d_x, d_y in (
             (1, 1), (1, 0), (1, -1),
             (0, 1), (0, -1),
             (-1, 1), (-1, 0), (-1, -1)):
        total += grid[((x + d_x), (y + d_y))]
    return total


def process(n):
    grid = defaultdict(int)
    pos_x, pos_y = 0, 0
    grid[pos_x, pos_y] = 1
    length = 1
    while True:
        for index, d in enumerate(directions):
            d_x, d_y = d
            pos_x, pos_y = pos_x + initial_step[index][0], pos_y + initial_step[index][1]
            num = calc_val(grid, pos_x, pos_y)
            grid[pos_x, pos_y] = num
            if num > n:
                return num

            for i in range(length):
                pos_x, pos_y = pos_x + d_x, pos_y + d_y
                num = calc_val(grid, pos_x, pos_y)
                grid[pos_x, pos_y] = num
                if num > n:
                    return num
        length += 2

for line in fileinput.input():
    line = line.strip()
    print(process(int(line)))
