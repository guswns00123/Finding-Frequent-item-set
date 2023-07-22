#!/usr/bin/env python
import sys

check_pairs = {}
file = open("pair_list", "r")
for line in file:
    pair = line.strip()
    check_pairs[pair] = 0

for line1 in sys.stdin:
    line1 = line1.strip()
    word_list = line1.split(' ')
    word_list = list(set(word_list))
    #print(word_list)
    for i in range(len(word_list) - 1):
        for j in range(i+1, len(word_list)):
            if (word_list[i] <= word_list[j]):
                pair = word_list[i] + word_list[j]
            else : pair = word_list[j] + word_list[i]
            #print(pair)
            if pair in check_pairs:
                check_pairs[pair] +=1
                

for pair, cnt in check_pairs.items():
    print("%s\t%s" % (pair, cnt))