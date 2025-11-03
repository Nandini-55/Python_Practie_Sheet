lst= list(map(int,input().split()))
num=int(input())
result=[]
for ele in lst:
    result.append(ele+num)
print(result)