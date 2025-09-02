num = int(input("Enter the no. : "))
original = num
sum_of_digits=0

while(num!=0):
    sum_of_digits+=num%10
    num//=10

print("Sum of digits in ",original ," is :",sum_of_digits)