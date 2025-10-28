arr= list(map(int,input().split()))
b=int(input())
count=0
for i in range(len(arr)):
    subSum=0
    for j in range(i,len(arr)):
        subSum+=arr[j]
        if(subSum<b):
            count+=1

print("Number of subarrays in A with a sum less than B :" ,count)

