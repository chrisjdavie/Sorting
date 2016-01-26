'''
Solving the hackerrank puzzle Quicksort part two.

https://www.hackerrank.com/challenges/quicksort2

----------------------

In the previous challenge, you wrote a partition method to split an array into two sub-arrays, one containing smaller elements and one containing larger elements than a given number. This means you 'sorted' half the array with respect to the other half. Can you repeatedly use partition to sort an entire array?

Guideline 
In Insertion Sort, you simply went through each element in order and inserted it into a sorted sub-array. In this challenge, you cannot focus on one element at a time, but instead must deal with whole sub-arrays, with a strategy known as "divide and conquer".

When partition is called on an array, two parts of the array get 'sorted' with respect to each other. If partition is then called on each sub-array, the array will now be split into four parts. This process can be repeated until the sub-arrays are small. Notice that when partition is called on just one numbers, they end up being sorted.

Can you repeatedly call partition so that the entire array ends up sorted?

Print Sub-Arrays 
In this challenge, print your array every time your partitioning method finishes, i.e. whenever two subarrays, along with the pivot, is merged together.

The first element in a sub-array should be used as a pivot.
Partition the left side before partitioning the right side.
The pivot should be placed between sub-arrays while merging them.
Array of length 1 or less will be considered sorted, and there is no need to sort or to print them.
Note 
Please maintain the original order of the elements in the left and right partitions while partitioning around a pivot element.

For example: Partition about the first element for the array A[]={5, 8, 1, 3, 7, 9, 2} will be {1, 3, 2, 5, 8, 7, 9}

Input Format 
There will be two lines of input:

n - the size of the array
ar - the n numbers of the array
Output Format 
Print every partitioned sub-array on a new line.

----------------------

Notes: Some coders separated partition and quicksort, I guess reusing most
of the partition function from quicksort1. I'm not sure this is helpful
- it doesn't reduced the code length, and the partition is the quick sort.

Created on 26 Jan 2016

@author: chris
'''

def partition(ar):
    p = ar[0]
    arGteP = []
    arLtP = []
    for a in ar[1:]:
        if a > p:
            arGteP.append(a)
        else:
            arLtP.append(a)

    if len(arLtP) > 1:
        arLtP = partition(arLtP)    
    if len(arGteP) > 1:
        arGteP = partition(arGteP)
        
    arOut = arLtP + [p] + arGteP 
    for a in arOut: print a,
    print
    return arOut
    
input()
ar = map(int, raw_input().strip().split())
partition(ar)
