#In this challenge, the user enters a string and a substring.
#You have to print the number of times that the substring occurs in the given string. 
#String traversal will take place from left to right, not from right to left.

def count_substring(string, substring):
    z=0
    # for n in range (len(string)-len(substring)+1):
    for n in range (len(string)-len(substring)+1):
        
        if string[n:len(substring)+n]==substring:
            #print(string[n:len(substring)+n])
            z=z+1
            
    return z

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count