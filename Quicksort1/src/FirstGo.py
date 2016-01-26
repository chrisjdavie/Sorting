'''
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