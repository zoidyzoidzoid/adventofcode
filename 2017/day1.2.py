#!/usr/bin/env python3
import fileinput
from collections import *
from functools import *
from itertools import *


def process(line):
    total = 0
    half = len(line) // 2
    for index, i in enumerate(line):
        i = int(i)
        if index + half >= len(line):
            if i == int(line[index + half - len(line)]):
                total += i
        elif i == int(line[index + half]):
            total += i
    return total

for line in fileinput.input():
    line = line.strip()
    print(process(line))
