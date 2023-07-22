#!/usr/bin/env python
import sys
from itertools import *

item ={}
check_item = {}
ths = 0.005
total_basket = 0
basket_list =[]
for line in sys.stdin:
    line = line.strip()
    word_list = line.split(' ')
    total_basket += 1
    word_list = list(set(word_list))
    basket_list.append(word_list)
    for word in word_list:
        if word in item:
            item[word] += 1
        else:
            item[word] = 1

s = ths * total_basket

for word, cnt in item.items():
    if cnt >= s:
        check_item[word] = cnt

check_triplet = {}
triplets =[]
for basket in basket_list:
    triplet_list = list(permutations(basket, 3))
    #triplet_list = [sorted(list(item)) for item in triplet_list]
    triplet_list = list(set([tuple(sorted(list(item))) for item in triplet_list]))
    #print([sorted(list(item)) for item in triplet_list])
    #print(list(set([tuple(item) for item in triplet_list])))

    for triplet in triplet_list:
        if triplet in check_triplet:
            check_triplet[triplet] += 1
        else:
            check_triplet[triplet] = 1


for triplet, cnt in check_triplet.items():

    if (cnt >= s):
        print("%s\t%s" %(triplet, cnt))