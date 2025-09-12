lst = list(map(int,input().split()))
min=float("inf")
max=-float("inf")
for ele in lst:
    min = min if min<ele else ele
    max = max if max>ele else ele
print("Max : ",max,"\nMin :",min)

