'''
Created on 4 Feb 2016

@author: chris
'''
from collections import Counter

for _ in input():
    input()
    nums = map(int, raw_input().strip().split())
    counts = Counter(nums)
    print counts