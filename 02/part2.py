#!/usr/bin/python3

import sys

lines = sys.stdin.read().split()

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
