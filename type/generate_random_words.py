#!/bin/python3

# Program to generate random words + numbers combination
# Paste the words in keybr

import random
import sys

def filter_words(words, max_length=5):
  return list(filter(lambda x: len(x) <= max_length, words))


words = open('./words.txt', 'r').read().split('\n')
words = filter_words(words)
N = len(words)

REQ_WORDS = 1000

sys.stdout = open('./custom_words.txt', 'w+')


for i in range(REQ_WORDS):
  print(words[random.randint(0, N)], random.randint(10, 100), end = ' ')
