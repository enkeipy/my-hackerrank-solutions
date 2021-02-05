# Challenge at hackerrank.com - http://hr.gs/3rtx

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    path = [x for x in path]
    sea_level = 0
    valleys = 0
    x = range(steps)
    for i in x:
        sea_level = make_step(i, path, sea_level)
        if sea_level == 0:
            if path[i] == 'U':
                valleys += 1
    return valleys

def make_step(i, path, sea_level):
    if path[i] == 'U':
        sea_level = sea_level + 1
    else:
        sea_level = sea_level - 1
    return sea_level
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
