#count the number of vowels in the string

def getCount(inputStr):
    num_vowels = 0
    li_vowel=['a','e','i','o','u']
    for x in inputStr:
        if x in li_vowel:
            num_vowels+=1
    return num_vowels
res=getCount('abracadabra')
