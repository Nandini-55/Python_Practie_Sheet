n=int(input())
deadlines=list(map(int,input().split()))
target=int(input())
pairCount=0

for i in range(n):
    for j in range((i+1),n):
        if(deadlines[i]+deadlines[j]==target):
            pairCount+=1

print(pairCount)
