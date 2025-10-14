str=input()
check=input()
result=""
idx=0
count=0
for i in range(len(str)):
    if( idx<len(check) and str[i]==check[idx]):
        result+=str[i]
        idx+=1
        if(result==check):
            count+=1
            idx=0
            result=""
    else:
        idx=0
        result=""
print(count)


