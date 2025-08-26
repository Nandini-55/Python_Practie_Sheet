row = int(input("Enter no. of rows : "))
for i in range(1,row+1):
    for j in range(row-i+1):
        print("*",end="")
    for j in range(1,i):
        print("  ",end="")
    for j in range(row-i+1):
        print("*",end="")
   
    print()
for i in range(1,row):
    for j in range(i):
        print("*",end="")
    for j in range(row-i):
        print("  ",end="")
    for j in range(i):
        print("*",end="")
    print()