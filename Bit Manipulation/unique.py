#Given N array element , every element repeats twice except 1. find the unique element.
arr=list(map(int,input().split()))

#Time complexity - O(n^2)
for i in range(len(arr)):
    ele=arr[i]
    check = True
    for j in range(len(arr)):
        if(ele ^ arr[j]==0 and i!=j):
            check=True
            break
        else:
            check=False
    if(check==False):
        print(arr[i]) 
        break

#Properties -
# a^a=0
# a^0=a 
# a^b^a^d^b =d
#Time complexity : O(n)
unique=0
for i in range(len(arr)):
    unique ^= arr[i]
# print(unique)
