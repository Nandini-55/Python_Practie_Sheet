#Given 'n' and 'i' (i is th bit) check if ith bit position is set(1) or not
#34- 100010
# 13=1011
#21 = 10101

#Dry run - 
# n=13 - 1011
#i=2
#n>>2 - 10 
#10 & 1 = 0- unset

n=int(input()) 
i=int(input())
bitMask=n>>i
if(1 & bitMask==1):
    print("set")
else:
    print("unset")

