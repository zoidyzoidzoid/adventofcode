#!/usr/bin/env python3
import fileinput


def process(lines):
    for i, line in enumerate(lines[:-1]):
        for line2 in lines[i + 1:]:
            diffs = 0
            for x, c in enumerate(line):
                if c != line2[x]:
                    diffs += 1
                if diffs > 1:
                    break
            if diffs == 1:
                s = ''
                for x, c in enumerate(line):
                    if c == line2[x]:
                        s += c
                print(s)




lines = []
for line in fileinput.input():
    lines.append(line.strip())


process(lines)
