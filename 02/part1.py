#!/usr/bin/python3

import sys

twos = 0
threes = 0

for line in sys.stdin:
    chars = {}
    line = line.strip()
    got_twos = False
    got_threes = False

    for char in line:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for credits in chars.values():
        if credits == 2 and not got_twos:
            twos += 1
            got_twos = True
        elif credits == 3 and not got_threes:
            threes += 1
            got_threes = True

print(twos * threes)
