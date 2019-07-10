#!/usr/bin/env python3.6
import fileinput
from collections import Counter, OrderedDict
from functools import cmp_to_key, total_ordering
from itertools import chain, islice

@total_ordering
class CheckSum:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value

    def __lt__(self, other):
        return (self.value > other.value) or (self.value == other.value and self.key < other.key)

    def __repr__(self):
        return f'{self.key} {self.value}'

total = 0

for line in fileinput.input():
    line = line.strip().split('-')
    name = line[:-1]
    sector_id = int(line[-1].split('[')[0])
    possible_checksum = line[-1].split('[')[-1].strip(']')
    checksum = Counter(chain.from_iterable(name))
    # print(f'{checksum}')
    checksum = sorted(CheckSum(k, v) for k, v in checksum.items())
    # print(f'{checksum}')
    checksum = ''.join((i.key for i in checksum))[:5]

    print(f'comparing {checksum} and {possible_checksum}')
    if checksum == possible_checksum:
        print(f'success for {checksum}')
        total += sector_id

print(f'sum of sector IDs: {total}')
