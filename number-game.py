actual_number=34
number=0
while input!=34:
    number=int(input("Enter a number"))
    if(number<actual_number):
        print("Your guess is less than the answer")
    elif(number>actual_number):
        print("Your guess is greater than the answer")
    else:
        print("Your guess is correct")
        break