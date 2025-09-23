n=int(input())
temps=list(map(int,input().split()))
avg= sum(temps)/n
aboveAvg=0
for temp in temps:
    if temp>avg : aboveAvg+=1
print(aboveAvg)