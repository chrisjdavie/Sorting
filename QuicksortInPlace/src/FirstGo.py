'''

Solving the hackerrank Quicksort In-Place puzzle.

https://www.hackerrank.com/challenges/quicksort3

----------------------

The previous version of Quicksort was easy to understand, but it was not optimal. It required copying the numbers into other arrays, which takes up space and time. To make things faster, one can create an "in-place" version of Quicksort, where the numbers are all sorted within the array itself.

Challenge 
Create an in-place version of Quicksort. You need to follow Lomuto Partitioning method.

Guideline 
Instead of copying the array into multiple sub-arrays, use indices to keep track of the different sub-arrays. You can pass the indices to a modified partition method. The partition method should partition the sub-array and then return the index location where the pivot gets placed, so you can then call partition on each side of the pivot.

Always select the last element in the 'sub-array' as a pivot.
Partition the left side and then the right side of the sub-array.
Print out the whole array at the end of every partitioning method.
An array of length 1 or less will be considered sorted, and there is no need to sort or to print them.
Since you cannot just create new sub-arrays for the elements, partition method will need to use another trick to keep track of which elements are greater and which are lower than the pivot.

The In-place Trick

If an element is lower than the pivot, you should swap it with a larger element on the left-side of the sub-array.
Greater elements should remain where they are.
At the end of the partitioning method, the pivot should be swapped with the first element of the right partition, consisting of all larger elements, of the sub-array.
To ensure that you don't swap a small element with another small element, use an index to keep track of the small elements that have already been swapped into their "place".

Input Format 
There will be two lines of input:

n - the size of the array
ar - the n numbers of the array
Output Format 
Print the entire array on a new line at the end of every partitioning method.

----------------------

Created on 27 Jan 2016

@author: chris
'''
def partition(ar,iStart,iEnd):
    key = ar[iEnd-1]
    iLtPart = iStart
    for i in range(iStart,iEnd-1):
        if ar[i] < key:
            tmp = ar[iLtPart]
            ar[iLtPart] = ar[i]
            ar[i] = tmp
            iLtPart += 1
    
    ar[iEnd-1] = ar[iLtPart]
    ar[iLtPart] = key
    
    for a in ar: print a,
    print
    
    if iLtPart - iStart > 1:
        partition(ar, iStart, iLtPart)
    
    iGtPart = iLtPart + 1
    if iEnd - (iGtPart) > 1:
        partition(ar, iGtPart, iEnd)
    

input()
ar = map(int,raw_input().strip().split())
partition(ar,0,len(ar))
