#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    letter = "a"

    arr = [i for i in s]
    count = arr.count(letter)

    if n < len(arr):
        return arr[:n].count(letter)
    else:
        fullSeq = count * int(n / len(arr))
        remainderSeq = arr[:int(n % len(arr))].count(letter)
        return fullSeq + remainderSeq

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
