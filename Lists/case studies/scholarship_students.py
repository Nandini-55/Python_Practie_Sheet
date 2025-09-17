n = int(input())
eligibleCount=0
for i in range(n):
    data=list(map(int,input().split()))
    if(data[0]>=75 and data[1]>=80):
        eligibleCount+=1
print(eligibleCount)