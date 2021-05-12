#!/usr/bin/env python3

import itertools
import sys

PREAMBLE=25

def read_sequence(filename):
    seq = list()
    with open(filename, 'r') as f:
        for l in f.readlines():
            seq.append(int(l.strip()))
    return seq

def find_first_invalid(seq):
    slice_first = 0
    valid = [True] * PREAMBLE
    valid.extend([False] * (len(seq) - PREAMBLE))
    for n in seq[PREAMBLE:]:
        print('===================')
        print(n)
        possible = [i for i in range(len(seq)) if valid[i]]
        combs = itertools.combinations(possible, 2)
        found = False
        for c in combs:
            s = seq[c[0]] + seq[c[1]]
            if s == n:
                print(str(c[0]) + ' ' + str(c[1]))
                found = True
#                valid[c[0]] = False
#                valid[c[1]] = False
                valid[slice_first] = False
                valid[slice_first + PREAMBLE] = True
                print(valid)
                slice_first += 1
                print(slice_first)
                break
        if not found:
            return n

def main():
    filename = sys.argv[1]
    seq = read_sequence(filename)
    print(seq)
    inv = find_first_invalid(seq)
    print(inv)

if __name__ == "__main__":
    main()

