#Given an array, A , of N integers, print A's elements in reverse order as a single line of space-separated numbers.



#!/bin/python

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())
    x=arr[::-1]
final=''
for z in x:
    final=final+str(z)+' '
print(final)
