def add_binary(a,b):
    #your code here
    res=a+b
    new_bin='{0:b}'.format(res)
    return new_bin

a=2
b=3
res=add_binary(a,b)
print(res)
