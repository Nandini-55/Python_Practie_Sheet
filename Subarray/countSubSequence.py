 #give a string s you have to count no. of "AG" pairs in a string - a string contains only capital letters - e.g - s="ABCGAG" - ans - 3 ->find subsequence
    
s=input()
count=0
gCount=0
for i in range(len(s)-1,-1,-1):
    if(s[i]=="G"):
        gCount+=1
    elif(s[i]=="A"):
        count+=gCount

print(count)
