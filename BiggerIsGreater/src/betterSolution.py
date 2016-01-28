'''
Using http://www.nayuki.io/page/next-lexicographical-permutation-algorithm

I missed the "reverse the suffix" at the end, but otherwise was fine.

Is interesting to read someone write this stuff with words. Half the battle
I'd guess.

Created on 27 Jan 2016

@author: chris
'''
def doThis(stringIn):
    
    # find longest non-increasing suffix
    
    charsRev = list(stringIn)[::-1]
    for i in range(len(charsRev)-1):
        if charsRev[i] > charsRev[i+1]:
            break
    else:
        return "no answer"
    
    # identify pivot
    i += 1
    
    # find rightmost successor to pivot in the suffix
    DiffOrdMin = 1000
    jOrdMin = 0
    
    for j in range(i):
        DiffOrd = ord(charsRev[j])-ord(charsRev[i])
        if DiffOrd > 0 and DiffOrd < DiffOrdMin:
            jOrdMin = j
            DiffOrdMin = DiffOrd
            
    # swap with pivot
    charsRev[i], charsRev[jOrdMin] = charsRev[jOrdMin], charsRev[i]
    
    # reverse the suffix (I missed this, didn't suffix was already
    # sorted)
    charsRev[:i] = reversed(charsRev[:i])
    
    return charsRev[::-1]

def solve(stringIn):
    print "".join(doThis(stringIn))

for _ in range(input()):
    stringIn = raw_input().strip()
    solve(stringIn)