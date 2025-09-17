n=int(input())
deadlines=list(map(int,input().split()))
target=int(input())
pairCount=0

for i in range(n):
    for j in range((i+1),n):
        if(deadlines[i]+deadlines[j]==target):
            pairCount+=1

print(pairCount)

# deadlines.sort()
# print(*deadlines)
# low=0
# high=len(deadlines)-1
# while(high>low):
#     h=deadlines[high]
#     print(h)
#     l=deadlines[low]
#     print(l)
#     if((h+l)==target):
#         pairCount+=1
#         low+=1
#         high-=1
#     elif((h+l)>target):
#         high-=1
#     else:
#         low+=1
# print(pairCount)