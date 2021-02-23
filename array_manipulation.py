# Challenge at hackerrank.com - http://hr.gs/deabde

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    current_max = 0
    max_sum = 0
    arr = [0]*n
    for q in queries:
        value = q[2]
        index0 = q[0] - 1
        index1 = q[1] - 1
        arr[index0] += value
        if index1 < n - 1:
            arr[index1 + 1] -= value
    print(arr)
    for i, n in enumerate(arr):
        current_max += n
        if current_max > max_sum:
            max_sum = current_max
    return max_sum
        
            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
