#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaximumMex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER x
#

def getMaximumMex(arr, x):
    return "test"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    x = int(input().strip())

    result = getMaximumMex(arr, x)

    fptr.write(str(result) + '\n')

    fptr.close()