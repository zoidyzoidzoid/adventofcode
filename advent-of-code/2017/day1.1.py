#!/usr/bin/env python3
import fileinput
from collections import *
from functools import *
from itertools import *

def process(line):
    total = 0
    for index, i in enumerate(line):
        i = int(i)
        if index + 1 == len(line):
            if i == int(line[0]):
                total += i
        elif i == int(line[index + 1]):
            total += i
    return total

for line in fileinput.input():
    line = line.strip()
    print(process(line))

