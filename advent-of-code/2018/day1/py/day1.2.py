#!/usr/bin/env python3
import fileinput


def process(lines):
    freq = 0
    seen = set()
    while True:
        for line in lines:
            freq += int(line)
            if freq in seen:
                return freq
            seen.add(freq)


lines = []
for line in fileinput.input():
    lines.append(line.strip())

print(process(lines))
