row = int(input("Enter no. of rows : "))
for i in range(row):
    if(i==0 or i==row-1):
        for j in range(row):
            print("*",end=" ")
    else:
        for j in range(row//2):
            print("*",end=" ")

    print()