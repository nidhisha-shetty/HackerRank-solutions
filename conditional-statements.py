# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 4, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird



number=int(input("Please enter a number"))
if(number >=1 and number <=100):
    if((number%2!=0) or (number%2==0 and number in range(6, 21))):
        print("Weird")
    elif((number%2==0 and number in range(2, 5)) or (number%2==0 and number>20) ):
        print("Not Weird")
