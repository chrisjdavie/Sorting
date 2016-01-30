'''
Created on 30 Jan 2016

@author: chris
'''
import collections

ar = []
for _ in range(input()):
    a, _ = raw_input().strip().split()
    ar.append(int(a))

counts = collections.Counter(ar)

cum = 0
for i in range(0, 100):
    cum += counts[i]
    print cum