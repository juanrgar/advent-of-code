#!/usr/bin/env python3

import re
import sys

RE_KVP = re.compile('(.*):(.*)')

RE_YEAR = re.compile('^\d\d\d\d$')
RE_HGT = re.compile('^(\d+)([a-z]{2})$')
RE_HCL = re.compile('^#[0-9a-f]{6}$')
RE_PID = re.compile('^[0-9]{9}$')

BYR_MIN = 1920
BYR_MAX = 2002
IYR_MIN = 2010
IYR_MAX = 2020
EYR_MIN = 2020
EYR_MAX = 2030
HGT_CM_MIN = 150
HGT_CM_MAX = 193
HGT_IN_MIN = 59
HGT_IN_MAX = 76
ECL_VALUES = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

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
        if validate_passport(p):
            valid.append(p)
    return valid

def validate_passport(p):
    missing = [x for x in FIELDS if x not in p.keys()]
    has_all_fields = (len(missing) == 0) or (len(missing) == 1 and missing[0] == 'cid')

    if not has_all_fields:
        return False

    return check_byr(p) and check_iyr(p) and check_eyr(p) and check_hgt(p) and check_hcl(p) and check_ecl(p) and check_pid(p)

def check_byr(p):
    return check_year(p, 'byr', BYR_MIN, BYR_MAX)

def check_iyr(p):
    return check_year(p, 'iyr', IYR_MIN, IYR_MAX)

def check_eyr(p):
    return check_year(p, 'eyr', EYR_MIN, EYR_MAX)

def check_year(p, k, m, M):
    s = p[k]
    if len(s) != 4:
        return False
    v = int(s)
    return (v >= m) and (v <= M)

def check_hgt(p):
    s = p['hgt']
    m = RE_HGT.match(s)
    if m is None:
        return False
    u = m.group(2)
    v = int(m.group(1))
    if u == 'cm':
        return (v >= HGT_CM_MIN) and (v <= HGT_CM_MAX)
    elif u == 'in':
        return (v >= HGT_IN_MIN) and (v <= HGT_IN_MAX)
    return False

def check_hcl(p):
    s = p['hcl']
    m = RE_HCL.match(s)
    if m is None:
        return False
    return True

def check_ecl(p):
    s = p['ecl']
    return s in ECL_VALUES

def check_pid(p):
    s = p['pid']
    m = RE_PID.match(s)
    return m is not None

def main():
    filename = sys.argv[1]
    passports = read_passports(filename)
    valid = validate_passports(passports)
    for p in valid:
        print(p)
    print(len(valid))

if __name__ == "__main__":
    main()
