n=int(input())
ids=list(map(int,input().split()))
reverseIds=[]

for i in range(n):
   
    if(ids[i]%5==0):
        reverseIds.append(ids[i])
reverseIds.reverse()
if(len(reverseIds)==0):
    print(-1)
else:
    print(*reverseIds)