#!/usr/bin/env python3
import fileinput
from collections import *
from functools import *
from itertools import *
from math import *


def process(line):
    line = [str(sorted(word)) for word in line.split(" ")]
    if len(set(line)) == len(line):
        return 1
    return 0

total = 0

for line in fileinput.input():
    line = line.strip()
    total += process(line)

print(total)
