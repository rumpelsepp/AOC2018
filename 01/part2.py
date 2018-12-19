#!/usr/bin/python3

import sys

iterations = 0
f = 0
seen_frequencies = set()
seen_frequencies.add(0)
data = [int(a) for a in sys.stdin.readlines()]

while True:
    for line in data:
        f += line

        if f in seen_frequencies:
            print(f)
            sys.exit(0)

        seen_frequencies.add(f)

    iterations += 1
