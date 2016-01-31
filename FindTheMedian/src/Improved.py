'''
Missed a constraint - number of elements is odd

Created on 31 Jan 2016

@author: chris
'''

input()
nums = map(int, raw_input().strip().split())
nums.sort()
median = nums[len(nums)/2]
print median