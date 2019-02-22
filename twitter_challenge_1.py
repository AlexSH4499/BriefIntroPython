#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'closest' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def helper_fn(s):
    result = []
    #lets construct a dic with key as given character value a tuple with [0] as indexes, [1] as freq
    di = {}
    for i, s in enumerate(s):
        if s not in di:
            di[s] = [[i], 1] #why am i even bothering with a tuple, derp just use a list of lists
        elif s in di:
            temp_li = di[s] #tuple unpacking
            temp_li[0].append(i) #append new index
            temp_li[1] += 1
            di.update(s,) #update the entry with new tuple
    return result

def closest(s, queries):
    # Write your code here
    return


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = closest(s, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
