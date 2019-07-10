#!/usr/bin/env python3.6
import fileinput
import re
from collections import *
from functools import *
from itertools import *


def check_ip(line):
    found = 0
    for line in re.split('(\[[^]]*\])', line):
        search = re.search('(\[[^]]*\])', line)
        if search is not None:
            for group in search.groups():
                group = group.lstrip('[').rstrip(']')
                # print(group)
                for i, c in enumerate(group):
                    if i + 3 < len(group) and group[i:i+2] == group[i+2:i+4][::-1] and group[i] != group[i+1]:
                        # print('invalid:', group[i:i+4])
                        return 0
        else:
            # print(line)
            for i, c in enumerate(line):
                if i + 3 < len(line) and line[i:i+2] == line[i+2:i+4][::-1] and line[i] != line[i+1]:
                    # print('valid:', line[i:i+4])
                    found = 1
    return found


total = 0

for line in fileinput.input():
    line = line.strip()
    if check_ip(line):
        total += 1
        # print(f"valid: {line}")
    # else:
        # print(f"invalid: {line}")


print(f'{total}')
