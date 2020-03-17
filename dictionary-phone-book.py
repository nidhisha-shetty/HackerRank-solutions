#Given 'n' names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
#You will then be given an unknown number of names to query your phone book for. For each 'name' queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
#if an entry for 'name' is not found, print 'Not found' instead.


no_of_entries=int(input("Enter a number "))
name_number=[input("Enter a name and their corresponding contact number").split() for _ in range(no_of_entries)]
phone_book={k:v for k,v in name_number}
check_name=input("Enter a name ")
if check_name in phone_book:
    print(phone_book[check_name])
else:
    print("Not found")
