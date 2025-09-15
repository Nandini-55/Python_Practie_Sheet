lst = list(map(int,input().split()))
search=int(input())
for i in range(len(lst)) :
    if lst[i]==search:
        print(1)
        break
    if(i==len(lst)-1):
        print(0)
