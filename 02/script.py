#!/usr/bin/python3

import sys

# part 1
twos = 0
threes = 0
lines = sys.stdin.read().split()

for line in lines:
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

# part 2
for line in lines:
    for candidate in lines:
        differ = 0
        for a, b in zip(candidate, line):
            if a != b:
                differ += 1

        if differ == 1:
            answer = ""
            for a, b in zip(candidate, line):
                if a == b:
                    answer += a

            print(answer)

            sys.exit()
