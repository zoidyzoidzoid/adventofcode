#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def a(lines):
    result = 0
    for i, line in enumerate(lines):
        if '-' in line:
            start, _, end = line.partition('-')
            r = range(int(start), int(end))
        else:
            line = int(line)
            r = range(line, line + 1)
        for i in r:
            last = None
            count = 0
            same = None
            i = str(i)
            for c in i:
                if last == None:
                    last = c
                    count = 1
                    continue
                if c == last:
                    count += 1
                elif c < last:
                    print(i, 'invalid, decreasing')
                    break
                elif count == 2:
                    same = True
                if c != last:
                    count = 1
                last = c
            else:
                if count == 2:
                    same = True
                if not same:
                    print(i, 'invalid, no pair')
                    continue
                print(i, 'valid')
                result += 1
    print(result)


def b(lines):
    pass


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
