# Challenge at hackerrank.com - http://hr.gs/3apgt

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    arr_dict = {n: i for i, n in enumerate(arr)}
    for i, n in enumerate(arr):
        if n != i+1:
            index = arr_dict[i+1]
            arr[i], arr[index] = arr[index], arr[i]
            arr_dict[n] = index
            arr_dict[i+1] = i
            swaps += 1
    return swaps
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
