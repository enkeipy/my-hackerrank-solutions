# Challenge at hackerrank.com - http://hr.gs/eabbdd

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    result = 0
    counted = {}
    for i in ar:
        counted[i] = counted.get(i,0) + 1
    for x,y in counted.items():
        result += y//2
    return result
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
