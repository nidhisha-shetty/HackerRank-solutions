#Average of unique numbers in a list

from __future__ import division

def average(array):
    # your code goes here
    z=(sum(set(array)))/len(set(array))
    return z
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
