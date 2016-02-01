'''
Solving the hackerrank Sherlock and Watson puzzle.

https://www.hackerrank.com/challenges/sherlock-and-watson

---------------------

John Watson performs an operation called Right Circular Rotation on an integer array [a0,a1,...aN-1]. Right Circular Rotation transforms the array from [a0,a1,...aN-1] to [aN-1,a0,...,aN-2].

He performs the operation K times and tests Sherlock's ability to identify the element at a particular position in the array. He asks Q queries. Each query consists of one integer, idx, for which you have to print the element at index idx in the rotated array, i.e. aidx.

Input Format 
The first line consists of three integers, N, K, and Q,, separated by a single space. 
The next line contains N space-separated integers which indicate the elements of the array A. 
Each of the next Q lines contains one integer per line denoting idx.

Output Format 
For each query, print the value at index idx in the updated array separated by newline.

---------------------

Created on 1 Feb 2016

@author: chris
'''

N, K, Q = map(int, raw_input().strip().split())
nums = map(int, raw_input().strip().split())
idx = []
for _ in range(Q):
    idx.append(input())

numsRot = [0]*N

for i, n in enumerate(nums):
    
    numsRot[(i + K)%N] = n

for i in idx:
    print numsRot[i]