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
    data = {}
    mask = {}
    for i, line in enumerate(lines):
        if line.startswith('mask = '):
            line = line[len('mask = '):]
            # mask = {}
            for i, c in enumerate(line[::-1]):
                if c == 'X':
                    mask.pop(i, None)
                    continue
                mask[i] = c
             # print('*' * 36)
             # print('updated mask')
             # print('*' * 36)
             # print('mask:   {}'.format(''.join(reversed([mask.get(i, 'X') for i in range(36)]))))
             # print('*' * 36)
        else:
            line = line[len('mem['):]
            addr, _, val = line.partition('] = ')
            addr, val = int(addr), int(val)
            # print('value:  {0:036b}  (decimal {0})'.format(val))
            # print('mask:   {}'.format(''.join(reversed([mask.get(i, 'X') for i in range(36)]))))
            val = list('{0:036b}'.format(val))
            for i, c in mask.items():
                val[-1-i] = c
            result = int(''.join(val), base=2)
            # print('result: {0:036b}  (decimal {0})'.format(result))
            data[addr] = result
        # print(data)
    print(sum(data.values()))


def b(lines):
    data = {}
    mask = {}
    for i, line in enumerate(lines):
        if line.startswith('mask = '):
            line = line[len('mask = '):]
            for i, c in enumerate(line[::-1]):
                mask[i] = c
        else:
            line = line[len('mem['):]
            addr, _, og_val = line.partition('] = ')
            addr, og_val = int(addr), int(og_val)
            # print('addr:  {0:036b}  (decimal {0})'.format(addr))
            addr = list('{0:036b}'.format(addr))
            # print('mask:  {}'.format(''.join(reversed([mask.get(i, 'X') for i in range(36)]))))
            for i, c in mask.items():
                if c == '0':
                    continue
                addr[-1-i] = c
            addrs = []
            # print('seed:   {0}'.format(''.join(addr)))
            for i in range(addr.count('X') + 1):
                for combo in combinations([j for j, c in enumerate(addr) if c == 'X'], i):
                    b = list(addr).copy()
                    for k, d in enumerate(b):
                        if d != 'X':
                            continue
                        b[k] = '0' if k in combo else '1'
                    b = ''.join(b)
                    b = int(b, base=2)
                    # print('addr:   {0:036b}  (decimal {0})'.format(b))
                    data[b] = og_val
        # print(data)
    print(sum(data.values()))


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
