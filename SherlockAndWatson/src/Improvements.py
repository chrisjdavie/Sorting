'''
Didn't now that the inverse of j = (i + K)%N is i = (j - K)%N 

Created on 1 Feb 2016

@author: chris
'''

N, K, Q = map(int, raw_input().strip().split())
nums = map(int, raw_input().strip().split())
idx = []
for _ in range(Q):
    i = input()
    print nums[(i - K)%N]