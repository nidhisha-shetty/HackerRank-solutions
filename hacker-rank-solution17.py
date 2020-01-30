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



#Second method
li=list(input("Enter a list").split(" "))
rev_li=li[::-1]
final_li=""
for x in rev_li:
    final_li=final_li+x+" "
print(final_li)
