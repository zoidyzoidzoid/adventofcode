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
from time import time_ns

from z3 import Int, Solver, Z3Exception, And


def a(lines):
    return
    result = 0
    for i, line in enumerate("\n".join(lines).split("\n\n")):
        line = line.split("\n")
        a_x, _, a_y = line[0][10:].partition(", ")
        b_x, _, b_y = line[1][10:].partition(", ")
        p_x, _, p_y = line[2][7:].partition(", ")
        a_x, a_y = int(a_x[2:]), int(a_y[2:])
        b_x, b_y = int(b_x[2:]), int(b_y[2:])
        p_x, p_y = int(p_x[2:]), int(p_y[2:])
        # print(f"Button A: X+{a_x}, Y+{a_y}")
        # print(f"Button B: X+{b_x}, Y+{b_y}")
        # print(f"Prize: X={p_x}, Y={p_y}")
        x = Int("x")
        y = Int("y")
        a = Int("a")
        b = Int("b")
        s = Solver()
        s.set("timeout", 30)
        # s.add(And(0 <= a, a <= 100, 0 <= b, b <= 100, (a * (x + a_x)) + (b * (x + b_x)) == p_x, (a * (y + a_y)) + (b * (y + b_y)) == p_y))
        s.check(And(0 <= a, a <= 100, 0 <= b, b <= 100, (a * (x + a_x)) + (b * (x + b_x)) == p_x, (a * (y + a_y)) + (b * (y + b_y)) == p_y))
        # print(s.check())
        try:
            a1 = int(str(s.model()[a]))
            b1 = int(str(s.model()[b]))
        except Z3Exception:
            continue
        if a1 > 100 or b1 > 100:
            continue
        # s2 = Solver()
        # s2.add((a * (x + a_x)) + (b * (x + b_x)) == p_x, (a * (y + a_y)) + (b * (y + b_y)) == p_y, a >= 0, b >= 0, a >= b, a <= 100, b <= 100)
        # s2.check()
        # a2 = int(str(s2.model()[a]))
        # b2 = int(str(s2.model()[b]))
        print(f"s: {a1}, {b1}")
        print(f"s: {a1 * a_x + b1 * b_x} == {p_x}, {a1 * a_y + b1 * b_y} == {p_y}")
        if a1 * a_x + b1 * b_x != p_x or a1 * a_y + b1 * b_y != p_y:
            continue
        # print(f"s2: {a2}, {b2}")
        # if (a1 * 3) + b1 > (a2 * 3) + b2:
        #     result += (a2 * 3)  + b2
        # else:
        result += (a1 * 3) + b1
    print(result)


def b(lines):
    pass
    result = 0
    for i, line in enumerate("\n".join(lines).split("\n\n")):
        line = line.split("\n")
        a_x, _, a_y = line[0][10:].partition(", ")
        b_x, _, b_y = line[1][10:].partition(", ")
        p_x, _, p_y = line[2][7:].partition(", ")
        a_x, a_y = int(a_x[2:]), int(a_y[2:])
        b_x, b_y = int(b_x[2:]), int(b_y[2:])
        p_x, p_y = int(p_x[2:]), int(p_y[2:])
        p_x, p_y = p_x + 10000000000000, p_y + 10000000000000
        x = Int("x")
        y = Int("y")
        a = Int("a")
        b = Int("b")
        s = Solver()
        s.set("timeout", 30)
        s.check(And(0 <= a, 0 <= b, (a * (x + a_x)) + (b * (x + b_x)) == p_x, (a * (y + a_y)) + (b * (y + b_y)) == p_y))
        try:
            a1 = int(str(s.model()[a]))
            b1 = int(str(s.model()[b]))
        except Z3Exception:
            continue
        print(f"s: {a1}, {b1}")
        print(f"s: {a1 * a_x + b1 * b_x} == {p_x}, {a1 * a_y + b1 * b_y} == {p_y}")
        if a1 * a_x + b1 * b_x != p_x or a1 * a_y + b1 * b_y != p_y:
            continue
        # print(f"s2: {a2}, {b2}")
        # if (a1 * 3) + b1 > (a2 * 3) + b2:
        #     result += (a2 * 3)  + b2
        # else:
        result += (a1 * 3) + b1
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


class Timer(object):
    def __init__(self, description):
        self.description = description
    def __enter__(self):
        self.start = time_ns()
    def __exit__(self, type, value, traceback):
        self.end = time_ns()
        d = self.end - self.start
        if d > 1_000_000_000:
            d /= 1_000_000_000
            u = "s"
        elif d > 1_000_000:
            d /= 1_000_000
            u = "ms"
        elif d > 1_000:
            d /= 1_000
            u = "µs"
        else:
            u = "ns"
        print("{}: {} {}".format(self.description, d, u))


def main():
    with Timer("Part 1"):
        a(lines)

    with Timer("Part 2"):
        b(lines)


if __name__ == "__main__":
    main()
