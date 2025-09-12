lst = list(map(int,input().split()))
odd=0
even=0
for ele in lst:
    if(ele%2==0):odd+=1
    else:even+=1
print("Diffrerence between count of odd and even :",(odd-even))