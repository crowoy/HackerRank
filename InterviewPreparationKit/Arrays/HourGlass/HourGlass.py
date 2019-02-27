#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    rows = len(arr)
    cols = len(arr[0])

    allHgs = []

    for j in range(1, cols-1):
        for i in range(1, rows-1):
            currHg = arr[i][j]

            for k in [-1,1]:
                for l in [-1,0,1]:
                    currHg += arr[i+k][j+l]

            allHgs.append(currHg)

    return max(allHgs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
