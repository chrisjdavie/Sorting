'''
Solving the hackerrank Find The Median puzzle.

https://www.hackerrank.com/challenges/find-median

It will take longer to build this package than solve.

----------------------

n the Quicksort challenges, you sorted an entire array. Sometimes, you just need specific information about a list of numbers, and doing a full sort would be unnecessary. Can you figure out a way to use your partition code to find the median in an array?

Challenge 
Given a list of numbers, can you find the median?

Input Format 
There will be two lines of input:

n - the size of the array
ar - n numbers that makes up the array
Output Format 
Output one integer, the median.

----------------------

Created on 31 Jan 2016

@author: chris
'''

input()
nums = map(int, raw_input().strip().split())
nums.sort()
if len(nums)%2 == 0:
    median = (nums[len(nums)/2] - nums[len(nums)/2+1])/2.0
else:
    median = nums[len(nums)/2]
print median