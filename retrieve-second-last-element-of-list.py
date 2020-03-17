#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up. (find the runner-up score)

#method 1
s=(set(list(input().split())))      #for input such as '2 3 6 6 5'
print(s)
s_max=max(s)
li=[]
for x in s:
    if x<s_max:
        li.append(x)
print(li)
print(max(li))



#method 2
s=(set(list(input().split())))        #for input such as '2 3 6 6 5'
s.remove(max(s))
print(max(s))
