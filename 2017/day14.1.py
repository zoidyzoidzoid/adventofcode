#!/usr/bin/env python
# coding: utf-8


def knot_hash(inp):
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


def process(inp):
    print(inp)
    grid = [['0' for i in range(128)] for i in range(128)]
    total = 0
    for i in range(128):
        key = inp + '-' + str(i)
        hash = knot_hash(key)
        for j, x in enumerate(hash):
            for k, y in enumerate('{:04b}'.format(int(x, base=16))):
                grid[i][(j * 4) + k] = y
                if y == '1':
                    total += 1
    for row in grid:
        print(''.join(row))
    return total


print('Example')
print(process('flqrgnkx'))
print('Puzzle input')
print(process('vbqugkhl'))
