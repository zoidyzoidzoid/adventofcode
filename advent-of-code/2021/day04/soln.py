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
    order = [int(i) for i in lines[0].split(",")]
    # print(order)
    boards = []
    for i, line in enumerate("\n".join(lines[2:]).split("\n\n")):
        # print("Board #{}".format(i))
        # print(line)
        # print()
        board = []
        boards.append([
            [int(c) for c in row.replace("  ", " ").split()]
            for row in line.split("\n")
        ])
    for num in order:
        for bn, board in enumerate(boards):
            for row in board:
                if num not in row:
                    continue
                col = row.index(num)
                row[col] = 0
                if sum(row) == 0 or sum(row[col] for row in board) == 0:
                    print("Board #{}".format(bn))
                    print("{} * {}".format(num, sum(sum(row) for row in board)))
                    print(num * sum(sum(row) for row in board))
                    return

    # print(boards)
    # print(result)


def b(lines):
    result = 0
    order = [int(i) for i in lines[0].split(",")]
    # print(order)
    boards = []
    for i, line in enumerate("\n".join(lines[2:]).split("\n\n")):
        # print("Board #{}".format(i))
        # print(line)
        # print()
        board = []
        boards.append([
            [int(c) for c in row.replace("  ", " ").split()]
            for row in line.split("\n")
        ])
    for num in order:
        for bn, board in enumerate(boards):
            for row in board:
                if num not in row:
                    continue
                col = row.index(num)
                row[col] = 0
                if sum(row) == 0 or sum(row[col] for row in board) == 0:
                    if len([b for b in boards if len(b) != 0]) == 1:
                        print("Board #{}".format(bn))
                        print("{} * {}".format(num, sum(sum(row) for row in board)))
                        print(num * sum(sum(row) for row in board))
                        return
                    else:
                        boards[bn] = []
                break

    print(boards)
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
