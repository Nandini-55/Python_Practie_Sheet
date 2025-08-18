num = int(input("Enter the no. : "))
pow = int(input("Enter the power :"))
print("Result : ",num**pow )
result=num
while(pow>1):
    result*=num
    pow-=1
print("Result : ",result)
