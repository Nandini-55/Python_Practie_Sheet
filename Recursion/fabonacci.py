#Write a recursive function to find the nth fabonacci no.

def fabonacci(a,b,n):
    if(n==0):
        print(a)
        return
    fabonacci(b,a+b,n-1)

n=int(input())
# fabonacci(0,1,n)

def fab(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return fab(n-1)+fab(n-2)
    

print(fab(n))

