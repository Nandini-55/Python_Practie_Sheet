row =int(input("Enter no. of rows: "))
for i in range((row*2),0,-1):
    if(i%2!=0):
        for j in range(i):
            print("*",end="")
        print()
    