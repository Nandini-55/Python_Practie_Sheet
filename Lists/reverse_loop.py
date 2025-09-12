lst = list(map(int,input().split()))
for i in range(len(lst)//2):
    lst[i],lst[len(lst)-i-1]=lst[len(lst)-i-1],lst[i]
print(lst)