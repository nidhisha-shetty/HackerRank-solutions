#List filtering
def filter_list(l):
  'return a new list with the strings filtered out'
  fin=[]
  for x in l:
      if isinstance(x, int):
        # print(type(x))
        # print(type(fin))
        fin.append(x)
        # print("yes")
  return fin    
  

a=[1,2,3,'abc','def']
res=filter_list(a)
print(res)