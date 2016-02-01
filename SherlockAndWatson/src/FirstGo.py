'''
Created on 1 Feb 2016

@author: chris
'''

N, K, Q = raw_input().strip().split()
nums = map(int, raw_input().strip().split())
idx = []
for _ in range(Q):
    idx.append(input())

numsRot = [0]*N

for i, n in enumerate(nums):
    numsRot[i + K&N] = n

for i in idx:
    print numsRot[i]