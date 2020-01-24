#Guess the number game, wherein a number is stored in a variable beforehand, and the user is asked to enter a number, untill and unless the user enters the correct number, the program keeps executing. 

i=32
j=0
while j!=i:
    j=int(input("Enter a number: "))
    if(j<i):
        print("You entered a smaller value")
    elif(j>i):
        print("You entered a greater value")
    else:
        print("You entered the correct value!")
        break
