#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def process(lines):
    result = None
    c2 = 0
    c3 = 0
    for i, line in enumerate(lines[:-1]):
        for line2 in lines[i + 1:]:
            diffs = 0
            for x, c in enumerate(line):
                if c != line2[x]:
                    diffs += 1
                if diffs > 1:
                    break
            if diffs == 1:
                s = ''
                for x, c in enumerate(line):
                    if c == line2[x]:
                        s += c
                print(s)




lines = []
for line in fileinput.input():
    lines.append(line.strip())


process(lines)
