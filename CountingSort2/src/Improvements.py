'''
Using collections and counter. Yay inbuilt libraries!

Created on 30 Jan 2016

@author: chris
'''

import collections

n = input()
ar = []
counts = collections.Counter(ar)

for i in range(0, 100):
    for _ in range(counts[i]):
        print i,