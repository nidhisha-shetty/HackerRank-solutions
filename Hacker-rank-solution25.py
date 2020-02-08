#Wrap the string into a paragraph of width 'W' .

def ele(char, max_width):
    for i in range(0,len(char),2):
        res="".join(char[i:i+max_width])
        print(res)
   
char=input("Enter a series of character")
max_width=int(input("Enter a number"))
a=ele(char, max_width)
