#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0

    for i in range(0, len(arr) - 1):
        while arr[i] != i + 1:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            swaps += 1

    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
