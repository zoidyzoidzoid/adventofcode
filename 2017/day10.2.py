#!/usr/bin/env python3
# coding: utf-8


def process(inp):
    sparse = [x for x in range(256)]
    inp = [ord(c) for c in inp] + [17, 31, 73, 47, 23]
    pos = 0
    skip = 0
    for _ in range(64):
        for length in inp:
            l = pos + length
            if l >= 256:
                while l >= 256:
                    l -= 256
                s = sparse[pos:] + sparse[:l]
                s = list(reversed(s))
                sparse = s[len(s) - l:] + sparse[l:pos] + s[:len(s) - l]
            else:
                sparse = sparse[:pos] + list(reversed(sparse[pos:l])) + sparse[l:]
            pos += length + skip
            while pos >= 256:
                pos -= 256
            skip += 1
    dense = ''
    for i in range(16):
        output = 0
        for k in sparse[i * 16:(i * 16) + 16]:
            output ^= k
        dense += '{:0>2x}'.format(output)
    return dense


for e, a in (
        ('a2582a3a0e66e6e86e3812dcb672a272', process('')),
        ('33efeb34ea91902bb2f59c9920caa6cd', process('AoC 2017')),
        ('3efbe78a8d82f29979031a4aa0b16a9d', process('1,2,3')),
        ('63960835bcdc130f0b66d7ff4f6a5a8e', process('1,2,4'))):
    if e != a:
        print('Expected:', e, 'Actual:', a)

print(process('157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30'))
