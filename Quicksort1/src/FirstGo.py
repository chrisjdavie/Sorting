'''
Solving the hackerrank quicksort 1 - partition puzzle.

https://www.hackerrank.com/challenges/quicksort1

----------------------

The previous challenges covered Insertion Sort, which is a simple and intuitive sorting algorithm. Insertion Sort has a running time of O(N2) which isn't fast enough for most purposes. Instead, sorting in the real world is done with faster algorithms like Quicksort, which will be covered in the challenges that follow.

The first step of Quicksort is to partition an array into two smaller arrays.

Challenge 
You're given an array ar and a number p. Partition the array, so that all elements greater than p are to its right, and all elements smaller than p are to its left. p is called the pivot of the partition.

Guideline - In this challenge, you do not need to move around the numbers 'in-place'. This means you can create two lists and combine them at the end.

Input Format 
You will be given an array of integers. The number p is the first element in ar.

There are two lines of input:

n - the number of elements in the array ar
the n elements of ar (including p at the beginning)
Output Format 
Print out the numbers of the partitioned array on one line.

----------------------

Created on 26 Jan 2016

@author: chris
'''

input()
ar = map(int, raw_input().strip().split())
p = ar[0]
arGteP = []
arLtP = []
for a in ar:
    if a >= p:
        arGteP.append(a)
    else:
        arLtP.append(a)

for a in arLtP + arGteP: print a,