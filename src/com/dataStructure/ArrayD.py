#!/bin/python3

import math
import os
import random
import re
import sys

# HackersRank Algorithm Question - Arrays - DS Solution

#Category: Data Structure
#Solved Date: 2019 - 08 - 08
#Author: TK Lee
#Source: https: //www.hackerrank.com/challenges/arrays-ds/problem

# Complete the reverseArray function below.
def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

