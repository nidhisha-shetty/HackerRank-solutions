#Add and remove elements of a set using commands such as pop, remove and discard.

s = set(input().split())
print(s)
s.add(input("Enter a number to add in the list"))
print(s)
s.remove(input("Enter a number to remove from the list and if the number doesnot exist in list an error will be thrown"))
print(s)
s.discard(input("Enter a number to remove from the list") ) #if number doesnot exist, no error will be thrown
print(s)
s.pop() #returns a random set of numbers
print(s)
