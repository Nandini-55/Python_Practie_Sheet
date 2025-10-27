arr= list(map(int,input().split()))
sum=0
for i in range(len(arr)):
    subSum=0
    for j in range(i,len(arr)):
        subSum+=arr[j]
        sum+=subSum


#           OR
#Contribution technique - find no. of contribution of each element and then multiply with no. of contribution
sum=0
for i in range(len(arr)):
    count = (i+1)*(len(arr)-i) #contribution of element
    sum=count*arr[i]

print("Sum of all subarrays sum : ",sum)