#!/usr/bin/env python3
# coding: utf-8
import fileinput


def process(row):
    row = list(map(int, row.split()))
    for index, i in enumerate(row[:-1]):
        for j in row[index + 1:]:
            if i % j == 0:
                return i // j
            elif j % i == 0:
                return j // i

total = 0
for line in fileinput.input():
    line = line.strip()
    total += process(line)
print(total)
