a=int(input("Enter a number"))
name_number=[input("Enter a name and number").split() for _ in range(a)]
phone_book={k:v for k,v in name_number}
user_input=input("Enter a name")
if user_input in phone_book:
	print(phone_book[user_input])
else:
	print("Not found")