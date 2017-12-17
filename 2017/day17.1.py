#!/usr/bin/env python3
# coding: utf-8


def process(inp):
    pos = 0
    arr = [0]
    for i in range(1, 2018):
        pos = ((pos + inp) % i) + 1
        arr.insert(pos, i)
        # print(' '.join(str(i) if index != pos else '({})'.format(i) for index, i in enumerate(arr)))
    return arr[pos-3:pos+3]


print(process(3))
print(process(329))
