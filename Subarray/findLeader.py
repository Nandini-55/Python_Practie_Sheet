#write a program to print all the leaders in the array  , an element is a leader if it is greater than all the elements to its right side and the rightmost element is always a leader
# for e.g - [16,17,4,3,5,2] - output - 17,5,2
arr= list(map(int,input().split()))
result=[]
result.append(arr[len(arr)-1])
lastMax=-float("inf")
for i in range(len(arr)-2,-1,-1):
    if(arr[i]>lastMax):
        result.append(arr[i])
        lastMax=arr[i]
print(result)

