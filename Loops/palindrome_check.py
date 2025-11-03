num = int(input("Enter the no. you want to check for palindrome : "))
reverse=0
original = num
while(num!=0):
    digit = num%10
    reverse=(reverse*10)+digit
    num//=10

if(reverse==original):
    print("Is palindrome")
else:
    print("Is not palindrome")

