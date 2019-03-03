#!/bin/python

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    arr = {}
    freqs = {}
    output = []

    for op, n in queries:
        if (n in arr) and (arr[n] > 0):
            freqs[arr[n]] = freqs[arr[n]] - 1 if ((arr[n] in freqs) and freqs[arr[n]]) else 0
            if op == 1: arr[n] += 1
            if op == 2: arr[n] -= 1
            freqs[arr[n]] = freqs[arr[n]] + 1 if (arr[n] in freqs) else 1
        else:
            if op == 1:
                arr[n] = 1
                freqs[arr[n]] = freqs[arr[n]] + 1 if (arr[n] in freqs) else 1

        if op == 3: output.append(1 if ((n in freqs) and freqs[n]) else 0)

    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    queries = []

    for _ in xrange(q):
        queries.append(map(int, raw_input().rstrip().split()))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
