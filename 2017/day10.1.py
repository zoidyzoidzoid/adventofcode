#!/usr/bin/env python3
# coding: utf-8
def process(inp, l):
    rope = [x for x in range(l)]
    pos = 0
    skip = 0
    for length in inp:
        r = pos + length
        if pos + length >= len(rope):
            r = (pos + length) - len(rope)
            s = rope[pos:] + rope[:r]
            s = list(reversed(s))
            rope = s[len(s) - r:] + rope[r:pos] + s[:len(s) - r]
        else:
            rope = rope[:pos] + list(reversed(rope[pos:pos + length])) + rope[pos + length:]
        pos += length + skip
        if pos > len(rope):
            pos -= len(rope)
        skip += 1
        # print(' '.join(str(x) if i != pos else '[{}]'.format(x) for i, x in enumerate(rope)), 'skip={}'.format(skip))
    print(rope[0] * rope[1])
process([3, 4, 1, 5], l=5)
process([157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30], l=256)
