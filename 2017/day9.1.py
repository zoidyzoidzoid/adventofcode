#!/usr/bin/env python3
# coding: utf-8


def process(line):
    res = 0
    skip = False
    garbage = False
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
                    continue
                garbage = True
                g_start = index
            elif i == '>':
                garbage = False
                line = line[:g_start] + line[index + 1:]
                try_again = True
                break
            elif garbage:
                continue
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
    return res


lines = """{}
{{{}}}
{{},{}}
{{{},{},{{}}}}
{<a>,<a>,<a>,<a>}
{{<ab>},{<ab>},{<ab>},{<ab>}}
{{<!!>},{<!!>},{<!!>},{<!!>}}
{{<a!>},{<a!>},{<a!>},{<ab>}}""".strip().split()


for line in lines:
    print(process(list(line)))

print(process(open('day9.txt').read().strip()))
