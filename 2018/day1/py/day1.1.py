#!/usr/bin/env python3
import fileinput


def process(lines):
    freq = 0
    for line in lines:
        freq += int(line)
    return freq


lines = []
for line in fileinput.input():
    lines.append(line.strip())

print(process(lines))
