lst = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
result=[]
if(len(lst)==len(lst2)):
    for i in range(len(lst)):
        result.append(lst[i]+lst2[i])
    print(result)
else:
    print("Arrays must be of equal size.")
