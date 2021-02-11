# Challenge at hackerrank.com - http://hr.gs/fccdad

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):          
    bribes = 0
    LEN_Q = len(q)
    for i in range(LEN_Q):
        m = q[i]
        if m-i > 3:
            print('Too chaotic')
            return
        for x in range(max(m-2,0),i):
            if q[x] > m:
                bribes += 1
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
