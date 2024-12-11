#!/usr/bin/env python3
import fileinput
from collections import defaultdict
from time import time_ns


def a(lines):
    result = 0
    line = [int(i) for i in lines[0].split()]
    old = defaultdict(int)
    for i in line:
        old[i] += 1
    for i in range(25):
        new = defaultdict(int)
        for j, count in old.items():
            if j == 0:
                new[1] += count
            elif len(str(j)) % 2 == 0:
                j = str(j)
                a, b = j[:len(j)//2], j[len(j)//2:]
                new[int(a)] += count
                new[int(b)] += count
            else:
                new[j * 2024] += count
        old = new
    print(sum(old.values()))


def b(lines):
    result = 0
    line = [int(i) for i in lines[0].split()]
    old = defaultdict(int)
    for i in line:
        old[i] += 1
    for i in range(75):
        new = defaultdict(int)
        for j, count in old.items():
            if j == 0:
                new[1] += count
            elif len(str(j)) % 2 == 0:
                j = str(j)
                a, b = j[:len(j)//2], j[len(j)//2:]
                new[int(a)] += count
                new[int(b)] += count
            else:
                new[j * 2024] += count
        old = new
    print(sum(old.values()))


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
