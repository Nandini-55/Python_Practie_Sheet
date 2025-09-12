lst = list(map(int,input().split()))
odd=[]
even=[]
for ele in lst:
    if(ele%2==0):odd.append(ele)
    else:even.append(ele)
print("Odds  :",odd,"\nEvens :",even)