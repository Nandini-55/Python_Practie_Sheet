num = int(input("Enter a no. :"))
# using while loop
i=1
while(i<=num):
    if(i%2!=0):print(i)
    i+=1

#using for loop
for i in range(1,num+1,2):
     print(i,end=" ")