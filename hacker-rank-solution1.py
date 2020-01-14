# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird



number=int(input("Please enter a number"))
if(number >=1 and number <=100):
    if((number%2!=0) or (number%2==0 and number in range(6, 21))):
        print("Weird")
    elif((number%2==0 and number in range(2, 5)) or (number%2==0 and number>20) ):
     print("Not Weird")