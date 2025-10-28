arr=list(map(int,input().split()))
b=int(input())
countGood=0
for i in range(len(arr)):
    length=0
    subSum=0
    for j in range(i,len(arr)):
        length+=1
        subSum+=arr[j]
        if((length%2==0 and subSum<b) or (length%2!=0 and subSum>b)): #conditions to be a good subarray
            countGood+=1
print("Number of good subarrays : ",countGood)