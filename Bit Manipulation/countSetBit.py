
#Given an integer 'n' count how many set bit are their in 'n'
#27 -11011
# 13 #1011
n=int(input())
count=0
while(n!=0):
    if(n & 1==1):
        count+=1
    n = n>>1

print(count)