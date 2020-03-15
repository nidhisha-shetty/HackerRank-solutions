#Wrap the string into a paragraph of width 'W' .

def ele(char, max_width):
    for i in range(0,len(char),2):
        res="".join(char[i:i+max_width])
    return res
   
char=input("Enter a series of character")
max_width=int(input("Enter a number"))
a=ele(char, max_width)
print(a)


###Second method (hackerrank specific)###
def wrap(string, max_width):
    	final=''
    	for i in range(0, len(string), max_width):
        	res=''.join(string[i:i+max_width])
        	final+=res+'\n'
    	return final
if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
