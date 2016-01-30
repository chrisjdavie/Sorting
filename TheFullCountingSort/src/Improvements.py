'''
Solving the hackerrank The Full Counting Sort puzzle.

https://www.hackerrank.com/challenges/countingsort4

----------------------

In this challenge you need to print the data that accompanies each integer in a list. In addition, if two strings have the same integers, you need to print the strings in their original order. Hence, your sorting algorithm should be stable, i.e. the original order should be maintained for equal elements.

Insertion Sort and the simple version of Quicksort were stable, but the faster in-place version of Quicksort was not (since it scrambled around elements while sorting).

In cases where you care about the original order, it is important to use a stable sorting algorithm. In this challenge, you will use counting sort to sort a list while keeping the order of the strings (with the accompanying integer) preserved.

Challenge 
In the previous challenge, you created a "helper array" that contains information about the starting position of each element in a sorted array. Can you use this array to help you create a sorted array of the original list?

Hint: You can go through the original array to access the strings. You can then use your helper array to help determine where to place those strings in the sorted array. Be careful about being one off.

Details and a Twist 
You will be given a list that contains both integers and strings. Can you print the strings in order of their accompanying integers? If the integers for two strings are equal, ensure that they are print in the order they appeared in the original list.

The Twist - Your clients just called with an update. They don't want you to print the first half of the original array. Instead, they want you to print a dash for any element from the first half. So you can modify your counting sort algorithm to sort the second half of the array only.

Input Format 
- n, the size of the list ar. 
- n lines follow, each containing an integer x and a string s.

Output Format 
Print the strings in their correct order.

----------------------

Created on 30 Jan 2016

@author: chris
'''
from collections import deque

arText = {}
lim = 100
ar = [0]*100
N = input()
for i in range(N):
    num, text = raw_input().strip().split()
    num = int(num)
    ar[num] += 1
    if i < N/2:
        text = '-'
    try:
        arText[num].append(text)
    except KeyError:
        arText[num] = deque([text])

opAr = [ arText[num].popleft() for num, count in enumerate(ar) for _ in range(count) ]

print " ".join(opAr)
        