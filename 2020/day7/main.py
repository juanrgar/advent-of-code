#!/usr/bin/env python3

import sys

class BagDownstreamRef(object):
    def __init__(self) -> None:
        super().__init__()
        self.bag = None
        self.amount = 0

class Bag(object):
    def __init__(self) -> None:
        super().__init__()
        self.color = ''
        self.bags_down = list()
        self.bags_up = list()

def read_bags(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    bags = dict()

    for l in lines:
        l = l.strip()
        bags_i = l.index('bags')
        color = l[:bags_i-1]
        if color in bags.keys():
            b = bags[color]
        else:
            b = Bag()
            b.color = color

        contain_i = l.index('contain')
        subbags = l[contain_i + len('contain '):]
        if subbags != 'no other bags.':
            subbags = subbags.split(',')
            for sb in subbags:
                sb = sb.strip()
                amount_i = sb.index(' ')
                amount = int(sb[:amount_i])
                color_i = sb.index('bag', amount_i)
                color = sb[amount_i+1:color_i-1]
                bd = BagDownstreamRef()
                bd.amount = amount
                if color in bags.keys():
                    bd.bag = bags[color]
                else:
                    bd.bag = Bag()
                    bd.bag.color = color
                    bags[color] = bd.bag
                b.bags_down.append(bd)
                bd.bag.bags_up.append(b)

        bags[b.color] = b

    return bags

def find_bag(bags, b):
    if len(b.bags_up) == 0:
        return [b.color]
    acc = [b.color]
    for bb in b.bags_up:
        acc.extend(find_bag(bags, bb))
    acc = list(dict.fromkeys(acc))
    return acc

def count_bags(bags, b):
    if len(b.bags_down) == 0:
        return 1

    acc = 1
    for bd in b.bags_down:
        acc += bd.amount * count_bags(bags, bd.bag)
    return acc

def main():
    filename = sys.argv[1]
    bags = read_bags(filename)
    acc = 0
    acc = find_bag(bags, bags['shiny gold'])
    print(len(acc) - 1)
    acc = count_bags(bags, bags['shiny gold'])
    print(acc - 1)

if __name__ == "__main__":
    main()
