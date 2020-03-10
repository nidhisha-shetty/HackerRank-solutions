# Complete the method which accepts an array of integers, and returns one of the following:

# "yes, ascending" - if the numbers in the array are sorted in an ascending order
# "yes, descending" - if the numbers in the array are sorted in a descending order
# "no" - otherwise


def is_sorted_and_how(arr):
    desc=sorted(arr, reverse=True)
    asc=sorted(arr)
    if arr==desc:
        print("'yes, descending'")
    elif arr==asc:
        print("'yes, ascending'")
    else:
        print("'no'")
    
    
arr=list(input("Enter a list of numbers").split(" "))
is_sorted_and_how(arr)
