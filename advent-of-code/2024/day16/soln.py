#!/usr/bin/env python3
import dataclasses
import fileinput
import heapq
import math
from dataclasses import dataclass
from time import time_ns


@dataclass(frozen=True, order=True)
class HeapItem:
    score: int
    x: int
    y: int
    d_x: int
    d_y: int
    path: set[tuple[int, int]] = dataclasses.field(default_factory=set)


def a(lines):
    start = None
    end = None
    data = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                data[x, y] = c
            elif c == "S":
                start = x, y
            elif c == "E":
                end = x, y
    mx_x, mx_y = len(lines[0]), len(lines)
    # print(start, end, data)

    def print_grid(data):
        print("=" * mx_x)
        for j in range(mx_y):
            for i in range(mx_x):
                if (i, j) == start:
                    print("S", end="")
                elif (i, j) == end:
                    print("E", end="")
                else:
                    print(data.get((i, j), "."), end="")
            print()
        print("=" * mx_x)

    # print_grid(data)
    pos_x, pos_y = start
    dir_x, dir_y = 1, 0
    turns = {
        # straight
        # 1, 0 -> 1, 0
        # (lambda x: (x[0], x[1], 0)),
        # left
        # 1, 0 -> 0, -1
        (lambda x: (x[1], -x[0], 1000)),
        # right
        # 1, 0 -> 0, 1
        (lambda x: (-x[1], x[0], 1000)),
        # around
        # 1, 0 -> -1, 0
        # (lambda x: (-x[1], x[0], 2000)),
    }
    h = [
        HeapItem(0, pos_x, pos_y, dir_x, dir_y),
    ]
    seen = set()
    while True:
        item = heapq.heappop(h)
        if (item.x, item.y, item.d_x, item.d_y) in seen:
            continue
        seen.add((item.x, item.y, item.d_x, item.d_y))
        if (item.x + item.d_x, item.y + item.d_y) == end:
            return item.score + 1
        elif data.get((item.x + item.d_x, item.y + item.d_y)) != "#":
            heapq.heappush(
                h,
                HeapItem(
                    item.score + 1,
                    item.x + item.d_x,
                    item.y + item.d_y,
                    item.d_x,
                    item.d_y,
                ),
            )
        for turn in turns:
            d_x, d_y, s = turn((item.d_x, item.d_y))
            if data.get((item.x + d_x, item.y + d_y)) != "#":
                heapq.heappush(h, HeapItem(item.score + s, item.x, item.y, d_x, d_y))
        # DEBUG
        # print(seen)
        # print(h)
        # # DEBUG
        # break
    # result = 0
    # print(result)


def b(lines):
    start = None
    end = None
    data = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                data[x, y] = c
            elif c == "S":
                start = x, y
            elif c == "E":
                end = x, y
    mx_x, mx_y = len(lines[0]), len(lines)
    # print(start, end, data)
    result = {
        (start),
    }

    def print_grid(data):
        for j in range(mx_y):
            for i in range(mx_x):
                if (i, j) == start:
                    print("S", end="")
                elif (i, j) == end:
                    print("E", end="")
                elif (i, j) in result:
                    print("O", end="")
                else:
                    print(data.get((i, j), "."), end="")
            print()

    # print_grid(data)
    pos_x, pos_y = start
    dir_x, dir_y = 1, 0
    turns = {
        (lambda x: (x[0], x[1], 1)),
        (lambda x: (x[1], -x[0], 1001)),
        (lambda x: (-x[1], x[0], 1001)),
    }
    h = [
        HeapItem(0, pos_x, pos_y, dir_x, dir_y, {(pos_x, pos_y)}),
    ]
    best_score = a(lines)
    cache: dict[tuple[int, int, int, int], int] = {}
    print(f"Looking for best score={best_score}")
    while h:
        item = heapq.heappop(h)
        # print(item)
        if item.score > best_score:
            break
        # seen.add((item.x, item.y, item.d_x, item.d_y))
        if (item.x, item.y) == end:
            print(item)
            if item.score == best_score:
                print(f"Best path found")
                print(f"path={item.path}")
                print(f"score={item.score}")
                result.update({(x[0], x[1]) for x in item.path})
            continue
        if cache.get((item.x, item.y, item.d_x, item.d_y), math.inf) < item.score:
            continue
        cache.setdefault((item.x, item.y, item.d_x, item.d_y), item.score)
        cache[item.x, item.y, item.d_x, item.d_y] = min(cache[item.x, item.y, item.d_x, item.d_y], item.score)
        for turn in turns:
            d_x, d_y, s = turn((item.d_x, item.d_y))
            if data.get((item.x + d_x, item.y + d_y)) != "#":
                heapq.heappush(
                    h,
                    HeapItem(
                        item.score + s,
                        item.x + d_x,
                        item.y + d_y,
                        d_x,
                        d_y,
                        item.path.union({(item.x, item.y)}),
                    ),
                )
    print_grid(data)
    print(len(result) + 1)


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
