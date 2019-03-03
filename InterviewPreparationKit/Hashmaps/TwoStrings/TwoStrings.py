#!/bin/python

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    return 'YES' if (set(s1) & set(s2)) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s1 = raw_input()

        s2 = raw_input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
