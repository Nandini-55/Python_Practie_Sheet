str=input()
count=0
for i in range(len(str)-2):
    if(str[i]=="b" and str[i+1]=="o" and str[i+2]=="b"):
        count+=1
        
print(count)


