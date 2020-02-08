Given are two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper.
The same student could be in both sets. The task is to find the total number of students who have subscribed to at least one newspaper.

a=raw_input()
for x in a:
    res1=set(raw_input().split())

b=raw_input()
for z in b:
    res2=set(raw_input().split())
print(len(set(res1.union(res2))))
