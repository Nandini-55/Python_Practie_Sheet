num = int(input("Enter the no. : "))
original = num
reverse =0

while(num!=0):
    digit=num%10
    reverse=(reverse*10)+digit
    num//=10

print("Reverse of  ",original ," is :" ,reverse)