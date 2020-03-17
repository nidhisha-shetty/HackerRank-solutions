#Given an integer, n, and  space-separated integers as input, create a tuple, , of those  integers.
#Then compute and print the result of .

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print hash((tuple(integer_list)))
