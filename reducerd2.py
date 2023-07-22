#!/usr/bin/env python
import sys

cur_pair = None
total = 0
ths = 0.01
total_basket = 4984636
s = ths * total_basket

for line in sys.stdin:
    line = line.strip()
    pair, cnt = line.split("\t")
    if pair != cur_pair:
        if cur_pair is not None:
            if total >= s:
                print("%s\t%s" % (cur_pair, total))
        cur_pair = pair
        total = int(cnt)
    else: total += int(cnt)

print("%s\t%s" % (cur_pair, total))