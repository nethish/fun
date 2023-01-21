#!/bin/python3

import random
import sys

FILE = sys.argv[1]

REQ_WORDS = 1000

def filter_words(words, max_length=5):
  return list(filter(lambda x: len(x) <= max_length, words))


words = open(FILE, 'r').read().split('\n')
# words = filter_words(words)
N = len(words)

print("Number of words:", N)

# nums = [4, 5, 6, 7, 45, 56, 67, 46, 47, 57]
# nums = [str(i) for i in nums]
# nums += [i[::-1] for i in nums]


def print_rand(word_list):
  print(word_list[random.randint(0, len(word_list) - 1)], end = ' ')


sys.stdout = open('./custom_words.txt', 'w+')
for i in range(REQ_WORDS):
  print_rand(words)
