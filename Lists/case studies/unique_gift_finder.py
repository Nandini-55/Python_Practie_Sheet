n= int(input())
codes = list(map(int,input().split()))
counts=[]
for i in range(n+1):
    counts.append(0)
for code in codes:
    counts[code//10]+=1
for i in range(n+1):
    if(counts[i]==1):
        print((i*10),end=" ")

