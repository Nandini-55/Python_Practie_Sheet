num = int(input("Enter a no. : "))
original = num 
digits=0
while(num!=0):
    num//=10 #// - is used to ignore decimal values  or for integer division
    digits+=1
print(original,"has",digits,"digits.")