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
    for i, line in enumerate(lines):
        d, _, units = line.partition(" ")
        units = int(units)
        print(d, int(units))
        if d == "forward":
            x += units
        elif d == "up":
            y -= units
        elif d == "down":
            y += units
    print(x * y)


def b(lines):
    x, y, aim = 0, 0, 0
    for i, line in enumerate(lines):
        d, _, units = line.partition(" ")
        units = int(units)
        print(d, int(units))
        if d == "forward":
            x += units
            y += aim * units
        elif d == "up":
            aim -= units
        elif d == "down":
            aim += units
    print(x * y)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
