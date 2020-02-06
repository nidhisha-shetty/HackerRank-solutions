# Read a given string, change the character at a given index and then print the modified string.

#method 1
def mutate_string(string, position, character):
    string=list(string)
    z = string[:position]+character+s[i:]
    return z

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
   
#method 2
n=input("Enter input")
i=int(input("Enter a number"))
c=input("Enter the character")
def mutate(n,i,c):
    x=n[:i]+c[:]+n[i+1:]
    return x
z=mutate(n,i,c)
print(z)
