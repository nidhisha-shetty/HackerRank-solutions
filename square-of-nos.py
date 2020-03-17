#Read an integer n. For all non-negative integers n, print n*n. 
#Constraints
#1<=N<=20



if __name__ == '__main__':
    n = int(raw_input())
    if(n>=1 and n<=20):
        i=0
        while(i<n):
            ans=i*i
            print(ans)
            i=i+1
