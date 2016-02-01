'''
Created on 1 Feb 2016

@author: chris
'''

input()
nums = map(int, raw_input().strip().split())

decreasing = False
maybeSwap = False
swap = False
rev = False
nOperations = 0
ind0 = -1
ind1 = -1

for i, n0, n1 in enumerate(zip(nums[:-1],nums[1:])):
    if n1 < n0:
        if nOperations > 0:
            nOperations += 1
            break
        decreasing = True
        ind0 = i
        if maybeSwap:
            swap = True
            ind1 = i + 1
            nOperations += 1
        
    if decreasing:
        if n1 > n0:
            decreasing = False
            if i == ind0 + 1:
                ind1 = -1
                maybeSwap = True
            else:
                ind1 = i
                rev = True
                nOperations += 1
    
# reverse with final index

# swap with final index?

# if detected an adjacent reverse, turn into swap


if nOperations < 1:
    print 'yes'
    if rev:
        print 'reverse', ind0, ind1
    if swap:
        print 'swap', ind0, ind1
else:
    print 'no'

        
        