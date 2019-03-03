#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    freqM = {i:magazine.count(i) for i in set(magazine)}

    for n in note:
        if (n not in freqM) or (freqM[n] <= 0):
            return "No"
        else:
            freqM[n] -= 1

    return "Yes"

if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    print checkMagazine(magazine, note)
