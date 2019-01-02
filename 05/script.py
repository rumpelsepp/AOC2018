#!/usr/bin/python3

import sys


def data_generator(data, deleted):
    for i in range(0, len(data)):
        if deleted[i]:
            continue

        yield i, data[i]


def run(data):
    deleted = [False for i in range(0, len(data))]
    run = True
    while run:
        run = False
        prev = ''
        prev_i = 0

        for i, cur in data_generator(data, deleted):
            if (prev.lower() == cur.lower()) and prev != cur:
                deleted[i] = True
                deleted[prev_i] = True

                run = True
                prev = ''
                continue

            prev = cur
            prev_i = i

    return len(list(data_generator(data, deleted)))


def main():
    data = sys.stdin.read().strip()

    # part 1
    print(run(data))

    # part 2
    best = len(data)
    for i in range(ord('a'), ord('z')+1):
        reduced_data = data.replace(chr(i), '').replace(chr(i).upper(), '')
        length = run(reduced_data)
        if length < best:
            best = length

        print(f'{chr(i)}: got length: {length}')

    print(f'best is: {best}')


if __name__ == '__main__':
    main()
