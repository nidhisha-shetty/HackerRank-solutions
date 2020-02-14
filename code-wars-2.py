#sum of 2 smallest nos in the list

def sum_two_smallest_numbers(numbers):
    li=[]
    for x in numbers.split():
        li.append(x)
    li.sort()
    
    res=int(li[0]) + int(li[1])
    return res
numbers=input("Enter a list of numbers")
final=sum_two_smallest_numbers(numbers)
print(final)
