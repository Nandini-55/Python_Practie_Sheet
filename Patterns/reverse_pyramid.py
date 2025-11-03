num=int(input("Enter no. of rows : "))
for i in range(1,num+1):
    for j in range(1,i):
        print(" ",end="")
    for j in range(num+1-i):
        print("*",end=" ")
    
    print()