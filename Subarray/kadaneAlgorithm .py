#Given an integer array nums, find the subarray with the largest sum, and return its sum.
n=int(input())
max=-float("inf")
arr= list(map(int,input().split()))
for i in range(n):
    subSum=0
    for j in range(i,len(arr)):
        subSum+=arr[j]
        max = subSum if subSum>max else max
    
print(max)