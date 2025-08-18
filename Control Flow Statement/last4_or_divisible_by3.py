num = int(input("Enter the no. : "))

if(num%10==4 and num%3==0):
    print("Last digit is 4 and divisible by 3.")
elif(num%10==4):
    print("Last digit is 4.")
elif(num%3==0):
    print("Divisible by 3.")
else:
    print("No condition is true.")
    