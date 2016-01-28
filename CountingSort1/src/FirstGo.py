'''
Solving the hackerrank Counting Sort 1 puzzle.

https://www.hackerrank.com/challenges/countingsort1

----------------------

Comparison Sorting 
Quicksort usually has a running time of n×log(n), but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat n×log(n) (worst-case) running time, since n×log(n) represents the minimum number of comparisons needed to know where to place each element. For more details, you can see these notes (PDF).

Alternative Sorting 
However, for certain types of input, it is more efficient to use a non-comparison sorting algorithm. This will make it possible to sort lists even in linear time. These challenges will cover Counting Sort, a fast way to sort lists where the elements have a small number of possible values, such as integers within a certain range. We will start with an easy task - counting.

Challenge 
Given a list of integers, can you count and output the number of times each value appears?

Hint: There is no need to sort the data, you just need to count it.

Input Format 
There will be two lines of input:

n - the size of the list
ar - n space-separated numbers that make up the list
Output Format 
Output the number of times every number from 0 to 99 (inclusive) appears on the list.

----------------------

Created on 28 Jan 2016

@author: chris
'''

input()
ar = map(int,raw_input().strip().split())
counts = [0]*100

for a in ar: counts[a] += 1
for count in counts: print count,