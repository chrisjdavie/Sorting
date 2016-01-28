'''
Solving the hackerrank Running Time of Algorithm puzzle.

https://www.hackerrank.com/challenges/runningtime

Doesn't really, it compares the number of array operations. Quicksort,
at least this one, on an ordered array becomes dominated by comparisons.

Also, needed to be dead careful about which alg version I used, which
was surprising, as I thought they were equivalent. But I might be
getting something wrong, not sure.

----------------------

The running time of Quicksort will depend on how balanced the partitions are. If you are unlucky and select the greatest or the smallest element as the pivot, then each partition will separate only one element at a time, so the running time will be similar to Insertion Sort.

However, Quicksort will usually pick a pivot that is mid-range, and it will partition the array into two parts. Let's assume Partition is lucky and it always picks the median element as the pivot. What will be the running time in such a case?

Running Time of Recursive Methods 
Quicksort is a recursive method, so we will have to use a technique to calculate the total running time of all the method calls. We can use a version of the "Recursion Tree Method" to estimate the running time for a given array of N elements.


Each time partition is called on a sub-array, each element in the sub-array needs to be compared to the pivot element. Since all the sub-arrays are passed to partition, there will be N total operations for each level of the tree.

How many levels will it take for the Quicksort to finish? Since we assume it always picks the middle element, the array will be split into two equal halves each time. So it will take log(N) splits until we get single elements in the sub-arrays. Since there are log(N) levels and each one involves N operations, the total running time for Quicksort will be Nlog(N).

In real sorting, Quicksort won't always pick the exact middle element. But as long as it's regularly picking elements near the median value, it will have a running time better than Insertion Sort. To make sure that Quicksort works well on most inputs, the real-world implementations do not pick the same index as pivot each time. They use some other technique, e.g. picking a random element. There are other techniques, as well, that can be used to improve Quicksort. The Java Arrays class uses a modified version of Quicksort to sort primitives.

Notice that O(Nxlog(N)) of Quicksort is much much faster than the O(N2) of Insertion Sort. For example, for an array of one million elements, N2 =1012, while Nxlog(N) is approximately 2x107, a much more manageable number.

Challenge 
In practice, how much faster is Quicksort (in-place) than Insertion Sort? Compare the running time of the two algorithms by counting how many swaps or shifts each one takes to sort an array, and output the difference. You can modify your previous sorting code to keep track of the swaps. The number of swaps required by Quicksort to sort any given input have to be calculated. Keep in mind that the last element of a block is chosen as the pivot, and that the array is sorted in-place as demonstrated in the explanation below.

Any time a number is lower than the partition, it should be "swapped", even if it doesn't actually move to a different location. Also ensure that you count the swap when the pivot is moved into place. The count for Insertion Sort should be the same as the previous challenge, where you just count the number of "shifts".

Note 
Please use Lomuto Partition for this challenge.

Input Format 
There will be two lines of input:

n - the size of the array
ar - n numbers that make up the array
Output Format 
Output one integer D, where D= (insertion sort shifts) - (quicksort swaps)

----------------------

Created on 28 Jan 2016

@author: chris
'''
import copy

# Quicksort
def quicksort(ar,iStart,iEnd):
    n = 0
    key = ar[iEnd-1]
    iLtPart = iStart
    for i in range(iStart,iEnd-1):
        if ar[i] < key:
            n += 1
            tmp = ar[iLtPart]
            ar[iLtPart] = ar[i]
            ar[i] = tmp
            iLtPart += 1
    
    n += 1
    ar[iEnd-1] = ar[iLtPart]
    ar[iLtPart] = key
    
    if iLtPart - iStart > 1:
        nTmp = quicksort(ar, iStart, iLtPart)
        n += nTmp
    
    iGtPart = iLtPart + 1
    if iEnd - (iGtPart) > 1:
        nTmp = quicksort(ar, iGtPart, iEnd)
        n += nTmp
    
    return n
        

# Insertion sort
def insertionSort(l):
    N = 0
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (j >= 0) and (l[j] > key):
            N += 1
            tmp = l[j]
            l[j] = l[j+1]
            l[j+1] = tmp
            
            j -= 1
        l[j+1] = key
    return N


input()
ar = map(int,raw_input().strip().split())
nInsert = insertionSort(copy.copy(ar))
nQuick = quicksort(copy.copy(ar),0,len(ar))
print nInsert - nQuick
