#Check if a given sentence is a pangram or not

import string

def is_pangram(s):
    
    res=s.casefold()
    res=res.replace(" ", "")
    z=set(res)
    
    if len(set('abcdefghijklmnopqrstuvwxyz')-set(res))==0:
        print(len(set('abcdefghijklmnopqrstuvwxyz')-set(res)))
        return True
    else:
        print(len(set('abcdefghijklmnopqrstuvwxyz')-set(s)))
        return False
    

s="Cwm fjord bank glyphs vext quiz"
is_pangram(s)
