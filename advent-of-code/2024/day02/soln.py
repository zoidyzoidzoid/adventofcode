#!/usr/bin/env python3
import fileinput
from time import time_ns

def validate_line(line):
    direction = None
    x = 0
    end = len(line[:-1])
    while x != end:
        diff = int(line[x + 1]) - int(line[x])
        if direction is None and diff > 0:
            direction = "inc"
        elif direction is None and diff < 0:
            direction = "dec"
        if diff not in (-3, -2, -1, 1, 2, 3):
            print(f"diff invalid: {' '.join(line)}")
            return False
        if direction == "inc" and diff < 0:
            print(f"wrong dir: {' '.join(line)}")
            return False
        elif direction == "dec" and diff > 0:
            print(f"wrong dir: {' '.join(line)}")
            return False
        x += 1
    print(f'{" ".join(line)}: Safe')
    return True

def a(lines):
    result = 0
    lines = [line for line in lines if line.strip()]

    for _, line in enumerate(lines):
        if not line:
            continue
        line = line.split()
        if validate_line(line):
            result += 1
    print(result)


def b(lines):
    result = 0


    lines = [line for line in lines if line.strip()]
    for _, line in enumerate(lines):
        if not line:
            continue
        line = line.split()
        # print(" ".join(line))
        if validate_line(line):
            result += 1
        else:
            for i, _ in enumerate(line):
                if validate_line([y for (x, y) in enumerate(line) if x != i]):
                    result += 1
                    break
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
