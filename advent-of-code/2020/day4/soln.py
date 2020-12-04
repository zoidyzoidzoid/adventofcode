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
    lines = deque(lines)
    fields = {}
    while True:
        try:
            line = lines.popleft()
        except IndexError:
            line = ""
        if line == "":
            # process_fields
            if all(field in fields for field in [
                    'byr',
                    'iyr',
                    'eyr',
                    'hgt',
                    'hcl',
                    'ecl',
                    'pid',
                ]):
                result += 1
            fields = {}
        else:
            # add to fields
            for kv in line.split(' '):
                k, _, v = kv.partition(':')
                fields[k] = v
        if not lines and line == "":
            break
    print(result)


vs = {
    'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    'hgt': lambda x: (x.endswith('cm') and 150 <= int(x.replace('cm', '')) <= 193) or (x.endswith('in') and 59 <= int(x.replace('in', '')) <= 76),
    'hcl': lambda x: len(x) == 7 and len(x.lstrip('#')) == 6 and all(i in set('abcdef0123456789') for i in x.lstrip('#')),
    'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda x: len(x) == 9 and x.isnumeric(),
}


def b(lines):
    result = 0
    lines = deque(lines)
    fields = {}
    while True:
        try:
            line = lines.popleft()
        except IndexError:
            line = ""
        if line == "":
            # process_fields
            if len(set(fields.keys()).intersection({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'})) != 7:
                fields = {}
                continue
            if all(vs.get(k, lambda x: True)(v) for k, v in fields.items()):
                result += 1
            fields = {}
        else:
            # add to fields
            for kv in line.split(' '):
                k, _, v = kv.partition(':')
                fields[k] = v
        if not lines and line == "":
            break
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
