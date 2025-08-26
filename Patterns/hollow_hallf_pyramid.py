num = int(input("Enter no. of rows : "))
#time complexity - i*j
for i in range(num,0,-1):
    for j in range(i):
       if(j==0 or j==i-1) :print("*",end=" ")
       else:print(" ",end=" ")
    print()