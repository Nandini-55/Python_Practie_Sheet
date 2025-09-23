n=int(input())
price=list(map(int,input().split()))
countIncr=0
for i in range(1,n):
    if(price[i]>price[i-1]):
        countIncr+=1
print(countIncr)