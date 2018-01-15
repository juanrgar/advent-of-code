#!/usr/bin/env python

import sys
import re

def print_usage():
    print "main.py <input-file> <1|2>"

class LetterFreq:
    letter = ''
    freq = 0

    def __init__(self, l):
        self.letter = l
        self.freq = 1

    def inc_freq(self):
        self.freq = self.freq + 1

    def compare_to(self, other):
        r = -1 * cmp(self.freq, other.freq)
        if r == 0:
            r = cmp(self.letter, other.letter)
        return r

    def __eq__(self, other):
        return self.letter == other.letter

    def __str__(self):
        return "(" + self.letter + ": " + str(self.freq) + ")"

def is_room_real(room_name, exp_checksum):
    freqs = get_letter_frequencies(room_name)
    freqs_sorted = sorted(freqs, cmp=lambda x,y: x.compare_to(y))
    checksum = ''.join([x.letter for x in freqs_sorted])[:5]

    return exp_checksum == checksum

def get_letter_frequencies(room_name):
    freqs = list()

    for l in room_name:
        if l == '-':
            continue

        lf = LetterFreq(l)
        if lf in freqs:
            freqs[freqs.index(lf)].inc_freq()
        else:
            freqs.append(lf)

    return freqs

def decrypt_room_name(room_name, shift):
    # generated with [chr(x) for x in range(ord('a'), ord('z')+1)]
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    decrypted_name = ""
    for l in room_name:
        if l == '-':
            decrypted_l = ' '
        else:
            decrypted_l = symbols[(symbols.index(l) + shift) % len(symbols)]
        decrypted_name = decrypted_name + decrypted_l

    return decrypted_name

def main(args):
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(-1)

    filename = sys.argv[1]
    part = int(sys.argv[2])

    f = open(filename, "r")
    idata = f.readlines()
    f.close()

    # print idata

    sum_sector_id = 0
    room_names = dict()

    for l in idata:
        room_name = l[:l.rfind('-')]
        sector_id = l[l.rfind('-')+1:l.rfind('[')]
        checksum = l[l.rfind('[')+1:l.rfind(']')]

        if is_room_real(room_name, checksum):
            sum_sector_id = sum_sector_id + int(sector_id)
            decrypted_name = decrypt_room_name(room_name, int(sector_id))
            room_names[decrypted_name] = sector_id

    if part == 1:
        print sum_sector_id
    elif part == 2:
        for r in room_names:
            if 'north' in r and 'object' in r:
                print room_names[r]

if __name__ == "__main__":
    main(sys.argv)
