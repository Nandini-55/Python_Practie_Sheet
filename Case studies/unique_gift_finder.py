n= int(input())
codes = list(map(int,input().split()))
#time complexitiy- O(n^2)
for i in range(n):
    val=codes[i]
    count=0
    for j in range(n):
        if(codes[j]==val):
            count+=1
    if(count==1):
        print(val,end=" ")

#only applicable to given example 

#time complexity - O(n+1)

# counts=[]
# for i in range(n+1):
#     counts.append(0)
# for code in codes:
#     counts[code//10]+=1
# for i in range(n+1):
#     if(counts[i]==1):
#         print((i*10),end=" ")