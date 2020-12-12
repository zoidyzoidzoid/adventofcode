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
    result = 0
    i = 0
    seen = set()
    while True:
        if i in seen:
            break
        seen.add(i)
        line = lines[i]
        cmd, _, arg = line.partition(" ")
        arg = int(arg)
        print(cmd, arg)
        if cmd == "nop":
            i += 1
        elif cmd == "acc":
            result += arg
            i += 1
        elif cmd == "jmp":
            i += arg
    print(result)


def b(og_lines):
    swaps = [
        i
        for i, j in enumerate(og_lines)
        if j.startswith("nop ") or j.startswith("jmp ")
    ]
    for swap in swaps:
        lines = og_lines.copy()
        if "jmp" in lines[swap]:
            lines[swap] = lines[swap].replace("jmp", "nop")
        else:
            lines[swap] = lines[swap].replace("nop", "jmp")
        result = 0
        i = 0
        seen = set()
        while True:
            if i == len(lines):
                print("{}/{}: {}".format(i, len(lines), result))
                break
            i = i % len(lines)
            if i in seen:
                # print("{}/{}: {}".format(i, len(lines), result))
                break
            seen.add(i)
            line = lines[i]
            cmd, _, arg = line.partition(" ")
            arg = int(arg)
            # print(cmd, arg)
            if cmd == "nop":
                i += 1
            elif cmd == "acc":
                result += arg
                i += 1
            elif cmd == "jmp":
                i += arg


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
