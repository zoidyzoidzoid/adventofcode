#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt
from typing import List


def a(lines):
    result = 0
    for i, line in enumerate(lines):
        line = int(line)
        mass = floor(line / 3) - 2
        result += mass
    print(result)
    return result


def b(lines):
    res = 0
    for i, line in enumerate(lines):
        result = 0
        line = int(line)
        mass = floor(line / 3) - 2
        result += mass
        fuel = result
        while True:
            fuel = floor(fuel / 3) - 2
            if fuel <= 0:
                break
            result += fuel
        res += result
    print(res)
    return res


def main():
    lines = []
    for line in fileinput.input():
        lines.append(line.strip())


    a(lines)
    b(lines)


if __name__ == '__main__':
    main()


@dataclass
class Case:
    want: List[int]
    expected: int


def test_a():
    cases = [
        Case([12], 2),
        Case([14], 2),
        Case([1969], 654),
        Case([100756], 33583),
    ]
    with open('input.txt') as f:
        cases.append(
            Case(
                [line for line in f.read().split('\n') if line],
                3406432))

    for case in cases:
        assert a(case.want) == case.expected


def test_b():
    cases = [
        Case([12], 2),
        Case([1969], 966),
        Case([100756], 50346),
    ]
    with open('input.txt') as f:
        cases.append(
            Case(
                [line for line in f.read().split('\n') if line],
                5106777))

    for case in cases:
        assert b(case.want) == case.expected

