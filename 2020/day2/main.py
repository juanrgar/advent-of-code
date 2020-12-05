#!/usr/bin/env python3

import re
import sys

PASSWORD_RE=re.compile('(\d+)-(\d+) (\w): (.*)')
# 1-7 j: vrfjljjwbsv

def validate_password(l):
    l = l.strip()
    m = PASSWORD_RE.match(l)
    if not m:
        print('Not matched: ' + l)
        return False
    else:
        min_occ = int(m.group(1))
        max_occ = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)
        # nb_occ = password.count(letter)
        # return (nb_occ >= min_occ) and (nb_occ <= max_occ)
        letter0 = password[min_occ - 1]
        letter1 = password[max_occ - 1]
        return ((letter0 == letter) and (letter1 != letter)) or ((letter0 != letter) and (letter1 == letter))

def main():
    filename = sys.argv[1]
    v = 0
    with open(filename, 'r') as f:
        lines = f.readlines()

    for l in lines:
        if validate_password(l):
            v += 1

    print(v)

if __name__ == "__main__":
    main()
