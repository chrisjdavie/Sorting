'''
2 things I found looking at other people's code - a nicer 
way to swap variables in Python (array operation on one
line, seems to take all the values out and then put them
into the arrays) and I also saw a way of doing it with
queues instead of recursion, which seems a nicer way of 
doing it. Easier to look at and such.

I think queues could be used for sub arrays as well as 
indicies, and I think the memory useage is lower (resolving
as it goes instead of storing all the answers until the end)

Created on 27 Jan 2016

@author: chris
'''
def partition(ar,iStart,iEnd):
    key = ar[iEnd]
    iLtPart = iStart
    for i in range(iStart,iEnd):
        if ar[i] < key:
            ar[iLtPart],ar[i] = ar[i],ar[iLtPart]
            iLtPart += 1
    
    ar[iEnd], ar[iLtPart] = ar[iLtPart], key
    return iLtPart
    
def quicksort(ar):
    
    queue = []
    queue.append((0,len(ar)-1))
    while(len(queue)>0):
        iStart, iEnd = queue.pop()
        iMid = partition(ar, iStart, iEnd)
        if iEnd - (iMid + 1) > 0:
            queue.append((iMid+1, iEnd))
        if (iMid - 1) - iStart > 0:
            queue.append((iStart, iMid-1))
        for a in ar: print a,
        print
    
input()
ar = map(int,raw_input().strip().split())
quicksort(ar)