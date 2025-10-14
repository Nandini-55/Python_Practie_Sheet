str=input()
lst=str.split()
result=""
for i in range(len(lst)-1,-1,-1):
    result+=lst[i]+" "

print(result)