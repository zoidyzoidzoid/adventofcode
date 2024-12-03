#!/usr/bin/env python3
import fileinput
from collections import Counter
from time import time_ns


def a(lines):
    result = 0
    lines = [line for line in lines if line.strip()]
    l1, l2 = [], []
    for _, line in enumerate(lines):
        if not line:
            continue
        line = [int(i) for i in line.split()]
        l1.append(line[0])
        l2.append(line[1])
    l1 = list(sorted(l1))
    l2 = list(sorted(l2))
    for i, j in enumerate(l1):
        result += abs(l2[i] - j)
    print(result)


def b(lines):
    result = 0
    lines = [line for line in lines if line.strip()]
    l1, l2 = [], []
    for _, line in enumerate(lines):
        if not line:
            continue
        line = [int(i) for i in line.split()]
        l1.append(line[0])
        l2.append(line[1])
    l1 = list(sorted(l1))
    l2 = Counter(l2)
    for i, j in enumerate(l1):
        result += l2[j] * j
    print(result)


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
    lines = []
    for line in fileinput.input():
        lines.append(line.strip())

    with Timer("Part 1"):
        a(lines)

    with Timer("Part 2"):
        b(lines)


if __name__ == "__main__":
    main()
