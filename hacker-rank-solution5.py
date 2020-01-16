#Read an integer 'N' 
#Without using any string methods, try to print the following:
#123..N

from __future__ import print_function
i=int(input())
print(*range(1,i+1), sep='')
    	
