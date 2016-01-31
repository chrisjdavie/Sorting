'''
Solving the hackerrank Closest Numbers puzzle.

https://www.hackerrank.com/challenges/closest-numbers

----------------------

Sorting is often useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses, as well.

Challenge 
Given a list of unsorted integers, A={a1,a2,…,aN}, can you find the pair of elements that have the smallest absolute difference between them? If there are multiple pairs, find them all.

Input Format 
The first line of input contains a single integer, N, representing the length of array A. 
In the second line, there are N space-separated integers, a1,a2,…,aN, representing the elements of array A.

Output Format 
Output the pairs of elements with the smallest difference. If there are multiple pairs, output all of them in ascending order, all on the same line (consecutively) with just a single space between each pair of numbers. If there's a number which lies in two pair, print it two times (see the sample case #3 for explanation).

----------------------

Created on 31 Jan 2016

@author: chris
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
numsIn = map(int, raw_input().strip().split())
numsIn.sort()

minDiff = 10**7 + 1
pairs = []
for n1, n0 in zip(numsIn[1:], numsIn[:-1]):
    diffN = abs(n1 - n0)
    if diffN == minDiff:
        pairs += [n0, n1]
    elif diffN < minDiff:
        minDiff = diffN
        pairs = [n0, n1]

print " ".join(map(str,pairs))
