row =int(input("Enter no. of rows: "))
for i in range(1,row+1):
    for j in range(i):
        print("*",end="")
    print()