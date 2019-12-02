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
        # print(line)
        state = [int(i) for i in line.split(',')]
        state[1] = 12
        state[2] = 2
        pos = 0
        while True:
            op_code = state[pos]
            if op_code == 1:
                pos += 1
                x = state[pos]
                pos += 1
                y = state[pos]
                pos += 1
                z = state[pos]
                state[z] = state[x] + state[y]
                pos += 1
            elif op_code == 2:
                pos += 1
                x = state[pos]
                pos += 1
                y = state[pos]
                pos += 1
                z = state[pos]
                state[z] = state[x] * state[y]
                pos += 1
            elif op_code == 99:
                break
            else:
                raise Exception('Unknown op_code: %s', op_code)
        # print(state)
        print(state[0])
    # print(result)


def calc(line, noun, verb):
    state = dict((k, int(i)) for k, i in enumerate(line.split(',')))
    state[1] = noun
    state[2] = verb
    pos = 0
    while True:
        op_code = state[pos]
        if op_code == 1:
            pos += 1
            x = state[pos]
            pos += 1
            y = state[pos]
            pos += 1
            z = state[pos]
            state[z] = state[x] + state[y]
            pos += 1
        elif op_code == 2:
            pos += 1
            x = state[pos]
            pos += 1
            y = state[pos]
            pos += 1
            z = state[pos]
            state[z] = state[x] * state[y]
            pos += 1
        elif op_code == 99:
            break
        else:
            raise Exception('Unknown op_code: %s', op_code)
    from pprint import pprint
    # pprint(state)
    result = state[0]
    return result

def b(lines):
    result = 0
    for i, line in enumerate(lines):
        # print(line)
        for x in range(100):
            for y in range(100):
                res = calc(line, x, y)
                if res == 19690720:
                    print(x, y, res)
                    print((100 * x) + y, res)
    # print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
