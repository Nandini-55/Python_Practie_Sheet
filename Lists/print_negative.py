lst = list(map(int,input().split()))
result=[]
for ele in lst:
    if(ele<0): result.append(ele)
print(result)