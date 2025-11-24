def countSteps(a,b,c,n):
    if(n==1):
        print("Disk",n," from",a,"to",c)
        return 1
    step = countSteps(a,c,b,n-1)
    print("Disk",n," from",a,"to",c)  
    step2=countSteps(b,a,c,n-1)
    

    return step+1+step2

# to count step an easier formula can also be used -> 2^n-1  (n=no. of disks)
print(countSteps("A","B","C",4))