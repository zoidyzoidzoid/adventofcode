#!/usr/bin/env python3.6
import fileinput
from collections import *
from functools import *
from itertools import *
from math import *
from numpy import *

directions = ((0, -1), (-1, 0), (0, 1), (1, 0))

initial_step = [(1, 0), (-1, 0), (0, 1), (1, 0)]


def process(n):
    length = int(floor(sqrt(n)))
    if length % 2 != 1:
        length -= 1
    start = int((length - 1) / 2)
    pos = start, start
    num = length ** 2
    for index, direction in enumerate(directions):
        pos = pos[0] + initial_step[index][0], pos[1] + initial_step[index][1]
        num += 1
        if num == n:
            return abs(pos[0]) + abs(pos[1])
        for i in range(length):
            pos = pos[0] + direction[0], pos[1] + direction[1]
            num += 1
            if num == n:
                return abs(pos[0]) + abs(pos[1])


for line in fileinput.input():
    line = line.strip()
    print(process(int(line)))
