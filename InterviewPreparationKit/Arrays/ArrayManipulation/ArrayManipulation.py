#!/bin/python

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n+1)

    for a, b, k in queries:
        arr[a-1] += k
        arr[b] -= k

    maxVal, tmp = 0, 0
    for a in arr:
        tmp += a
        if tmp > maxVal: maxVal = tmp

    return maxVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
