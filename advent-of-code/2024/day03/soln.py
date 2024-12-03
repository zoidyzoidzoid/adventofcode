#!/usr/bin/env python3
import fileinput
from time import time_ns

from rich.console import Console


def a(lines):
    return
    result = 0
    for line in lines:
        for i in range(len(line)):
            if line[i : i + 4] == "mul(":
                a, _, b = line[i + 4 : i + 4 + line[i + 4 : ].index(")")].partition(",")
                if a.isdecimal() and b.isdecimal():
                    result += int(a) * int(b)
    print(result)


def b(lines):
    enabled = True
    result = 0
    for line in lines:
        for i in range(len(line)):
            if line[i : i + 4] == "do()":
                enabled = True
            elif line[i : i + 7] == "don't()":
                enabled = False
            elif line[i : i + 4] == "mul(":
                a, _, b = line[i + 4 : i + 4 + line[i + 4 : ].index(")")].partition(",")
                if a.isdecimal() and b.isdecimal() and enabled:
                    result += int(a) * int(b)
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
