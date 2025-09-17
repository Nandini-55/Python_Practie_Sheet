n=int(input())
ids=list(map(int,input().split()))
evenIds=[]
for id in ids:
    if(id%2==0):
        evenIds.append(id)
if(len(evenIds)==0):
    print(-1)
else:
    print(*evenIds)