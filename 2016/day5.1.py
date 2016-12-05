#!/usr/bin/env python3.6
import fileinput
from collections import *
from functools import *
from hashlib import md5
from itertools import *

password = ''

for line in fileinput.input():
    line = line.strip()
    index = 0
    while True:
        hash = md5((line + str(index)).encode()).hexdigest()
        if hash[:5] == '00000':
            password += hash[5]
        index += 1
        if len(password) == 8:
            break

print('{}'.format(password))
