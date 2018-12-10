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
    points = []
    result = 0
    for i, line in enumerate(lines):
        p, _, v = line.partition(" velocity=")
        p, v = p.lstrip('position=< ').rstrip('>'), v.lstrip('< ').rstrip('>')
        p, v = p.replace(' ', ''), v.replace(' ', '')
        p, v = p.split(','), v.split(',')
        p_x, p_y = int(p[0]), int(p[1])
        v_x, v_y = int(v[0]), int(v[1])
        print(p_x, p_y, v_x, v_y)
        points.append((p_x, p_y, v_x, v_y))
    sec = 0
    mn = None
    attempts = 0
    while attempts < 10:
        mn_x = min((p[0] for p in points))
        mx_x = max((p[0] for p in points))
        mn_y = min((p[1] for p in points))
        mx_y = max((p[1] for p in points))
        a = (mx_x - mn_x) * (mx_y - mn_y)
        # print(a)
        if mn is None or a < mn:
            attempts = 0
            mn = a

            print('Second:', sec)
            if sec == 10333:
                grid = [
                    ['.'] * (mx_x - mn_x + 1)
                    for i in range((mx_y - mn_y + 1))
                ]
                for i, d in enumerate(points):
                    p_x, p_y, v_x, v_y = d
                    # print(mx_x, mn_x, mx_y, mn_y)
                    # print(p_y, p_x, mx_x - mn_x + 1, mx_y - mn_y + 1)
                    grid[p_y - mn_y][p_x - mn_x] = '#'
                    
                print('\n'.join(''.join(row) for row in grid))
        else:
            attempts += 1
        for i, d in enumerate(points):
            p_x, p_y, v_x, v_y = d
            points[i] = p_x + v_x, p_y + v_y, v_x, v_y
        sec += 1
    print(result)


def b(lines):
    a(lines)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
