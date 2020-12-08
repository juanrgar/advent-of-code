#!/usr/bin/env python3

import sys

def read_seats(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    seats = list()
    for l in lines:
        l = l.strip()
        m = 0
        M = 128
        r = 0
        for c in l[:7]:
            h = ((M - m) / 2) + m
            if c == 'F':
                M = h
                r = m
            elif c == 'B':
                m = h
                r = M

        m = 0
        M = 8
        col = 0
        for c in l[7:]:
            h = ((M - m) / 2) + m
            if c == 'F':
                M = h
                col = m
            elif c == 'B':
                m = h
                col = M

        seats.append(int(r * 8 + col))

    return seats

def main():
    filename = sys.argv[1]
    seats = read_seats(filename)

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
