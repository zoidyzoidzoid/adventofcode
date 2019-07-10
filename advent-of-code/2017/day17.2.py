#!/usr/bin/env python3
# coding: utf-8


def process(inp):
    pos = 0
    val = 0
    for i in range(1, 50000000):
        pos = ((pos + inp) % i) + 1
        if pos == 1:
            val = i
        # print(' '.join(str(i) if index != pos else '({})'.format(i) for index, i in enumerate(arr)))
    return val


# print(process(3))
print(process(329))
