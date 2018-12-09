#!/usr/bin/env python3

import sys

def main(args):
    if len(sys.argv) != 2:
        sys.exit(-1)

    filename = sys.argv[1]

    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    lines_len = len(lines)
    i = 0
    cur_freq = 0
    accum_freq = 0
    freq_hits = [cur_freq]
    rep_freq = 0
    rep_freq_hit = False

    while not rep_freq_hit:
        for l in lines:
            cur_freq += int(l.strip())
            i += 1
            if i == lines_len:
                accum_freq = cur_freq

            if (not rep_freq_hit) and (cur_freq in freq_hits):
                rep_freq = cur_freq
                rep_freq_hit = True
            else:
                freq_hits.append(cur_freq)

    print(str(accum_freq))
    print(str(rep_freq))

if __name__ == "__main__":
    main(sys.argv)
