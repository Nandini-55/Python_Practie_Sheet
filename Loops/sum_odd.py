num = int(input("Enter the no. : "))
i=1
sum_of_odd=0
while(i<=num):
    if(i%2!=0): sum_of_odd+=i
    i+=1

print("Sum of odd no. : ",sum_of_odd)