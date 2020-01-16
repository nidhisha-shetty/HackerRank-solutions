#You are given the year, and you have to write a function to check if the year is leap or not.

#Constraints: 1900<=y<=10^5

def leap_year(x):
    if x in range(1900, pow(10,5)+1):
        if (x % 4==0 and x % 100!=0):
            print(str(x) + " is a leap year.")
        elif (x % 400==0):
            print(str(x) + " is not a leap year.")
        else:
         print(str(x)+"is not a leap year.")
leap_year(2020)

