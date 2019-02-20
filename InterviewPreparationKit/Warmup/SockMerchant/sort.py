#!/bin/python

import math
import os
import random
import re
import sys

def sort(arr):
    for i in range(len(arr)-1):
        next = arr[i+1]

        while (arr[i] > next) and (i < len(arr)):


if __name__ == '__main__':

    arr = [1,2,4,1,2,4,51,2,53,6]

    print(sort(arr))
