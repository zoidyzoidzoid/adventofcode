#!/usr/local/bin/python3
from hashlib import md5

key = 'bgvyzdsv'


def mine_advent_coin(key):
    print('Mining advent coin for key:', key)
    n = 1
    while True:
        hex_hash = md5('{}{}'.format(key, n).encode()).hexdigest()
        if hex_hash.startswith('00000'):
            break
        n += 1
    print('Found hash,', hex_hash, 'with int,', n)

mine_advent_coin('abcdef')
mine_advent_coin('pqrstuv')
mine_advent_coin(key)


def mine_rarer_advent_coin(key):
    print('Mining rarer advent coin for key:', key)
    n = 1
    while True:
        hex_hash = md5('{}{}'.format(key, n).encode()).hexdigest()
        if hex_hash.startswith('000000'):
            break
        n += 1
    print('Found hash,', hex_hash, 'with int,', n)

mine_rarer_advent_coin('abcdef')
mine_rarer_advent_coin('pqrstuv')
mine_rarer_advent_coin(key)
