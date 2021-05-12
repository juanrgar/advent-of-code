#!/usr/bin/env python3

import sys

def read_adapter_jolts(filename) -> list:
    jolts = list()
    with open(filename, 'r') as f:
        for l in f.readlines():
            jolts.append(int(l.strip()))

    return jolts

def connect_adapters(jolts) -> int:
    jolts.sort()
    print(jolts)
    jolts.insert(0, 0)
    print(jolts)
    diffs = list()
    for i in range(len(jolts) - 1):
        diffs.append(jolts[i+1] - jolts[i])
    diff_1 = len([j for j in diffs if j == 1])
    diff_3 = len([j for j in diffs if j == 3]) + 1
    return diff_1 * diff_3

def main():
    filename = sys.argv[1]
    jolts = read_adapter_jolts(filename)
    print(jolts)
    diff = connect_adapters(jolts)
    print(diff)

if __name__ == "__main__":
    main()
