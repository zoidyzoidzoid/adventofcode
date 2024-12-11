#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import sys
import math
from ast import literal_eval
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt
from time import time_ns


def a(lines):
    result = 0
    result2 = 0
    for i, line in enumerate(lines):
        goal, inp = line.split(": ")
        goal = int(goal)
        inp = [i for i in inp.split(" ")]
        options = deque(inp)
        old, new = [], []
        while options:
            c = options.popleft()
            if len(old) == 0:
                new.append([c])
                old = new
                continue
            new = []
            for o in old:
                new.append(o + ["*", c])
                new.append(o + ["+", c])
            old = new
        # print(goal)
        # print(line)
        for i in old:
            res = 0
            op = "+"
            for c in i:
                if c == "*":
                    op = "*"
                elif c == "+":
                    op = "+"
                else:
                    if op == "+":
                        res += int(c)
                    else:
                        res *= int(c)
            # print("".join(i), "=", res)
            if res == goal:
                # print("Success", end="\n\n")
                result += 1
                result2 += goal
                break
        # else:
        #     print("Failure", end="\n\n")

        # if any((eval("".join(i)) == goal) for i in old):
        #     # for i in old:
        #     #     if eval("".join(i)) == goal:
        #     #         print("inp:", "".join(i))
        #     #         print("actual:", eval("".join(i)))
        #     #         print("expected:", goal)
        #     print("Success", end="\n\n")
        #     result += 1
        # else:
        #     print("Failure", end="\n\n")
    print(result)
    print(result2)


def b(lines):
    result = 0
    result2 = 0
    for i, line in enumerate(lines):
        # print(line)
        goal, inp = line.split(": ")
        goal = int(goal)
        inp = [i for i in inp.split(" ")]
        options = deque(inp)
        old, new = [], []
        while options:
            c = options.popleft()
            if len(old) == 0:
                new.append([c])
                old = new
                continue
            new = []
            for o in old:
                new.append(o + ["*", c])
                new.append(o + ["+", c])
                new.append(o + ["|", c])
            old = new
        results = []
        for i in old:
            # print("".join(i))
            # print("".join(i), "=", res)
            res = 0
            op = "+"
            queue = deque(i)
            while queue:
                c = queue.popleft()
                if c == "*":
                    op = "*"
                elif c == "+":
                    op = "+"
                elif c == "|":
                    res = int(str(res) + str(queue.popleft()))
                elif op == "+":
                    res += int(c)
                else:
                    res *= int(c)
                # print("".join(i), "=", res)
            if res == goal:
                result += 1
                result2 += goal
                # print("Success", end="\n\n")
                break
        # else:
        #     print("Failure", end="\n\n")
    print(result)
    print(result2)


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
    # with Timer("Part 1"):
    #     a(lines)

    with Timer("Part 2"):
        b(lines)


if __name__ == "__main__":
    main()
