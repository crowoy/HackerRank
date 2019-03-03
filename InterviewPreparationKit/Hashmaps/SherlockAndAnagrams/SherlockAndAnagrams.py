#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    subStr = list(s[i:j+1] for i in range(len(s)) for j in range(i, len(s)))

    freqS = {}
    for sub in subStr:
        sortedSub = ''.join(sorted(sub))
        if sortedSub in freqS:
            freqS[sortedSub] += 1
        else:
            freqS[sortedSub] = 1

    num = 0
    for v in freqS.values():
        num += (v*(v-1))/2

    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
