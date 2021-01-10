**Problem statement**:
There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6X6.

**hourglass**:
a b c
  d
e f g

**6X6 2D Array, arr**:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

**Solution**:
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum=[]
    for x in range(len(arr)-2):
        for y in range(len(arr)-2):
            sum.append(arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x+1][y+1]+arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2])
    return max(sum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
