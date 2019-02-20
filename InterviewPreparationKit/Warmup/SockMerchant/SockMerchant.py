#!/bin/python

import math
import os
import random
import re
import sys

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        nxt_element = arr[i]

        while (arr[j] > nxt_element) and (j >= 0):
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = nxt_element
    return arr

# Complete the sockMerchant function below.
def sockMerchant(n, arr):
    arr = insertion_sort(arr)
    sockPairs = 0

    i = 0
    while i < len(arr)-1:
        print i
        if (arr[i] == arr[i+1]) & (i < len(arr)):
            sockPairs += 1
            i += 1
        i += 1

    return sockPairs

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
