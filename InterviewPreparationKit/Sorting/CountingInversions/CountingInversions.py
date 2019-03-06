#!/bin/python

import math
import os
import random
import re
import sys

def merge(left, right):
    inversions, i, j, result = 0, 0, 0, []
    resultAppend = result.append
    while (i < len(left)) and (j < len(right)):
        if (left[i] <= right[j]):
            resultAppend(left[i])
            i += 1
        else:
            resultAppend(right[j])
            j += 1
            inversions += len(left) - i

    result += left[i:]
    result += right[j:]

    return result, inversions

def mergeSort(arr):
    if len(arr) <= 1: return arr, 0

    mid = len(arr) // 2
    resultLeft, inversionsLeft = mergeSort(arr[:mid])
    resultRight, inversionsRight = mergeSort(arr[mid:])
    if (type(resultLeft) != list): resultLeft = [resultLeft]
    if (type(resultRight) != list): resultRight = [resultRight]

    result, inversions = merge(resultLeft, resultRight)

    return result, inversions + inversionsLeft + inversionsRight

def countInversions(arr):
    return mergeSort(arr)[1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        arr = map(int, raw_input().rstrip().split())

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
