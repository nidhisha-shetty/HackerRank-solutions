# Read two integers from STDIN and print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

a=(input(""))
b=(input(""))
print('{0}\n{1}\n{2}'.format((a + b), (a - b), (a * b)))
