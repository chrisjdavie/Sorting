'''
Solving the hackerrank bigger-is-greater challenge

https://www.hackerrank.com/challenges/bigger-is-greater

----------------------

Given a word w, rearrange the letters of w to construct another word s in such a way that s is lexicographically greater than w. In case of multiple possible answers, find the lexicographically smallest one among them.

Input Format

The first line of input contains t, the number of test cases. Each of the next t lines contains w.

Constraints 
1<=t<=105 
1<=|w|<=100 
w will contain only lower-case English letters and its length will not exceed 100.

Output Format

For each testcase, output a string lexicographically bigger than w in a separate line. In case of multiple possible answers, print the lexicographically smallest one, and if no answer exists, print no answer.

----------------------

Created on 27 Jan 2016

@author: chris
'''
def doThis(stringIn):
    
    charsRev = list(stringIn)[::-1]
    for i in range(len(charsRev)-1):
        if charsRev[i] > charsRev[i+1]:
            #charsRev[i], charsRev[i+1] = charsRev[i+1], charsRev[i]
            break
            #return charsRev[::-1]
    else:
        return "no answer"
    i += 1
    
    DiffOrdMin = 1000
    jOrdMin = 0
    
    for j in range(i):
        DiffOrd = ord(charsRev[j])-ord(charsRev[i])
        if DiffOrd > 0 and DiffOrd < DiffOrdMin:
            jOrdMin = j
            DiffOrdMin = DiffOrd
    charsRev[i], charsRev[jOrdMin] = charsRev[jOrdMin], charsRev[i]
    
    charsRev[:i] = sorted(charsRev[:i],reverse=True)
    
    return charsRev[::-1]

def solve(stringIn):
    print "".join(doThis(stringIn))

for _ in range(input()):
    stringIn = raw_input().strip()
    solve(stringIn)