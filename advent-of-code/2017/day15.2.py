#!/usr/bin/env python3


def process(a, b):
    A_fact = 16807
    B_fact = 48271
    mod = 2147483647
    count = 0
    for i in range(5000000):
        while True:
            a = (a * A_fact) % mod
            if not a % 4:
                break
        while True:
            b = (b * B_fact) % mod
            if not b % 8:
                break
        a_s = str(''.join(reversed(list(reversed('{:016b}'.format(a)))[:16])))
        b_s = str(''.join(reversed(list(reversed('{:016b}'.format(b)))[:16])))
        if a_s == b_s:
            count += 1
    return count


print(process(65, 8921))
print(process(722, 354))
