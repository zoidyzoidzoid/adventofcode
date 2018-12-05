#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


# def soln(s):


def a(lines):
    result = ''
    line = deque(lines[0].strip())
    while line:
        c = line.popleft()
        if c == '(':
            s = ''
            c = line.popleft()
            while c != ')':
                s += c
                c = line.popleft()
            # print(s)
            x, _, y = s.partition('x')
            x, y = int(x), int(y)
            buf = ''
            for i in range(x):
                buf += line.popleft()
            for i in range(y):
                result += buf
        else:
            result += c

    print(len(result))


def soln(inp):
    result = 0
    inp = deque(inp)
    while inp:
        c = inp.popleft()
        if c == '(':
            s = ''
            c = inp.popleft()
            while c != ')':
                s += c
                c = inp.popleft()
            # print(s)
            x, _, y = s.partition('x')
            x, y = int(x), int(y)
            buf = ''
            for i in range(x):
                buf += inp.popleft()
            result += y * soln(buf)
            # print(''.join(line))
        else:
            result += 1
    return result


def b(lines):
    result = soln(lines[0].strip())
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


# a(lines)
b(lines)
