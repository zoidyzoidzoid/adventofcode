#!/usr/local/bin/python3

from codecs import decode, encode

with open('day8.txt', 'r') as instructions_file:
    strings = instructions_file.read()

strings = [s for s in strings.split('\n') if s]

# strings = [
#     '""',
#     '"abc"',
#     '"aaa\\"aaa"',
#     '"\\x27"'
# ]

total = 0

print('Computing length differences between raw and decoded strings')

for s in strings:
    raw_string = s
    print(raw_string)
    new_string = decode(raw_string, 'unicode_escape')
    print(new_string)
    total += len(raw_string) - len(new_string[1:-1])

print('Total:', total)


total = 0

print('Computing length differences between raw and double encoded strings')

for s in strings:
    raw_string = s
    # print(raw_string)
    new_string = '"{}"'.format(encode(
        s, 'unicode-escape').decode('ascii').replace('"', '\\"'))
    # print(new_string)
    total += len(new_string) - len(raw_string)

print('Total:', total)
