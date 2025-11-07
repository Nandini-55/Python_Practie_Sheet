def pow(n,p):
    if(p==0):
        return 1
    elif(p==1):
        return n
    return n*pow(n,p-1)
def exp(num,pow):
    if(pow==0):
        return 1
    half = exp(num,pow//2)
    if(pow%2==0):
        return half*half
    else:
        return half*half*num
arr=list(map(int,input().split()))
print(exp(arr[0],arr[1]))