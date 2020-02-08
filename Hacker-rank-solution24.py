#Calculate factorial of a number

a=int(input("Enter a number"))
fact=1
for x in range(1, a+1):
    fact=fact*x
print(fact)


