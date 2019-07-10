#!/usr/bin/env python3


def process(a, b):
    A_fact = 16807
    B_fact = 48271
    mod = 2147483647
    count = 0
    for i in range(40000000):
        a = (a * A_fact) % mod
        b = (b * B_fact) % mod
        a_s = str(''.join(reversed(list(reversed('{:016b}'.format(a)))[:16])))
        b_s = str(''.join(reversed(list(reversed('{:016b}'.format(b)))[:16])))
        if a_s == b_s:
            count += 1
    return count


print(process(65, 8921))
print(process(722, 354))
