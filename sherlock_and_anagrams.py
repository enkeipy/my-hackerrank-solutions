# Challenge at hackerrank.com - http://hr.gs/ec3

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    words = []
    counter = 0
    
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            words.append(sorted(s[i:j+1]))
    
    for i in range(0, len(words) - 1):
        i_word = words[i]
        for j in range(i+1, len(words)):
            if i_word == words[j]:
                counter += 1

    return counter
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
