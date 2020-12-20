#!/usr/bin/env python3

import sys

def read_seats(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    seats = list()
    for l in lines:
        l = l.strip()
        m = 0
        M = 127
        for c in l[:7]:
            if c == 'F':
                M = ((M - m + 1) / 2) - 1 + m
            elif c == 'B':
                m = ((M - m + 1) / 2) + m

        r = m

        m = 0
        M = 8
        col = 0
        for c in l[7:]:
            if c == 'L':
                M = ((M - m + 1) / 2) - 1 + m
            elif c == 'R':
                m = ((M - m + 1) / 2) + m

        col = m

        seats.append(int(r * 8 + col))

    return seats

def main():
    filename = sys.argv[1]
    seats = read_seats(filename)
    print(max(seats))

    free = [x for x in range(128 * 8) if x not in seats]

    for s in free:
        if s == 0:
            continue
        elif s == ((128 * 8) - 1):
            continue

        n = s + 1
        p = s - 1
        if (n in seats) and (p in seats):
            print(s)

if __name__ == "__main__":
    main()
