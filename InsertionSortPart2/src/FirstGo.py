'''
Solving the hackerrank Insertion Sort Part 2 puzzle.

https://www.hackerrank.com/challenges/insertionsort2

------------------

In Insertion Sort Part 1, you sorted one element into an array. Using the same approach repeatedly, can you sort an entire unsorted array?

Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an element with just the first element - that is already "sorted" since there's nothing to its left that is smaller.

In this challenge, don't print every time you move an element. Instead, print the array after each iteration of the insertion-sort, i.e., whenever the next element is placed at its correct position.

Since the array composed of just the first element is already "sorted", begin printing from the second element and on.

Input Format 
There will be two lines of input:

s - the size of the array
ar - a list of numbers that makes up the array
Output Format 
On each line, output the entire array at every iteration.

-----------------

Created on 24 Jan 2016

@author: chris
'''
#!/bin/python
def eachElement(ar,j):
    e = ar[-j]
    for i in range(j,len(ar)):
        ar[-i] = ar[-i-1]
        if ar[-i] < e:
            ar[-i] = e
            break
    else:
        ar[0] = e
    

def insertionSort(ar):
    for j in range(len(ar)-1,0,-1):
        eachElement(ar,j)
        for a in ar: print a,
        print
        

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)