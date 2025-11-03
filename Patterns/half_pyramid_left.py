num = int(input("Enter no. of rows : "))
for i in range(num):
    for j in range(num-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()