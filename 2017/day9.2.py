#!/usr/bin/env python3
# coding: utf-8


def process(line):
    res = 0
    skip = False
    garbage = False
    g = 0
    counted = set()
    while True:
        depth = 0
        try_again = False
        for index, i in enumerate(line):
            if skip:
                skip = False
            elif i == '!':
                skip = True
            elif i == '<':
                if garbage:
                    g += 1
                    continue
                garbage = True
                g_start = index
            elif i == '>':
                garbage = False
                line = line[:g_start] + line[index + 1:]
                try_again = True
                break
            elif garbage:
                g += 1
            elif i == '{':
                depth += 1
            elif i == '}':
                if index in counted:
                    depth -= 1
                else:
                    # print('Closing brackets of depth', depth)
                    counted.add(index)
                    res += depth
                    depth -= 1
        if not try_again:
            break
    # print(''.join(line))
    return g


print(process('<>'), '0 characters.')
print(process('<random characters>'), '17 characters.')
print(process('<<<<>'), '3 characters.')
print(process('<{!>}>'), '2 characters.')
print(process('<!!>'), '0 characters.')
print(process('<!!!>>'), '0 characters.')
print(process('<{o"i!a,<{i<a>'), '10 characters.')

print(process(open('day9.txt').read().strip()), 'characters')
