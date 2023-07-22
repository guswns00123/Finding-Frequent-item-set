#!/usr/bin/env python
import sys
cur_pair = None
for line in sys.stdin:
    line = line.strip()
    pair, count = line.split('\t')
    if pair != cur_pair:
        if cur_pair is not None:
            print ("%s" % (cur_pair))
        cur_pair = pair


print("%s" % (cur_pair))