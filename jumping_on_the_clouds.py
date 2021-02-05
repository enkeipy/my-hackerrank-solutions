# Challenge at hackerrank.com - http://hr.gs/efaabf

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    result = 0
    while i < len(c) - 1:
        if i+2 > len(c) - 1 or c[i+2] == 1:
            i += 1            
        else:
            i += 2
        result += 1
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
