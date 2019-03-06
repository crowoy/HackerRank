#!/bin/python

import math
import os
import random
import re
import sys
import bisect

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    num = 0
    arr = sorted(expenditure[:d])

    for i in range(d,len(expenditure)):
        median = (arr[d / 2 - 1] + arr[d / 2]) / 2.0 if (not d%2) else arr[int(d / 2)]

        if expenditure[i] >= median*2: num += 1

        arr.pop(bisect.bisect_left(arr, expenditure[i-d]))
        bisect.insort_right(arr, expenditure[i])

    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = map(int, raw_input().rstrip().split())

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
