#!/usr/bin/env python3

import re
import sys

RE_KVP = re.compile('(.*):(.*)')

FIELDS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
    ]

def read_passports(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    passports = list()
    p = dict()
    i = 0

    for l in lines:
        l = l.strip()
        if len(l) > 0:
            fields = l.split(' ')
            for f in fields:
                m = RE_KVP.match(f)
                p[m.group(1)] = m.group(2)
        else:
            passports.append(p)
            p = dict()

    passports.append(p)
    return passports

def validate_passports(passports):
    valid = list()
    for p in passports:
        missing = [x for x in FIELDS if x not in p.keys()]
        if len(missing) == 0:
            valid.append(p)
        elif len(missing) == 1 and missing[0] == 'cid':
            valid.append(p)

    return valid

def main():
    filename = sys.argv[1]
    passports = read_passports(filename)
    valid = validate_passports(passports)
    for p in valid:
        print(p)
    print(len(valid))

if __name__ == "__main__":
    main()
