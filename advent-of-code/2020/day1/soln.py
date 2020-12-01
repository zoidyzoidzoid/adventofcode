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
    lines = [int(i) for i in lines]
    for i, x in enumerate(lines):
        for _, y in enumerate(lines[i+1:]):
            if x + y == 2020:
                return x * y

def b(lines):
    lines = [int(i) for i in lines]
    for i, x in enumerate(lines):
        for j, y in enumerate(lines[i+1:]):
            for k, z in enumerate(lines[j+1:]):
                if x + y + z == 2020:
                    return x * y * z



lines = []
for line in fileinput.input():
    lines.append(line.strip())


print(a(lines))
print(b(lines))
