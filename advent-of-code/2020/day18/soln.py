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


def process_a(line):
    a = ''
    line = deque(line)
    while '(' in line:
        c = line.popleft()
        if c == '(':
            s = ''
            t = 0
            while True:
                d = line.popleft()
                if t == 0 and d == ')':
                    break
                elif d == '(':
                    s += d
                    t += 1
                elif d == ')':
                    s += d
                    t -= 1
                else:
                    s += d
            a += process_a(s)
        else:
            a += c
    else:
        while line:
            a += line.popleft()
        b = deque(''.join(a).split(' '))
        result = int(b.popleft())
        while b:
            c = b.popleft()
            if c == '*':
                result *= int(b.popleft())
            elif c == '+':
                result += int(b.popleft())
            else:
                raise Exception('Missing operator: {}'.format(c))
        return str(result)
    return a

def a(lines):
    result = 0
    for line in lines:
        r = int(process_a(line))
        # print(r)
        result += r
    print(result)


def process_b(line):
    a = ''
    line = deque(line)
    while '(' in line:
        c = line.popleft()
        if c == '(':
            s = ''
            t = 0
            while True:
                d = line.popleft()
                if t == 0 and d == ')':
                    break
                elif d == '(':
                    s += d
                    t += 1
                elif d == ')':
                    s += d
                    t -= 1
                else:
                    s += d
            a += process_b(s)
        else:
            a += c
    else:
        while line:
            a += line.popleft()
        if ' * ' in a:
            a = ' * '.join((process_b(i) for i in a.split(' * ')))
        # print(a)
        b = deque(''.join(a).split(' '))
        result = int(b.popleft())
        while b:
            c = b.popleft()
            if c == '*':
                result *= int(b.popleft())
            elif c == '+':
                result += int(b.popleft())
            else:
                raise Exception('Missing operator: {}'.format(c))
        return str(result)
    return a


def b(lines):
    result = 0
    for line in lines:
        r = int(process_b(line))
        # print(r)
        result += r
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
