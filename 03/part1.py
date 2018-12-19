#!/usr/bin/python3

import sys

#1 @ 387,801: 11x22
def parse(data):
    parts = data.split()
    _id = int(parts[0].lstrip("#"))

    left, top = parts[2].rstrip(":").split(",", 1)
    left = int(left)
    top = int(top)

    br, le = parts[3].split("x")
    br = int(br)
    le = int(le)

    return {
        "id": _id,
        "left": left,
        "top": top,
        "le": le,
        "br": br,
    }


# 0: not claimed
# 1: claimed, not counted
# 2: counted
def claim_area(area, parsed_data):
    x_start = parsed_data["left"]
    x_end = x_start + parsed_data["br"]
    y_start = parsed_data["top"]
    y_end = y_start + parsed_data["le"]
    overlap = 0

    for y in range(y_start, y_end):
        for x in range(x_start, x_end):
            if area[y][x] == 0:
                area[y][x] = 1
            elif area[y][x] == 1:
                overlap += 1
                area[y][x] = 2

    return overlap


def main():
    # I am too lazy to find out how large it actually is.
    area = []
    for i in range(0, 2**10):
        x = [0 for i in range(0, 2**10)]
        area.append(x)

    overlap_sum = 0

    for line in sys.stdin:
        data = parse(line)
        overlap_sum += claim_area(area, data)

    print(overlap_sum)


if __name__ == '__main__':
    main()
