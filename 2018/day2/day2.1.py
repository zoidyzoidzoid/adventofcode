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
    for line in lines:
        if result is None:
            result = 1
        c = Counter(line)
        print(line)
        print(c)
        s2, s3 = False, False
        for key, value in c.items():
            if value == 2:
                s2 = True
            elif value == 3:
                s3 = True
        if s3:
            print("Found 3")
            c3 += 1
        if s2:
            print("Found 2")
            c2 += 1
    print(c2)
    print(c3)
    result *= (c2 * c3)

    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


process(lines)
