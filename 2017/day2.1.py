#!/usr/bin/env python3
# coding: utf-8
import fileinput


def process(row):
    row = list(map(int, row.split()))
    return max(row) - min(row)

total = 0
for line in fileinput.input():
    line = line.strip()
    total += process(line)
print(total)
