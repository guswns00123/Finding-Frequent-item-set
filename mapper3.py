#!/usr/bin/python3
import sys

ths = 0.005
freq_pairs = {}
#file = open("./hw2/testres", "r")
file = open("result_pair.txt", "r")
freq_word = []
for line in file:
    pair,cnt = line.strip().split("\t")
    words = pair.split(" ")
    for word in words:
        if word not in freq_word:
            freq_word.append(word)
        else: continue

        
# print(freq_word)
# freq_triplets = {}
for line in sys.stdin:
    line = line.strip()
    word_list = line.split(' ')
    # total_basket += 1
    word_list = list(set(word_list) & set(freq_word))
    #print(word_list)
    # basket_list.append(word_list)
    for i in range(len(word_list)-2):
        for j in range(i+1, len(word_list)-1):
            for k in range(j+1, len(word_list)):
                tmp_arr = []
                tmp_arr.append(word_list[i])
                tmp_arr.append(word_list[j])
                tmp_arr.append(word_list[k])
                tmp_arr.sort()
                triplet = tmp_arr[0] + " " + tmp_arr[1] + " " + tmp_arr[2]
                print("%s\t1" %(triplet))









