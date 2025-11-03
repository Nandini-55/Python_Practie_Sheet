row =int(input("Enter no. of rows: "))
for i in range(row):
    for j in range(row//2):
        if(i==(row//2) and j==0):
            continue
        print("*",end=" ")
    print()