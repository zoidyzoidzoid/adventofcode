#!/usr/bin/env python
# coding: utf-8


def process(inp):
    output = [chr(ord('a') + i) for i in range(16)]
    for i in inp.split(','):
        if i[0] == 's':
            pos = int(i[1:])
            output = output[-pos:] + output[:-pos]
        elif i[0] == 'x':
            l, r = i[1:].split('/')
            l, r = int(l), int(r)
            output[l], output[r] = output[r], output[l]
        elif i[0] == 'p':
            l, r = i[1:].split('/')
            l, r = output.index(l), output.index(r)
            output[l], output[r] = output[r], output[l]
    return ''.join(output)

print(process('s1'))
print(process('x3/4'))
print(process('pe/b'))
print(process(open('day16.txt').read()))
