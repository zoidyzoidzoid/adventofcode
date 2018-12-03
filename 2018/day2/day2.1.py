#!/usr/bin/env python3
import fileinput
from collections import Counter


def process(lines):
    count2 = 0
    count3 = 0
    for line in lines:
        c = Counter(line)
        seen2, seen3 = False, False
        for key, value in c.items():
            if value == 2:
                seen2 = True
            elif value == 3:
                seen3 = True
        if seen3:
            count3 += 1
        if seen2:
            count2 += 1

    result = (count2 * count3)
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


process(lines)
