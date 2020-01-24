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
