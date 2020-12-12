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


def a(lines):
    x, y = 0, 0
    d_x, d_y = 1, 0
    for i, line in enumerate(lines):
        cmd, arg = line[0], line[1:]
        arg = int(arg)
        # print(cmd, arg)
        if cmd == 'N':
            y += arg
        elif cmd == 'S':
            y -= arg
        elif cmd == 'W':
            x -= arg
        elif cmd == 'E':
            x += arg
        elif cmd == 'L':
            for _ in range(arg // 90):
                d_x, d_y = -d_y, d_x
        elif cmd == 'R':
            for _ in range(arg // 90):
                d_x, d_y = d_y, -d_x
        elif cmd == 'F':
            x, y = x + (d_x * arg), y + (d_y * arg)
        else:
            raise SystemError('Unsupported command: {}'.format(cmd))
    print(abs(x) + abs(y))


def b(lines):
    x, y = 0, 0
    w_x, w_y = 10, 1
    d_x, d_y = 1, -1
    for i, line in enumerate(lines):
        cmd, arg = line[0], line[1:]
        arg = int(arg)
        # print(cmd, arg)
        if cmd == 'N':
            w_y += arg
        elif cmd == 'S':
            w_y -= arg
        elif cmd == 'W':
            w_x -= arg
        elif cmd == 'E':
            w_x += arg
        elif cmd == 'L':
            for _ in range(arg // 90):
                w_x, w_y = -w_y, w_x
        elif cmd == 'R':
            for _ in range(arg // 90):
                w_x, w_y = w_y, -w_x
        elif cmd == 'F':
            x, y = x + (arg * w_x), y + (arg * w_y)
        else:
            raise SystemError('Unsupported command: {}'.format(cmd))
        # print('Ship:', x, y)
        # print('Waypoint:', w_x, w_y)
        # print('=' * 20)
    print(abs(x) + abs(y))


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
