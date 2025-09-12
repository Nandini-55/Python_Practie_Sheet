lst = list(map(int,input().split()))
search=int(input())
for i in range(len(lst)) :
    if lst[i]==search:
        print("Index of",search,"is",i)
        break
