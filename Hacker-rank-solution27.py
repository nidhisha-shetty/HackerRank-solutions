num=input("Enter the number of students")
for i in num:
  name=input("Enter name of the student")
  marks=input("Enter the corresponding marks of student")
  marksheet=[]
  marksheet=marksheet+[[name, marks]]
  scorlist=[]
  scorelist=scorelist.append(marks)
  score=sorted(scorelist[1])
for name,marks in marksheet:
  if score==marks:
    print(name)
