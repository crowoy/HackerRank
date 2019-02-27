#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    lastIndex = len(q) - 1
    swaps = 0
    swaped = False

    # Check if too chaotic
    for i, v in enumerate(q):
        if (v - 1) - i > 2:
            return "Too chaotic"

    # Bubble Sort
    for i in range(0, lastIndex):
        for j in range(0, lastIndex):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                swaps += 1
                swaped = True

        if swaped:
            swaped = False
        else:
            break

    return swaps

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in range(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        print minimumBribes(q)
