#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    alt = 0
    valleys = 0
    inValley = False

    for step in s:
        if (alt == 0) & (step == "D"):
            inValley = not inValley

        if (alt == -1) & (step == "U"):
            inValley = not inValley
            valleys += 1

        if step == "U":
            alt += 1
        else:
            alt -= 1

    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
