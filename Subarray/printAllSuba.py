n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    subarr=[]
    for j in range(i,len(arr)):
        subarr.append(arr[j])
        print(subarr)