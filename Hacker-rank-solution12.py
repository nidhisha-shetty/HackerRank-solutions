#The first line contains an integer N, the total number of country stamps.
#The next N lines contains the name of the country where the stamp is from.
#Find the total number of distinct country stamps.


i=input()
li=[]
for x in range(i):
    n=raw_input()
    li.append(n)
li_1=[]
for x in li:
    if x not in li_1:
        li_1.append(x)
print(len(li_1))
