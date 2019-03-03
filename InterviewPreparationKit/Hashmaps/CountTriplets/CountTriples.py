#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    doubles, triples = {}, {}
    num = 0

    for x in arr:
        if x in triples:
            num += triples[x]

        if x in doubles:
            if x*r in triples:
                triples[x*r] += doubles[x]
            else:
                triples[x*r] = doubles[x]

        if x*r in doubles:
            doubles[x*r] += 1
        else:
            doubles[x*r] = 1

    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = raw_input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = map(long, raw_input().rstrip().split())

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
