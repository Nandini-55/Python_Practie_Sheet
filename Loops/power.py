num = int(input("Enter the no. : "))
pow = int(input("Enter the power :"))
exponent = pow
# using operator
print("Result : ",num**pow )

# using while loop
result=num
while(pow>1):
    result*=num
    pow-=1
print("Result : ",result)

#using for loop
solution =1
for i in range(exponent):
    solution*=num
print(solution,end=" ")
