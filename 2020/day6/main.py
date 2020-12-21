#!/usr/bin/env python3

import sys

class GroupAnswers(object):
    def __init__(self):
        self.nb_members = 0
        self.answers = dict()
        self.all_answers = list()

def read_answers(filename):
    lines = list()
    with open(filename, 'r') as f:
        lines = f.readlines()

    ans = list()
    new_group = True
    for l in lines:
        if new_group:
            ans_group = GroupAnswers()
            new_group = False
        l = l.strip()
        if len(l) == 0:
            ans.append(ans_group)
            new_group = True
        else:
            ans_group.answers[ans_group.nb_members] = l
            ans_group.nb_members += 1
            for c in l:
                if c not in ans_group.all_answers:
                    ans_group.all_answers.append(c)

    ans.append(ans_group)

    return ans


def main():
    filename = sys.argv[1]
    ans = read_answers(filename)
    yes_or = 0
    for g in ans:
        yes_or += len(g.all_answers)
    print(yes_or)

    yes_and = 0
    for g in ans:
        for c in g.all_answers:
            acc = 0
            for p in g.answers.values():
                if c in p:
                    acc += 1
            if acc == g.nb_members:
                yes_and += 1

    print(yes_and)


if __name__ == "__main__":
    main()
