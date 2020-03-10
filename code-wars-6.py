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