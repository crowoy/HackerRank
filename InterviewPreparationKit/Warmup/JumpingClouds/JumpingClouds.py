#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    clouds = [int(i) for i in c]
    path = [0]

    i = 0
    while i <= len(clouds)-1:
        if ((i+2) <= len(clouds)-1) and (not clouds[i+2]):
            path.append(i+2)
            i += 2
        elif ((i+1) <= len(clouds)-1) and (not clouds[i+1]):
            path.append(i+1)
            i += 1
        else:
            break

    jumps = len(path) - 1

    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
