row =int(input("Enter no. of rows: "))
for i in range(1,(row*2)+1):
    if(i%2!=0):
        for j in range(i):
            print("*",end="")
        print()
    