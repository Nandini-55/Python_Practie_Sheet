str=input()
check=input()
result=""
idx=0
for i in range(len(str)):
    if( idx<len(check) and str[i]==check[idx]):
        result+=str[i]
        if(result==check):
            print(i-len(check)+1)
            break
        idx+=1
    else:
        idx=0
        result=""
    if(i==len(str)-1):
        print("Not present")

