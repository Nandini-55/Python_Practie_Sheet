num = int(input("Enter no. of rows : "))
#time complexity - i*j
for i in range(num,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#time Complexity - i
for i in range(num,0,-1):
        print("* "*i)