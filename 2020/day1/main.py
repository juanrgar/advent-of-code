#!/usr/bin/env python3

import sys

def main():
    filename = sys.argv[1]

    entries = list()

    with open(filename, 'r') as f:
        lines = f.readlines()
        for l in lines:
            entries.append(int(l.strip()))

    for e0 in entries:
        for e1 in entries:
            for e2 in entries:
                if (e0 + e1 + e2) == 2020:
                    print(e0 * e1 * e2)
                    sys.exit(0)

if __name__ == "__main__":
    main()
