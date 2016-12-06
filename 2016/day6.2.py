#!/usr/bin/env python3.6
import fileinput
from collections import *
from functools import *
from itertools import *

results = defaultdict(Counter)

for line in fileinput.input():
    line = line.strip()

    for index, c in enumerate(line):
        results[index][c] += 1

for key in sorted(results):
    print(results[key].most_common()[-1][0], end='')

# print(f'hello world')
