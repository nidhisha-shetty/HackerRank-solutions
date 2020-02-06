#Swap the casing of each letter in the word (example: Hello World --> hELLO wORLD)

def swap_case(s):
    a=''
    for x in s:
        a+=x.swapcase()
    return a

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
