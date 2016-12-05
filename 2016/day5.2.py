#!/usr/bin/env python3.6
import fileinput
from collections import *
from functools import *
from hashlib import md5
from itertools import *

password = ['_' for i in range(8)]

for line in fileinput.input():
    line = line.strip()
    index = 0
    while True:
        hash = md5((line + str(index)).encode()).hexdigest()
        if hash[:5] == '00000' and hash[5].isnumeric() and int(hash[5]) < 8 and password[int(hash[5])] == '_':
            password[int(hash[5])] = hash[6]
            # print(password)
        index += 1
        if '_' not in password:
            break
print('{}'.format(''.join(password)))
