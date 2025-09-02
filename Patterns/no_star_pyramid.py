row=int(input("Enter no. of rows : "))
for i in range(row,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(row-i):
            print("*",end=" ")
    for k in range(1,row-i):
            print("*",end=" ")
    print()