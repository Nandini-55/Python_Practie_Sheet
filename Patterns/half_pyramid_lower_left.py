row = int(input("Enter no. of rows : "))
for i in range(row):
    for j in range(i):
        print(" ",end="")
    for k in range(row-i):
        print("*",end="")
    print()