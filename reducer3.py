#!/usr/bin/env python
import sys
cur_triplet = None
total = 1
ths = 0.005
total_basket = 4984636
s = ths * total_basket
#s = 1
for line in sys.stdin:
    triplet, cnt = line.strip().split("\t")
    cnt = int(cnt)
    if triplet != cur_triplet:
        if cur_triplet is not None:
            if total >= s:
                print ("%s\t%s" % (cur_triplet,total))
        total = cnt
        cur_triplet = triplet
    else: total += cnt

if total >= s:
    print("%s\t%s" % (cur_triplet, total))