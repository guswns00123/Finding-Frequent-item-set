#!/usr/bin/env python
import sys
import gc

item ={}
check_item = {}
ths = 0.01
total_basket = 0
basket_list =[]
hash_table = [0 for i in range(100000)]
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
    for i in range(len(word_list) -1):
        for j in range(i+1, len(word_list)):
            if (word_list[i] <= word_list[j]):
                pair = word_list[i] + " " + word_list[j]
            else : pair = word_list[j] + " " + word_list[i]
            hash_index = hash(pair) % 100000
            #print(hash_index)
            hash_table[hash_index] += 1


s = ths * total_basket

for word, cnt in item.items():
    if cnt >= s:
        check_item[word] = cnt
# print(check_item)
del item
gc.collect()

check_pairs ={}
for basket in basket_list:
    for i in range(len(basket)-1):
        for j in range(i+1, len(basket)):
            if (basket[i] in check_item) and (basket[j] in check_item):
                if (basket[i] <= basket[j]):
                    pair = basket[i] + " " +basket[j]
                else : pair = basket[j] + " " + basket[i]
                
                hash_index = hash(pair) % 100000
                if hash_table[hash_index] >= s:
                    if pair in check_pairs:
                        check_pairs[pair] += 1
                    else: check_pairs[pair] = 1

# print(check_pairs)
for pair, cnt in check_pairs.items():
    if (cnt >= s):
        print("%s\t%s" %(pair, cnt))