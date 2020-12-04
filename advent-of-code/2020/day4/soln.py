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


def validate(fields):
    if any(field not in fields for field in [
            'byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid',
        ]):
        return 0
    byr = fields['byr']
    if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
        return 0
    iyr = fields['iyr']
    if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
        return 0
    eyr = fields['eyr']
    if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
        return 0
    hgt = fields['hgt']
    if hgt.endswith('cm'):
        hgt = int(hgt.replace('cm', ''))
        if hgt < 150 or hgt > 193:
            return 0
    elif hgt.endswith('in'):
        hgt = int(hgt.replace('in', ''))
        if hgt < 59 or hgt > 76:
            return 0
    else:
        return 0
    hcl = fields['hcl']
    if len(hcl) != 7 or any(i not in set('abcdef0123456789') for i in hcl.replace('#', '')):
        return 0
    ecl = fields['ecl']
    if ecl not in set(('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')):
        return 0
    pid = fields['pid']
    if len(pid) != 9 or not pid.isnumeric():
        return 0
    return 1


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
            result += validate(fields)
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
