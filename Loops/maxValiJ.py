#Given an array of integers of size n . find maximum value of j-i such that A[i]<=A[j]
# e.g-arr=[3,5,4,2]  output =2

arr=[3,5,4,2]
max=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if((arr[i]<=arr[j]) and (j-i)>max):
            max=j-i
            # print(arr[i],i,arr[j],j)

print(max)
