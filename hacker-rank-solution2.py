

a=int(input("Enter a number"))
b=int(input("Enter a number"))
if(a>=1 and a<=10000000000) and (b>=1 and b<=10000000000):
	print(a+b)
	print(a-b)
	print(a*b)



######################solution 3#########################
# Read two integers from STDIN and print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

a=(input(""))
b=(input(""))
print('{0}\n{1}\n{2}'.format((a + b), (a - b), (a * b)))