#!/usr/bin/python3

import sys
import time

data = sys.stdin.read().strip()
deleted = [False for i in range(0, len(data))]
run = True

def data_generator():
    for i in range(0, len(data)):
        if deleted[i]:
            continue

        yield i, data[i]


while run:
    run = False
    prev = ''
    prev_i = 0

    for i, cur in data_generator():
        if (prev.lower() == cur.lower()) and prev != cur:
            deleted[i] = True
            deleted[prev_i] = True

            run = True
            prev = ''
            continue

        prev = cur
        prev_i = i

size = 0
for _, cur in data_generator():
    print(cur, end='')
    size += 1
print()
print(size)
