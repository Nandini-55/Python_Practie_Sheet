n=int(input())
code=[]
for i in range(n):
    code.append(int(input()))
for i in range(n):
    ele=code[i]
    evenSum=0
    oddSum=0
    while(ele!=0):
        digit=ele%10
        if(digit%2==0):
            evenSum+=digit
        else:
            oddSum+=digit
        ele//=10
    if(evenSum%4==0 or oddSum%3==0):
        print("Yes")
    else:
        print("No")