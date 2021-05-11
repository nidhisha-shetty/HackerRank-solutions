'''
Problem Statement: There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.
Return an array of the results.
'''

# Solution:
import math
import os
import random
import re
import sys

def matchingStrings(strings, queries):
    res=[]
    for x in range(len(queries)):
        count=0
        for y in range(len(strings)):
            if queries[x]==strings[y]:
                count+=1
        res.append(count)
    return res            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(raw_input().strip())

    strings = []

    for _ in xrange(strings_count):
        strings_item = raw_input()
        strings.append(strings_item)

    queries_count = int(raw_input().strip())

    queries = []

    for _ in xrange(queries_count):
        queries_item = raw_input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()


#Time complexity: O(n^2) 
#Space Complexity: O(1)
