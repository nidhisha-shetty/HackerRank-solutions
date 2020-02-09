#Print the name(s) of any student(s) having the second lowest grade; if there are multiple students, order their names alphabetically and print each one on a new line.

num=int(input("Enter the number of students"))
marksheet=[]
scorelist=[]
for i in range(num):
  name=input("Enter name of the student")
  marks=input("Enter the corresponding marks of student")
  marksheet=marksheet+[[name, marks]]
  scorelist=scorelist+[marks]
print(scorelist)
print(type(scorelist))
score=sorted(scorelist)[1]
for name,marks in marksheet:
  if score==marks:
    print(name)
