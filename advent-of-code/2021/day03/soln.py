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
    data = defaultdict(Counter)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            data[j][c] += 1

    result1, result2 = "", ""
    for i, _ in enumerate(line):
        result1 += data[i].most_common(2)[0][0]
        result2 += data[i].most_common(2)[1][0]
    print(int(result1, base=2) * int(result2, base=2))


def b(lines):
    # calculate o2
    # calculate co2

    o2data = defaultdict(Counter)
    co2data = defaultdict(Counter)
    o2lines = lines
    co2lines = lines
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            o2data[j][c] += 1
            co2data[j][c] += 1

    result1, result2 = "", ""
    for i, _ in enumerate(line):
        if len(o2lines) > 1:
            if o2data[i]["0"] == o2data[i]["1"]:
                o2criteria = "1"
            else:
                o2criteria = o2data[i].most_common(2)[0][0]
            old = o2lines.copy()
            o2lines = []
            o2data = defaultdict(Counter)
            for line in old:
                if line[i] == o2criteria:
                    o2lines.append(line)
            for line in o2lines:
                for j, c in enumerate(line):
                    if line[i] == o2criteria:
                        o2data[j][c] += 1
        if len(co2lines) > 1:
            if co2data[i]["0"] == co2data[i]["1"]:
                co2criteria = "0"
            else:
                co2criteria = co2data[i].most_common(2)[1][0]
            old = co2lines.copy()
            co2lines = []
            co2data = defaultdict(Counter)
            for line in old:
                if line[i] == co2criteria:
                    co2lines.append(line)
            for line in co2lines:
                for j, c in enumerate(line):
                    if line[i] == co2criteria:
                        co2data[j][c] += 1
        # print(i, o2criteria)
        # print(i, co2criteria)
        # print("O2 lines")
        # print(o2lines)
        # print("CO2 lines")
        # print(co2lines)
    print(int(o2lines[0], base=2) * int(co2lines[0], base=2))


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
