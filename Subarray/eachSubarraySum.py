n=int(input())
arr= list(map(int,input().split()))
for i in range(n):
    subSum=0
    for j in range(i,len(arr)):
        subSum+=arr[j]
        print(subSum)