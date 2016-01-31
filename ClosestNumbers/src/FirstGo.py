'''
Created on 31 Jan 2016

@author: chris
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
numsIn = map(int, raw_input().strip().split())

from collections import Counter
numsCounts = Counter(numsIn)
uniqNums = numsCounts.key().sort()

print uniqNums