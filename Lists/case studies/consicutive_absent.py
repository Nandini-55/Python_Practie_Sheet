n=int(input())
attendence=list(map(int,input().split()))
highest0=0
cons0=0
for i in range(n):
    if(attendence[i]==0):
        cons0+=1
        if(cons0>highest0):
            highest0=cons0
    else:
        cons0=0
print(highest0)

