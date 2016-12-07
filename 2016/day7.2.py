#!/usr/bin/env python3.6
import fileinput
import re
from collections import *
from functools import *
from itertools import *


def check_ip(line):
    supernets = []
    hypernets = []
    for line in re.split('(\[[^]]*\])', line):
        search = re.search('(\[[^]]*\])', line)
        if search is not None:
            for group in search.groups():
                hypernets.append(group.lstrip('[').rstrip(']'))
        else:
            supernets.append(line)
    for supernet in supernets:
        for i, c in enumerate(supernet):
            if i + 2 < len(supernet) and supernet[i] == supernet[i + 2] and supernet[i] != supernet[i + 1]:
                a = supernet[i]
                b = supernet[i + 1]
                for hypernet in hypernets:
                    for j, d in enumerate(hypernet):
                        if j + 2 < len(hypernet) and a == hypernet[j + 1] and b == hypernet[j] and b == hypernet[j + 2]:
                            return 1
    return 0


total = 0

for line in fileinput.input():
    line = line.strip()
    print(line)
    total += check_ip(line)


print(f'{total}')
