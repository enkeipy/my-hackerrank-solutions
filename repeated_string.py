# Challenge at hackerrank.com - http://hr.gs/11o9

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    result = 0
    s_len = len(s)
    positions_of_a = []
    full_string_count = n // s_len    
    for index, letter in enumerate(s):
        if letter == 'a':
            positions_of_a.append(index)
    for index_a in positions_of_a:
        result += full_string_count
        if (n % s_len >= index_a + 1):
            result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
