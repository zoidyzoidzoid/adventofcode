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


def a(lines, h=6, w=25):
    for _, line in enumerate(lines):
        d = deque(line)
        h2 = len(line) // (h * w)
        layers = []
        for layer in range(h2):
            x, y = layer * h * w, (layer + 1) * h * w
            l = []
            for _ in range(x, y):
                l.append(d.popleft())
            layers.append(l)

    def count(layer, i):
        return sum((pixel.count(i) for pixel in layer))

    mn = sys.maxsize
    result = 0
    for i, layer in enumerate(layers):
        zeroes = count(layer, '0')
        ones = count(layer, '1')
        twos = count(layer, '2')
        if min((zeroes, mn)) == zeroes:
            mn = zeroes
            result = ones * twos
    print(mn, result)


def b(lines, h=6, w=25):
    grid = [
        [' ' for _ in range(w)]
        for _ in range(h)
    ]

    for _, line in enumerate(lines):
        d = deque(line)
        h2 = len(line) // (h * w)
        layers = []
        for layer in range(h2):
            x2, y2 = layer * h * w, (layer + 1) * h * w
            for i in range(layer * h * w, (layer + 1) * h * w):
                z = (i - (layer * h * w))
                y = z // w
                x = z % w
                c = d.popleft()
                if grid[y][x] == ' ':
                    if c == '0':
                        grid[y][x] = '⬛'
                    elif c == '1':
                        grid[y][x] = '⬜'
    print('\n'.join(''.join(str(c) for c in row) for row in grid))


lines = []
for line in fileinput.input():
    lines.append(line.strip())


# a(['123456789012'], 2, 3)
# a(lines)
b(['0222112222120000'], 2, 2)
b(lines)
