#!/usr/bin/python3

import sys

# part 1
data = [int(a) for a in sys.stdin.readlines()]
sum_ = 0
for line in data:
    sum_ += line

print(sum_)

# part 2
iterations = 0
f = 0
seen_frequencies = set()
seen_frequencies.add(0)

while True:
    for line in data:
        f += line

        if f in seen_frequencies:
            print(f)
            sys.exit(0)

        seen_frequencies.add(f)

    iterations += 1
