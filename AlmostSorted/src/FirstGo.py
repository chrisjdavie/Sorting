'''
Solving the hackerrank almost sorted puzzle.

https://www.hackerrank.com/challenges/almost-sorted

Okay, so I constrained myself to as close as I could figure O(1*N) 
solution. There are much more straight forwards methods if you use 
sort, and a much more straight forwards method if you store the
wrong entries and then look at those, which would be O(2*N) and far
superior.

---------------------

Given an array with n elements, can you sort this array in ascending order using only one of the following operations?

Swap two elements.
Reverse one sub-segment.
Input Format 
The first line contains a single integer, n, which indicates the size of the array. 
The next line contains n integers separated by spaces.

n  
d1 d2 ... dn  
Constraints 
2≤n≤100000 
0≤di ≤1000000 
All di are distinct.

Output Format 
1. If the array is already sorted, output yes on the first line. You do not need to output anything else.

If you can sort this array using one single operation (from the two permitted operations) then output yes on the first line and then:

a. If you can sort the array by swapping dl and dr, output swap l r in the second line. l and r are the indices of the elements to be swapped, assuming that the array is indexed from 1 to n.

b. Else if it is possible to sort the array by reversing the segment d[l...r], output reverse l r in the second line. l and r are the indices of the first and last elements of the subsequence to be reversed, assuming that the array is indexed from 1 to n.

d[l...r] represents the sub-sequence of the array, beginning at index l and ending at index r, both inclusive.

If an array can be sorted by either swapping or reversing, stick to the swap-based method.

If you cannot sort the array in either of the above ways, output no in the first line.

---------------------

Created on 1 Feb 2016

@author: chris
'''

N = input()
nums = map(int, raw_input().strip().split())

decreasing = False
maybeSwap = False
swap = False
reverse = False
valid = True
nOperations = 0
ind0 = -1
ind1 = -1

def checkSwap(ind0, ind1):
    n0 = nums[ind1]
    n1 = nums[ind0]
    
    valid = True
    if nums[ind0 + 1] < n0:
        valid = False
    if (ind1 != len(nums) - 1 and nums[ind1 + 1] < n1) or n1 < nums[ind1 - 1]:
        valid = False
    
    return valid

def checkReverse(ind0, ind1):
    n0 = nums[ind1]
    n1 = nums[ind0]
    
    valid = True
    if n0 < nums[ind0 - 1]:
        valid = False
    if ind1 != len(nums) - 1 and nums[ind1 + 1] < n1:
        valid = False
        
    return valid
    

for i in range(N-1):
    n0 = nums[i]
    n1 = nums[i+1]
    if n1 < n0 and not decreasing:
        if maybeSwap:
            ind1 = i + 1
            maybeSwap = False
            swap = True
            valid = checkSwap(ind0, ind1)
            nOperations += 1
        else:
            if nOperations > 0:
                nOperations += 1
                break
            decreasing = True
            ind0 = i

            
    if decreasing:
        if n1 > n0:
            decreasing = False
            if i == ind0 + 1:
                if nums[i-2] < n0 and n0 < nums[i-1] and nums[i-1] < n1:
                    ind1 = i
                    swap = True
                    nOperations += 1
                else:
                    ind1 = -1
                    maybeSwap = True
            else:
                # check reverse would ensure sorted
                ind1 = i
                reverse = True
                valid = checkReverse(ind0, ind1)
                nOperations += 1
#     print nOperations, n1 < n0, i, ind0, ind1
    if not valid:
        break

# reverse with final index
if decreasing:
    ind1 = i + 1
    reverse = True
    valid = checkReverse(ind0, ind1)
    nOperations += 1

# swap with final index?
if maybeSwap:
    ind1 = i + 1
    swap = True
    valid = checkSwap(ind0, ind1)
    nOperations += 1
    

# if detected an adjacent reverse, turn into swap
if reverse and ind0 == ind1 - 1:
    reverse = False
    swap = True


# print swap, nOperations, valid, ind0, ind1
if nOperations < 2 and valid:
    print 'yes'
    if reverse:
        print 'reverse', ind0 + 1, ind1 + 1
    if swap:
        print 'swap', ind0 + 1, ind1 + 1
else:
    print 'no'

        
        